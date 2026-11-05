import hashlib
from pathlib import Path


def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()

    with Path(file_path).open("rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def save_baseline_checksum(baseline_file, checksum_file):
    checksum = calculate_file_hash(baseline_file)

    Path(checksum_file).parent.mkdir(parents=True, exist_ok=True)
    Path(checksum_file).write_text(checksum, encoding="utf-8")

    return checksum


def verify_baseline_checksum(baseline_file, checksum_file):
    baseline_path = Path(baseline_file)
    checksum_path = Path(checksum_file)

    if not baseline_path.is_file() or not checksum_path.is_file():
        return False

    expected = checksum_path.read_text(encoding="utf-8").strip()
    actual = calculate_file_hash(baseline_path)

    return actual == expected