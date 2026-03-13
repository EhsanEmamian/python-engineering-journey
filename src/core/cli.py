import argparse
import logging
from core.number_analyzer import analyze_number


def run():
    parser = argparse.ArgumentParser(
        description="Analyze properties of a number"
    )

    parser.add_argument(
        "number",
        type=int,
        help="Number to analyze"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    result = analyze_number(args.number)

    logging.info("Analysis result:")
    for key, value in result.items():
        logging.info(f"{key}: {value}")