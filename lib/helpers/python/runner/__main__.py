from argparse import ArgumentParser
import importlib
import os
import sys


parser = ArgumentParser(description="Advent of Code, Python runner")
parser.add_argument("--session", help="Set your session token")
parser.add_argument("--year", help="Set the challenge year")
parser.add_argument("--day", help="Set the challenge day")
parser.add_argument("--part", help="Set the challenge part")
parser.add_argument("--submit", action="store_true", help="Submit your solution")
parsed = parser.parse_args()

day = int(parsed.day)
day_str = str(day) if day >= 10 else "0{day}".format(day=day)

# Append challenge scripts to path for import
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "..",
        "..",
        parsed.year,
        "day_{day}".format(day=day_str),
        "python",
    )
)

# Append data module to path so scripts can import
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "aoc"))

from aoc import AOC

AOC.session = parsed.session
AOC.is_submitting = parsed.submit

# Import the day's solution as a module, allowing top level code to run, outputting the solution
challenge_module = importlib.import_module(f"day{day_str}")

# If test data is set running the challenge above, run it again forcing the test data to be skipped
if AOC.contains_test_input:
    AOC.force_skip_test = True
    print("--running again, with real input--")
    importlib.reload(challenge_module)
