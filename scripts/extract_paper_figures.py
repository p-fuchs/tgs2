from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageChops


ROOT = Path("/Users/pfuchs/mimuw/tgs/pres2")
PAPER_PDF = ROOT / "materials" / "womens-connectivity-extreme-networks.pdf"
WORK_DIR = ROOT / "build" / "pdfimages"
ORIGINAL_DIR = ROOT / "assets" / "figures" / "original"
PROCESSED_DIR = ROOT / "assets" / "figures" / "processed"


# pdfimages extracts the three main figure composites in stable order:
# img-000 = Figure 1, img-001 = Figure 2, img-002 = Figure 3.
FIGURE_MAP: dict[str, dict[str, tuple[float, float, float, float]]] = {
    "img-000.png": {
        "1A.png": (0.00, 0.00, 0.29, 0.995),
        "1B.png": (0.33, 0.00, 0.995, 0.30),
        "1C.png": (0.33, 0.33, 0.995, 0.69),
        "1D-left.png": (0.34, 0.70, 0.64, 0.995),
        "1D-right.png": (0.69, 0.70, 0.995, 0.995),
    },
    "img-001.png": {
        "2A.png": (0.00, 0.00, 0.21, 0.995),
        "2B.png": (0.24, 0.00, 0.63, 0.33),
        "2C.png": (0.24, 0.32, 0.63, 0.66),
        "2D.png": (0.24, 0.64, 0.63, 0.995),
        "2E.png": (0.64, 0.00, 0.995, 0.75),
    },
    "img-002.png": {
        "3A.png": (0.00, 0.00, 0.50, 0.995),
        "3B.png": (0.50, 0.00, 0.995, 0.995),
    },
}


def ensure_embedded_images() -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    for old in WORK_DIR.glob("img-*.png"):
        old.unlink()
    subprocess.run(
        ["pdfimages", "-png", str(PAPER_PDF), str(WORK_DIR / "img")],
        check=True,
    )


def trim_near_white(image: Image.Image, threshold: int = 245, padding: int = 10) -> Image.Image:
    rgb = image.convert("RGB")
    bg = Image.new("RGB", rgb.size, (255, 255, 255))
    diff = ImageChops.difference(rgb, bg)
    diff = diff.point(lambda px: 255 if px > (255 - threshold) else 0)
    bbox = diff.getbbox()
    if bbox is None:
        return image

    left = max(0, bbox[0] - padding)
    top = max(0, bbox[1] - padding)
    right = min(rgb.width, bbox[2] + padding)
    bottom = min(rgb.height, bbox[3] + padding)
    return image.crop((left, top, right, bottom))


def crop_fraction(image: Image.Image, box: tuple[float, float, float, float]) -> Image.Image:
    width, height = image.size
    left = int(width * box[0])
    top = int(height * box[1])
    right = int(width * box[2])
    bottom = int(height * box[3])
    return image.crop((left, top, right, bottom))


def write_outputs() -> None:
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    for composite_name, outputs in FIGURE_MAP.items():
        source_path = WORK_DIR / composite_name
        if not source_path.exists():
            raise FileNotFoundError(f"Missing extracted composite: {source_path}")

        shutil.copy2(source_path, ORIGINAL_DIR / composite_name)
        with Image.open(source_path) as source_image:
            for output_name, box in outputs.items():
                cropped = crop_fraction(source_image, box)
                trimmed = trim_near_white(cropped)
                trimmed.save(PROCESSED_DIR / output_name, optimize=True)
                print(f"wrote {output_name}: {trimmed.width}x{trimmed.height}")


def main() -> None:
    ensure_embedded_images()
    write_outputs()


if __name__ == "__main__":
    main()
