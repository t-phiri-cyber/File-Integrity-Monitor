
import argparse
import json
import logging
from pathlib import Path

from src.baseline import create_baseline
from src.monitor import check_integrity
from src.reporter import configure_logging, generate_report, log_results


def load_baseline(baseline_file):
    baseline_file = Path(baseline_file)

    if not baseline_file.is_file():
        raise FileNotFoundError(
            f"Baseline not found: {baseline_file}. Create one first."
        )

    from src.baseline_security import verify_baseline_checksum

    checksum_file = baseline_file.with_suffix(".sha256")

    if not verify_baseline_checksum(baseline_file, checksum_file):
        raise ValueError(
            "Baseline integrity verification failed. "
            "The baseline or checksum file is missing or has changed."
        )

    with baseline_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def print_results(results):
    print("\nFILE INTEGRITY SCAN RESULTS")
    print("=" * 35)

    for category, files in results.items():
        print(f"\n{category.upper()}: {len(files)}")

        for file_name in files:
            print(f"  - {file_name}")


def main():
    parser = argparse.ArgumentParser(
        description="SHA-256 File Integrity Monitoring Tool"
    )

    parser.add_argument(
        "action",
        choices=["baseline", "scan"],
        help="Create a baseline or scan for file changes"
    )

    parser.add_argument(
        "--directory",
        default="test-files",
        help="Directory to monitor"
    )

    parser.add_argument(
        "--baseline",
        default="baselines/baseline.json",
        help="Baseline JSON file"
    )

    args = parser.parse_args()

    configure_logging("logs/fim.log")

    try:
        if args.action == "baseline":
            data = create_baseline(args.directory, args.baseline)
            print(
                f"Baseline created successfully. "
                f"{len(data['files'])} files recorded."
            )

            logging.info(
                "Baseline created for %s with %d files",
                args.directory,
                len(data["files"])
            )

        elif args.action == "scan":
            baseline = load_baseline(args.baseline)

            results = check_integrity(args.directory, baseline)

            print_results(results)

            report_path = generate_report(
                results,
                "reports/scan-report.txt"
            )

            log_results(results)

            print(f"\nReport saved to: {report_path}")
            print("Activity logged to: logs/fim.log")

    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}")
        logging.exception("File integrity operation failed")


if __name__ == "__main__":
    main()
