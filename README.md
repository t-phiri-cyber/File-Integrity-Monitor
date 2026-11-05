

\# File Integrity Monitor



A Python-based file integrity monitoring tool that uses SHA-256 cryptographic hashing to detect unauthorised or unexpected changes to files.



\## Project Overview



The File Integrity Monitor establishes a trusted baseline of files within a selected directory. Subsequent scans compare current file hashes against the stored baseline to identify changes.



The tool is designed as a practical cybersecurity project demonstrating file integrity monitoring, cryptographic hashing, baseline verification, logging and automated testing.



\## Key Features



\- SHA-256 file hashing.

\- Baseline creation and storage in JSON format.

\- Detection of modified files.

\- Detection of newly added files.

\- Detection of deleted files.

\- Identification of unchanged files.

\- Recursive scanning of nested directories.

\- Detection of baseline tampering using a separate SHA-256 checksum.

\- Automated scan report generation.

\- Activity logging and error handling.

\- Automated unit testing.



\## Technology



\- Python 3

\- SHA-256

\- JSON

\- Python standard library

\- unittest testing framework



No third-party Python packages are required.



\## Project Structure



```text

File-Integrity-Monitor/

├── baselines/

│   ├── baseline.json

│   └── baseline.sha256

├── logs/

│   └── fim.log

├── reports/

│   └── scan-report.txt

├── src/

│   ├── baseline.py

│   ├── baseline\_security.py

│   ├── hash\_engine.py

│   ├── main.py

│   ├── monitor.py

│   └── reporter.py

├── test-files/

│   ├── empty.txt

│   ├── sample.txt

│   ├── unexpected.txt

│   └── subfolder/

│       └── nested.txt

├── tests/

│   └── test\_integrity.py

├── .gitignore

└── README.md

```



\## Installation



Clone the repository:



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



Navigate into the project directory:



```bash

cd File-Integrity-Monitor

```



Python 3 is required.



\## Usage



\### 1. Create a baseline



```bash

python -m src.main baseline

```



This records the SHA-256 hashes of files in the monitoring directory.



\### 2. Scan for changes



```bash

python -m src.main scan

```



The scan compares current file hashes against the saved baseline.



\### 3. Select a directory



```bash

python -m src.main baseline --directory test-files

```



To scan the same directory:



```bash

python -m src.main scan --directory test-files

```



\### 4. Run automated tests



```bash

python -m unittest discover -s tests -v

```



\## Test Results



The project has been manually tested and includes five automated unit tests.



| Test | Result |

|---|---|

| Unchanged file detection | Passed |

| Modified file detection | Passed |

| Added file detection | Passed |

| Deleted file detection | Passed |

| Nested file detection | Passed |



\*\*Automated test result: 5/5 passed.\*\*



Additional manual tests covered empty files, missing directories, baseline tampering, checksum verification, report generation and activity logging.



\## Security Considerations



The tool uses SHA-256 to identify changes in file contents.



A separate checksum is used to verify the integrity of the baseline JSON file.



The checksum is stored locally alongside the baseline. This provides detection of accidental or unauthorised changes but does not protect against an attacker who can modify both files.



For stronger production security, the checksum should be stored separately with restricted access or protected using a keyed authentication mechanism.



\## Current Limitations



\- Local directory monitoring rather than continuous real-time monitoring.

\- No graphical user interface.

\- No centralised monitoring dashboard.

\- No external alerting integration.

\- Baseline and checksum are stored locally.



\## Future Improvements



\- Real-time monitoring using filesystem event detection.

\- Secure baseline storage.

\- Email or dashboard alerts.

\- Configurable monitoring directories.

\- Improved automated test coverage.

\- Centralised logging and monitoring.



\## Learning Outcomes



This project demonstrates practical understanding of:



\- Cryptographic hashing.

\- File integrity monitoring.

\- Baseline verification.

\- Security logging.

\- Error handling.

\- Python development.

\- Automated testing.

\- Basic cybersecurity control implementation.



\## Disclaimer



This is an educational cybersecurity project developed and tested in a local environment. It is not a replacement for enterprise file integrity monitoring or endpoint detection and response solutions.



