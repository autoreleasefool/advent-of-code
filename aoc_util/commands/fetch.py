from os import path
import requests

from aoc_util.session import Session


class Fetch():
    def run(self, session: Session):
        session.validate(require_token=True)
        input_file = session.challenge.input_file

        # Already cached input
        if path.exists(input_file):
            print(f"input already exists for {session.challenge}, not fetching")
            return

        # Fetch the input with the session
        cookies = {"session": session.token}
        r = requests.get(session.challenge.input_url, cookies=cookies)

        # Cache to the file
        with open(input_file, "w") as f:
            f.write(r.text)
            print(f"Fetched and cached input for ${session.challenge}")
