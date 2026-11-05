
import hashlib
from pathlib import Path


def calculate_sha256(file_path):
    """
    Calculate the SHA-256 hash of a file.

    Reads the file in chunks to avoid loading
    large files entirely into memory.
    """

    file_path = Path(file_path)

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()
