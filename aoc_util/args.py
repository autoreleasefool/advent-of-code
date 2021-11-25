from argparse import ArgumentParser
import sys

from aoc_util.challenge import Challenge
from aoc_util.commands.command import Command
from aoc_util.commands.fetch import Fetch
from aoc_util.commands.open import Open
from aoc_util.language import Language
from aoc_util.session import Session


_valid_years = range(2015, 2021)
_valid_days = range(1, 26)


def parse_args(args=None):
  if args is None:
    args = sys.argv[1:]

  parser = ArgumentParser(description='Advent of Code')

  parser.add_argument(
    '-f', '--fetch',
    action='store_true',
    help='Fetch the input for the year/day'
  )

  parser.add_argument(
    '-r', '--run',
    action='store_true',
    help='Run the program for the language/year/day/part'
  )

  parser.add_argument(
    '-s', '--save',
    action='store_true',
    help='Save the output'
  )

  parser.add_argument(
    '-o', '--open',
    action='store_true',
    help='Open the challenge in the browser'
  )

  parser.add_argument(
    '-t', '--test',
    action='store_true',
    help='Run full test suite for a single language/year',
  )

  parser.add_argument('--session', help='Set your session. Cached for future runs')

  parser.add_argument('COMMAND', help='Command to run', type=Command, choices=list(Command))
  parser.add_argument('LANG', nargs='?', help='The language of the script to run. Cached for future runs', type=Language, choices=list(Language))
  parser.add_argument('YEAR', nargs='?', help='The year of the script to run. Cached for future runs', type=int, choices=_valid_years)
  parser.add_argument('DAY', nargs='?', help='The day of the script to run. Cached for future runs', type=int, choices=_valid_days)

  parsed = parser.parse_args(args)

  session = Session(parsed.session, parsed.LANG, parsed.YEAR, parsed.DAY)
  command = Command(parsed.COMMAND)
  command.run(session)
