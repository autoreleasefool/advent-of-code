from argparse import ArgumentParser
import requests

from aoc_util.commands.run import Run
from aoc_util.session import Session


class Submit:
    @classmethod
    def build_parser(cls, parser: ArgumentParser):
        parser.description = "Submit the set challenge"
        parser.add_argument(
            "PART",
            help="which part of the day's challenge to submit",
            type=int,
            choices=[1, 2],
        )

    def run(self, session: Session):
        print("submission is currently a WIP")
        # session.validate(require_token=True)
        # part = session.command_args.PART

        # # Run command will return the last line output when the Submit command is running
        # output = Run().run(session)

        # for line in output.splitlines():
        #     if line.startswith(f"p{part}="):
        #         submission = line[3:]

        # if not submission:
        #     print(f"no submission for part {part} in {output}")
        #     return

        # # Submit the answer with the current "level"
        # cookies = {"session": session.token}
        # r = requests.post(
        #     session.challenge.submit_url,
        #     cookies=cookies,
        #     json={
        #         'level': str(part),
        #         'answer': submission
        #     }
        # )

        # print(r)
        # print(r.text)
        # print(r.json())
