from argparse import ArgumentParser
from lib.session import Session
from os import path
import requests


class Fetch:
    @classmethod
    def build_parser(cls, parser: ArgumentParser):
        parser.description = "Fetch the input for the set challenge"

    def run(self, session: Session):
        session.validate(require_token=True)

        headers = {
            'User-Agent': 'https://github.com/autoreleasefool/advent-of-code',
        }

        # Already cached input
        if path.exists(session.input_file):
            print(f"input already exists for {session.challenge}, not fetching")
            return

        # Fetch the input with the session
        cookies = {"session": session.token}
        r = requests.get(session.challenge.input_url, cookies=cookies, headers=headers)

        # Cache to the file
        with open(session.input_file, "w") as f:
            f.write(r.text)
            print(f"Fetched and cached input for ${session.challenge}")
