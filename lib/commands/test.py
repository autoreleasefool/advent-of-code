from argparse import ArgumentParser
from lib.challenge import Challenge
from lib.commands.run import Run
from lib.session import Session
from os import path


class Test:
    @classmethod
    def build_parser(cls, parser: ArgumentParser):
        parser.description = "Test all challenges in the set year for correctness"
        parser.add_argument(
            "--strict", action="store_true", help="Limit all runs to 15 seconds"
        )

    def run(self, session: Session):
        current_challenge = session.challenge
        current_args = session.command_args
        strict_mode = session.command_args.strict

        parser = ArgumentParser()
        Run.build_parser(parser)
        session.command_args = parser.parse_args([])

        for day in range(1, 26):
            session.challenge = Challenge(current_challenge.year, day)
            session.save = False

            if not path.exists(session.challenge.output_file):
                print(f"no solution exists for {session.challenge}, skipping.")
                continue

            Run().run(session)

        session.challenge = current_challenge
        session.command_args = current_args
