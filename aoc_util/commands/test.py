from os import path

from aoc_util.commands.run import Run
from aoc_util.session import Session


class Test():
    def run(self, session: Session):
        for day in range(1, 26):
            day_session = session.session_with_day(day)
            session.save = False

            if not path.exists(day_session.challenge.output_file):
                print(f"no solution exists for {day_session.challenge}, breaking.")

            Run().run(day_session)
