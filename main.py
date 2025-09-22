import argparse
import sys

from config.db_config import get_engine
from config.test_db_connection import test_connection
from src.etl import inspect_data
from src.etl import extract


def run_tests():
    print("\n Running database configuration test...")
    print("🔁 About to get engine...")
    engine = get_engine()
    print("✅ Engine created:", engine)

    print("\n Running database connection test...")
    test_connection()
    print("Database connection test completed.\n")

    # print("Inspecting data...")
    # inspect_data.run_inspection()

    # print("Extracting data...")
    # extract.run_extraction()


def main():
    parser = argparse.ArgumentParser(description="Premier League Data Mart Runner")
    parser.add_argument("--test", action="store_true", help="Run DB + inspection + extraction tests")
    args = parser.parse_args()

    if args.test:
        run_tests()
    else:
        print(" No command provided. Use `--test` to run tests.")
        sys.exit(1)


if __name__ == "__main__":
    main()
