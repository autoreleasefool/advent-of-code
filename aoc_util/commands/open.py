import webbrowser

from aoc_util.commands.base_command import BaseCommand
from aoc_util.session import Session


class Open(BaseCommand):
    def run(self, session: Session):
        webbrowser.open(session.challenge.url, new=2)
