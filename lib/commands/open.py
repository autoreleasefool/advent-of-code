from argparse import ArgumentParser
from lib.session import Session
import webbrowser


class Open:
    @classmethod
    def build_parser(cls, parser: ArgumentParser):
        parser.description = "Open the description for the set challenge"

    def run(self, session: Session):
        webbrowser.open(session.challenge.url, new=2)
        print(f"opened {session.challenge}")
