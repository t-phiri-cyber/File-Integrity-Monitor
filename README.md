# File Integrity Monitor

A Python-based cybersecurity tool that monitors files for unauthorised changes using SHA-256 cryptographic hashing and baseline verification.

## Project Overview

The File Integrity Monitor (FIM) establishes a cryptographic baseline of files within a selected directory. Subsequent scans compare current file hashes against the stored baseline to identify modifications, newly created files and deleted files.

The project demonstrates core cybersecurity principles associated with file integrity monitoring, data integrity, cryptographic hashing, security logging and automated testing.

## Key Features

- **SHA-256 hashing:** Generates cryptographic hashes to identify file changes.
- **Baseline creation:** Records file hashes in a JSON baseline.
- **Baseline protection:** Uses a separate SHA-256 checksum to verify baseline integrity.
- **Change detection:** Identifies modified, added and deleted files.
- **Nested directory monitoring:** Supports files in subdirectories.
- **Automated reporting:** Generates scan reports in text format.
- **Security logging:** Records monitoring activity.
- **Automated testing:** Includes unit tests for core integrity-monitoring functions.

## Technology Stack

- Python 3
- SHA-256 / hashlib
- JSON
- pathlib
- unittest
- Git and GitHub

## Project Structure

```text
File-Integrity-Monitor/
├── src/
│   ├── main.py
│   ├── hash_engine.py
│   ├── baseline.py
│   ├── baseline_security.py
│   ├── monitor.py
│   └── reporter.py
├── tests/
│   └── test_integrity.py
├── test-files/
├── baselines/
├── reports/
├── logs/
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/t-phiri-cyber/File-Integrity-Monitor.git
cd File-Integrity-Monitor
```

Python 3 is required. The project uses Python standard-library modules and does not require additional third-party packages for its core functionality.

## Usage

**1. Create the initial baseline:**

```bash
python -m src.main baseline
```

**2. Run an integrity scan:**

```bash
python -m src.main scan
```

The scan compares the monitored files against the stored baseline and produces a report.

## Testing

Run the automated unit tests:

```bash
python -m unittest discover -s tests -v
```

The test suite covers:

- Modified file detection.
- Newly added file detection.
- Deleted file detection.
- Nested file handling.
- Unchanged file verification.

**Test result:** 5 tests passed successfully.

## Practical Validation

The project was also tested through manual command-line exercises.

| Test scenario | Observed result |
|---|---|
| Modified file | Detected |
| Newly added file | Detected |
| Deleted file | Detected |
| Unchanged files | Correctly identified |
| Tampered baseline | Verification failed |
| Recreated baseline | Successful |
| Clean integrity scan | 0 modified, 0 added, 0 deleted |

The baseline tampering exercise confirmed that changing the stored baseline without updating its checksum caused verification to fail.

## Security Considerations and Limitations

- SHA-256 provides file-integrity verification, not file confidentiality.
- The baseline and checksum are stored locally; an attacker with sufficient access could potentially compromise both.
- The tool is intended as a practical file-integrity monitoring project, not a replacement for enterprise endpoint detection and response (EDR), SIEM or host-based intrusion detection systems.
- Monitoring is initiated through command-line scans rather than continuous real-time monitoring.

## Future Improvements

- Scheduled or continuous monitoring.
- Secure off-device baseline storage.
- Alert notifications for detected changes.
- File exclusion and configuration options.
- Integration with centralised security monitoring platforms.

## Author

**Thembelani Phiri**

Cybersecurity portfolio project demonstrating Python development, cryptographic hashing, file-integrity verification and security testing.

## Disclaimer

This project was developed for educational and portfolio purposes. Testing was conducted on local test files and did not involve unauthorised access to systems or data.
