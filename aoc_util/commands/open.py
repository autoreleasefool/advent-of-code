import webbrowser

from aoc_util.session import Session


class Open():
    def run(self, session: Session):
        webbrowser.open(session.challenge.url, new=2)
        print(f"opened {session.challenge}")
