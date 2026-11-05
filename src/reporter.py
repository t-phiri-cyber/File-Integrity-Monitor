
from datetime import datetime, timezone
from pathlib import Path
import logging


def configure_logging(log_file):
    log_file = Path(log_file)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        force=True
    )


def generate_report(results, report_file):
    report_file = Path(report_file)
    report_file.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).isoformat()

    lines = [
        "FILE INTEGRITY MONITORING REPORT",
        "=" * 40,
        f"Scan time: {timestamp}",
        ""
    ]

    for category, files in results.items():
        lines.append(f"{category.upper()}: {len(files)}")

        for file_name in files:
            lines.append(f"  - {file_name}")

        lines.append("")

    report_file.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    return report_file


def log_results(results):
    for category, files in results.items():
        for file_name in files:
            logging.warning(
                "%s file detected: %s",
                category.upper(),
                file_name
            )

    if not any(results.values()):
        logging.info("No file integrity changes detected.")
