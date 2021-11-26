from enum import Enum

from aoc_util.commands.create import Create
from aoc_util.commands.fetch import Fetch
from aoc_util.commands.open import Open
from aoc_util.commands.run import Run
from aoc_util.commands.test import Test
from aoc_util.session import Session


class Command(Enum):
    CREATE = "create"
    FETCH = "fetch"
    OPEN = "open"
    RUN = "run"
    TEST = "test"

    def run(self, session: Session):
        if self == Command.CREATE:
            Create().run(session)
        elif self == Command.FETCH:
            Fetch().run(session)
        elif self == Command.OPEN:
            Open().run(session)
        elif self == Command.RUN:
            Run().run(session)
        elif self == Command.TEST:
            Test().run(session)
