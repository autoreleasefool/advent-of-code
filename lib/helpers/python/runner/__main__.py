from argparse import ArgumentParser
from importlib import import_module, reload
from os import path
import sys


parser = ArgumentParser(description="Advent of Code, Python runner")
parser.add_argument("BASE_DIRECTORY", help="Set base directory")
parser.add_argument("--token", help="Set your session token")
parser.add_argument("--year", help="Set the challenge year")
parser.add_argument("--day", help="Set the challenge day")
parser.add_argument("--part", help="Set the challenge part")
parser.add_argument("--input", help="Set input file")
parser.add_argument("--log", help="Set log file")
parser.add_argument("--submit", action="store_true", help="Submit your solution")
parsed = parser.parse_args()

day = int(parsed.day)
day_str = str(day) if day >= 10 else "0{day}".format(day=day)

# Append challenge scripts to path for import
sys.path.append(
    path.join(
        parsed.BASE_DIRECTORY,
        parsed.year,
        "day_{day}".format(day=day_str),
        "python",
    )
)

# Append data module to path so scripts can import
sys.path.append(path.join(parsed.BASE_DIRECTORY, "lib", "helpers", "python", "aoc"))

from aoc import AOC

AOC.token = parsed.token
AOC.is_submitting = parsed.submit
AOC.input_file = parsed.input
AOC.log_file = parsed.log

# Import the day's solution as a module, allowing top level code to run, outputting the solution
challenge_module = import_module(f"day{day_str}")

# If test data is set running the challenge above, run it again forcing the test data to be skipped
if AOC.contains_test_input:
    AOC.force_skip_test = True
    print("--running again, with real input--")
    reload(challenge_module)
