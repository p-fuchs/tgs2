"""Interactively crop figures from the Avram et al. (2019) paper PDF.

Ports the OpenCV cropping UI used in pres2/scripts/crop_paper_figures.py
to pres4. Renders each needed page of the paper PDF, then walks through
a queue of crop targets. For each target, drag a rectangle, preview,
then save / redo / skip / step back.

Usage::

    cd pres4
    uv run scripts/crop_paper_figures.py            # only pending targets
    uv run scripts/crop_paper_figures.py --include-existing   # re-crop everything
    uv run scripts/crop_paper_figures.py --from-target fig3_random.png
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np


ROOT = Path(__file__).resolve().parent.parent
PAPER_PDF = ROOT / "assets" / "avram_2019.pdf"
PAGES_DIR = ROOT / "build" / "pages"
ORIGINAL_DIR = ROOT / "assets" / "original"
PROCESSED_DIR = ROOT / "assets"
DISPLAY_PADDING_PX = 80
PAGE_DPI = 220


@dataclass(frozen=True)
class CropTarget:
    output_name: str
    page: int
    description: str

    def source_path(self) -> Path:
        return PAGES_DIR / f"page-{self.page:02d}.png"

    def output_path(self) -> Path:
        return PROCESSED_DIR / self.output_name


# Page numbers refer to the paper PDF (1-indexed).
TARGETS: tuple[CropTarget, ...] = (
    CropTarget("fig1_example.png", page=1,
               description="Figure 1 (p.1, top-right): underlying vs observed network --- two side-by-side network panels, red adversary, purple = added/fake."),
    CropTarget("fig2_moves.png", page=4,
               description="Figure 2 (p.4, top): local vs global adversarial moves --- two boxes of small graph cartoons. Original composite, kept for reference."),
    CropTarget("fig2_local.png", page=4,
               description="Figure 2 (p.4, top): LOCAL adversarial moves only --- crop the small graph cartoons in the LEFT box labeled 'Local adversarial moves'."),
    CropTarget("fig2_global_a.png", page=4,
               description="Figure 2 (p.4, top): GLOBAL adversarial moves --- FIRST half of the right (global) box. Two of the global-move panels."),
    CropTarget("fig2_global_b.png", page=4,
               description="Figure 2 (p.4, top): GLOBAL adversarial moves --- SECOND half of the right (global) box. The remaining global-move panels."),
    CropTarget("fig2_legend.png", page=4,
               description="Figure 2 (p.4, top): the small example graph + legend (node/edge color key) shown alongside the move panels."),
    CropTarget("fig3_random.png", page=6,
               description="Figure 3 (p.6, top third): Random Graph networks --- four bar-chart columns (closeness, eigenvector, betweenness, degree)."),
    CropTarget("fig4_scalefree.png", page=6,
               description="Figure 4 (p.6, middle third): Scale-free networks --- same four-column bar layout as Fig. 3."),
    CropTarget("fig5_smallworld.png", page=6,
               description="Figure 5 (p.6, bottom third): Small-world networks --- same four-column bar layout as Fig. 3."),
    CropTarget("fig6_cellular.png", page=7,
               description="Figure 6 (p.7, top half): Cellular networks --- four-column bar layout as Fig. 3."),
    CropTarget("fig7_distribution.png", page=7,
               description="Figure 7 (p.7, bottom half): distribution of centrality change --- 4-row x 3-col grid of density curves."),
)


def ensure_pages() -> None:
    """Render every page referenced by a target to PAGES_DIR."""
    needed = sorted({target.page for target in TARGETS})
    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    missing = [p for p in needed if not (PAGES_DIR / f"page-{p:02d}.png").exists()]
    if not missing:
        return

    if not PAPER_PDF.exists():
        raise FileNotFoundError(f"Paper PDF not found: {PAPER_PDF}")

    # Render every needed page in one pdftoppm call (per contiguous range
    # would be cleaner, but this is simple and only runs once).
    subprocess.run(
        [
            "pdftoppm", "-png", "-r", str(PAGE_DPI),
            "-f", str(min(needed)), "-l", str(max(needed)),
            str(PAPER_PDF),
            str(PAGES_DIR / "page"),
        ],
        check=True,
    )

    # pdftoppm zero-pads to width of last page number, normalise to 2-digit.
    for child in PAGES_DIR.glob("page-*.png"):
        suffix = child.stem.removeprefix("page-")
        if suffix.isdigit() and len(suffix) != 2:
            child.rename(PAGES_DIR / f"page-{int(suffix):02d}.png")


def pending_targets(targets: list[CropTarget], skip_existing: bool) -> list[CropTarget]:
    if not skip_existing:
        return targets
    return [t for t in targets if not t.output_path().exists()]


def fit_for_display(
    image: np.ndarray,
    max_width: int = 1500,
    max_height: int = 1000,
) -> tuple[np.ndarray, float]:
    height, width = image.shape[:2]
    scale = min(max_width / width, max_height / height, 1.0)
    if scale == 1.0:
        return image.copy(), 1.0

    resized = cv2.resize(
        image,
        (int(width * scale), int(height * scale)),
        interpolation=cv2.INTER_AREA,
    )
    return resized, scale


def crop_from_rect(image: np.ndarray, rect: tuple[int, int, int, int], scale: float) -> np.ndarray:
    x, y, width, height = rect
    if width <= 0 or height <= 0:
        return image[0:0, 0:0]

    left = max(0, int(round(x / scale)))
    top = max(0, int(round(y / scale)))
    right = min(image.shape[1], int(round((x + width) / scale)))
    bottom = min(image.shape[0], int(round((y + height) / scale)))
    return image[top:bottom, left:right]


def add_white_padding(image: np.ndarray, padding_px: int = DISPLAY_PADDING_PX) -> np.ndarray:
    if image.size == 0 or padding_px <= 0:
        return image
    return cv2.copyMakeBorder(
        image, padding_px, padding_px, padding_px, padding_px,
        borderType=cv2.BORDER_CONSTANT, value=(255, 255, 255),
    )


def show_preview(name: str, crop: np.ndarray) -> None:
    preview, _ = fit_for_display(crop, max_width=900, max_height=700)
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, preview)


def show_message(name: str, lines: list[str]) -> None:
    canvas = np.full((220, 1000, 3), 255, dtype=np.uint8)
    y = 50
    for line in lines:
        cv2.putText(
            canvas, line, (30, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 20, 20), 2, cv2.LINE_AA,
        )
        y += 36
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, canvas)


def wait_for_action(valid_keys: set[str]) -> str:
    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == 255:
            continue
        char = chr(key).lower()
        if char in valid_keys:
            return char


def save_original(source: np.ndarray, target: CropTarget) -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    out = ORIGINAL_DIR / target.source_path().name
    if not out.exists():
        cv2.imwrite(str(out), source)


def print_session_summary(queue: list[CropTarget]) -> None:
    print()
    print("=" * 78)
    print(f"  Figures to crop from {PAPER_PDF.name}  ({len(queue)} target(s))")
    print("=" * 78)
    for i, target in enumerate(queue, 1):
        print(f"  {i:>2}. {target.output_name:<22}  (page {target.page})")
        print(f"      {target.description}")
    print("=" * 78)
    print("  Controls: drag a rectangle, Enter/Space to confirm.")
    print("            s = save   r = redo   n = skip   p = previous   q = quit")
    print("=" * 78)
    print()


def run_crop_session(skip_existing: bool, start_from: str | None) -> int:
    ensure_pages()
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    queue = pending_targets(list(TARGETS), skip_existing=skip_existing)
    if start_from is not None:
        queue = [t for t in queue if t.output_name >= start_from]

    if not queue:
        print("No pending targets. Use --include-existing to re-crop saved outputs.")
        return 0

    print_session_summary(queue)

    index = 0
    while 0 <= index < len(queue):
        target = queue[index]
        source = cv2.imread(str(target.source_path()))
        if source is None:
            raise FileNotFoundError(f"Could not load page image {target.source_path()}")

        save_original(source, target)

        padded_source = add_white_padding(source)
        display_source, scale = fit_for_display(padded_source)
        window_name = f"Crop {index + 1}/{len(queue)} - {target.output_name}"
        print()
        print(f"[{index + 1}/{len(queue)}] {target.output_name}  (page {target.page})")
        print(target.description)
        print("Drag a rectangle and press Enter/Space to confirm it. Press c to cancel.")

        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, display_source)
        rect = cv2.selectROI(window_name, display_source, showCrosshair=True, fromCenter=False)
        crop = crop_from_rect(padded_source, rect, scale)

        if crop.size == 0:
            show_message(
                "Crop Action",
                [
                    "No crop selected.",
                    "r = retry   n = skip target   p = previous   q = quit",
                ],
            )
            action = wait_for_action({"r", "n", "p", "q"})
            cv2.destroyWindow("Crop Action")
            cv2.destroyWindow(window_name)
            if action == "r":
                continue
            if action == "n":
                index += 1
                continue
            if action == "p":
                index = max(0, index - 1)
                continue
            break

        show_preview("Crop Preview", crop)
        show_message(
            "Crop Action",
            [
                target.description,
                f"output: {target.output_name}    page {target.page}",
                "s = save   r = redo   n = skip   p = previous   q = quit",
            ],
        )
        action = wait_for_action({"s", "r", "n", "p", "q"})
        cv2.destroyWindow("Crop Preview")
        cv2.destroyWindow("Crop Action")
        cv2.destroyWindow(window_name)

        if action == "s":
            output_path = target.output_path()
            if not cv2.imwrite(str(output_path), crop):
                raise RuntimeError(f"Failed to write crop to {output_path}")
            print(f"Saved {output_path}")
            index += 1
            continue
        if action == "r":
            continue
        if action == "n":
            index += 1
            continue
        if action == "p":
            index = max(0, index - 1)
            continue
        break

    cv2.destroyAllWindows()
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Interactively crop paper figure panels from the Avram et al. (2019) PDF.",
    )
    parser.add_argument(
        "--include-existing",
        action="store_true",
        help="Re-crop targets whose output files already exist.",
    )
    parser.add_argument(
        "--from-target",
        dest="from_target",
        help="Start from this output file name, for example fig3_random.png.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return run_crop_session(
        skip_existing=not args.include_existing,
        start_from=args.from_target,
    )


if __name__ == "__main__":
    sys.exit(main())
