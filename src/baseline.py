
import json
from pathlib import Path
from datetime import datetime, timezone

from src.hash_engine import calculate_sha256
from src.baseline_security import save_baseline_checksum


def create_baseline(directory, baseline_file):
    directory = Path(directory).resolve()
    baseline_file = Path(baseline_file)

    if not directory.is_dir():
        raise NotADirectoryError(f"Directory not found: {directory}")

    baseline = {}

    for file_path in sorted(directory.rglob("*")):
        if file_path.is_file():
            relative_path = str(file_path.relative_to(directory))
            baseline[relative_path] = calculate_sha256(file_path)

    baseline_data = {
        "directory": str(directory),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "files": baseline
    }

    baseline_file.parent.mkdir(parents=True, exist_ok=True)

    with baseline_file.open("w", encoding="utf-8") as file:
        json.dump(baseline_data, file, indent=4)

    checksum_file = baseline_file.with_suffix(".sha256")
    save_baseline_checksum(baseline_file, checksum_file)

    return baseline_data