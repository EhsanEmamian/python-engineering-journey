# Python Engineering Journey

A structured learning project for building Python backend engineering fundamentals

## Features

- Analyze a number from the command line
- Detect whether the number is even or odd
- Detect whether the number is positive
- Calculate the square of the number
- Optional verbose logging

## Project Structure

- `src/main.py` → application entry point
- `src/core/cli.py` → command-line interface handling
- `src/core/number_analyzer.py` → business logic
- `tests/` → test files

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate

Install dependencies:

pip install -r requirements.txt
pip install -e .

Usage
Run the program:

python src/main.py 5

Run with verbose mode:

python src/main.py 5 --verbose
Run Tests
pytest -q
Purpose

This project is part of a long-term backend engineering learning path focused on clean structure, testing, and production-oriented thinkn
