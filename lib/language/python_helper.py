from lib.commands.command import Command
from lib.language.language_helper import LanguageHelper
from lib.language.language_id import LanguageID
from lib.session import Session
from os import path
from shutil import which
import subprocess


class PythonHelper(LanguageHelper):
    def __init__(self):
        super().__init__(LanguageID.PYTHON)

    @property
    def file_extension(self) -> str:
        return ".py"

    @property
    def execution_directory(self) -> str:
        return path.join(".", "lib", "helpers", "python")

    def solve_challenge(self, session: Session) -> subprocess.Popen[str]:
        # Python uses a custom runner to inject helper logic
        command = filter(
            None,
            [
                which("python3"),
                "-m",
                "runner",
                "--year",
                str(session.challenge.year),
                "--day",
                str(session.challenge.day),
                "--session",
                session.token,
                "--submit" if session.command == Command.SUBMIT else None,
            ],
        )

        return self.open_pipe(command)
