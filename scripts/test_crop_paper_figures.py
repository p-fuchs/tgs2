from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from crop_paper_figures import build_default_targets, pending_targets


class CropQueueTests(unittest.TestCase):
    def test_pending_targets_skip_existing_outputs(self) -> None:
        targets = build_default_targets(Path("/tmp/pres2"))

        with tempfile.TemporaryDirectory() as tmpdir:
            processed_dir = Path(tmpdir)
            (processed_dir / "1A.png").write_bytes(b"done")
            (processed_dir / "2B.png").write_bytes(b"done")

            pending = pending_targets(targets, processed_dir)

        self.assertNotIn("1A.png", [target.output_name for target in pending])
        self.assertNotIn("2B.png", [target.output_name for target in pending])
        self.assertEqual(pending[0].output_name, "1B.png")
        self.assertEqual(pending[-1].output_name, "3B.png")

    def test_pending_targets_can_include_existing_outputs(self) -> None:
        targets = build_default_targets(Path("/tmp/pres2"))

        with tempfile.TemporaryDirectory() as tmpdir:
            processed_dir = Path(tmpdir)
            (processed_dir / "1A.png").write_bytes(b"done")

            pending = pending_targets(
                targets,
                processed_dir,
                skip_existing=False,
            )

        self.assertEqual(len(pending), len(targets))
        self.assertEqual(pending[0].output_name, "1A.png")


if __name__ == "__main__":
    unittest.main()
