import sys
import logging
from core.number_analyzer import analyze_number


def run():
    if len(sys.argv) != 2:
        logging.error("Usage: python src/main.py <number>")
        return

    try:
        number = int(sys.argv[1])
    except ValueError:
        logging.error("Invalid number.")
        return

    result = analyze_number(number)

    logging.info("Analysis result:")
    for key, value in result.items():
        logging.info(f"{key}: {value}")