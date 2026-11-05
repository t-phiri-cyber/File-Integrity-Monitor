
from pathlib import Path

from src.hash_engine import calculate_sha256


def check_integrity(directory, baseline_data):
    directory = Path(directory).resolve()

    if not directory.is_dir():
        raise NotADirectoryError(f"Directory not found: {directory}")

    original_files = baseline_data["files"]
    current_files = {}

    for file_path in sorted(directory.rglob("*")):
        if file_path.is_file():
            relative_path = str(file_path.relative_to(directory))
            current_files[relative_path] = calculate_sha256(file_path)

    results = {
        "modified": [],
        "added": [],
        "deleted": [],
        "unchanged": []
    }

    for file_name, current_hash in current_files.items():
        if file_name not in original_files:
            results["added"].append(file_name)

        elif current_hash != original_files[file_name]:
            results["modified"].append(file_name)

        else:
            results["unchanged"].append(file_name)

    for file_name in original_files:
        if file_name not in current_files:
            results["deleted"].append(file_name)

    return results
