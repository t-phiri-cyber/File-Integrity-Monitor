
import tempfile
import unittest
from pathlib import Path

from src.baseline import create_baseline
from src.monitor import check_integrity


class TestFileIntegrityMonitor(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

        self.test_directory = self.root / "monitored"
        self.test_directory.mkdir()

        self.baseline_file = self.root / "baseline.json"

        (self.test_directory / "sample.txt").write_text(
            "Original content",
            encoding="utf-8"
        )

        self.baseline = create_baseline(
            self.test_directory,
            self.baseline_file
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_unchanged_file(self):
        results = check_integrity(
            self.test_directory,
            self.baseline
        )
        self.assertIn("sample.txt", results["unchanged"])

    def test_modified_file(self):
        (self.test_directory / "sample.txt").write_text(
            "Modified content",
            encoding="utf-8"
        )

        results = check_integrity(
            self.test_directory,
            self.baseline
        )
        self.assertIn("sample.txt", results["modified"])

    def test_added_file(self):
        (self.test_directory / "new-file.txt").write_text(
            "New file",
            encoding="utf-8"
        )

        results = check_integrity(
            self.test_directory,
            self.baseline
        )
        self.assertIn("new-file.txt", results["added"])

    def test_deleted_file(self):
        (self.test_directory / "sample.txt").unlink()

        results = check_integrity(
            self.test_directory,
            self.baseline
        )
        self.assertIn("sample.txt", results["deleted"])

    def test_nested_file(self):
        nested_directory = self.test_directory / "subfolder"
        nested_directory.mkdir()

        (nested_directory / "nested.txt").write_text(
            "Nested content",
            encoding="utf-8"
        )

        baseline = create_baseline(
            self.test_directory,
            self.baseline_file
        )

        results = check_integrity(
            self.test_directory,
            baseline
        )
        self.assertIn(
            "subfolder\\nested.txt",
            results["unchanged"]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
