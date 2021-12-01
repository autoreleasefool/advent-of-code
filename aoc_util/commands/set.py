from argparse import ArgumentParser
from datetime import datetime, timezone, timedelta

from aoc_util.challenge import Challenge
from aoc_util.language import Language
from aoc_util.session import Session


_valid_years = range(2015, 2022)
_valid_days = range(1, 26)


class Set:
    @classmethod
    def build_parser(cls, parser: ArgumentParser):
        parser.description = "Set properties for future runs"
        parser.add_argument("--token", help="Set the session token", type=str)
        parser.add_argument(
            "-l",
            help="The language of the script to run",
            type=Language,
            choices=list(Language),
        )
        parser.add_argument(
            "-y",
            help="The year of the challenge to run",
            type=int,
            choices=_valid_years,
        )
        parser.add_argument(
            "-d", help="The day of the challenge to run", type=int, choices=_valid_days
        )
        parser.add_argument(
            "-t", "--today", action="store_true", help="Set the challenge to today"
        )
        parser.add_argument(
            "-n", "--next", action="store_true", help="Set the challenge to tomorrow"
        )

    def run(self, session: Session):
        args = session.command_args

        if args.token:
            session.token = args.token
            print("updated token")
        if args.l:
            session.language = args.l
            print(f"updated language to {session.language}")
        if args.d or args.y or args.today or args.next:
            now = datetime.now(timezone(timedelta(hours=-5)))
            if args.today:
                if now.month != 12:
                    raise ValueError("advent of code is not currently running. try -n?")
                if now.day not in _valid_days:
                    raise ValueError("advent of code is not currently running")
                session.challenge.year = now.year
                session.challenge.day = now.day
            elif args.next:
                if now.month == 11 and now.day == 30:
                    session.challenge.year = now.year
                    session.challenge.day = 1
                else:
                    if now.month != 12:
                        raise ValueError("advent of code is not running tomorrow")
                    if now.day + 1 not in _valid_days:
                        raise ValueError("advent of code is not running tomorrow")
                    session.challenge.year = now.year
                    session.challenge.day = now.day + 1
            else:
                if args.y:
                    session.challenge.year = args.y
                    session.challenge = Challenge(args.y, session.challenge.day)
                if args.d:
                    session.challenge.day = args.d
                    session.challenge = Challenge(session.challenge.year, args.d)
            print(f"updated challenge to {session.challenge}")

        session.validate()
        session.cache()
