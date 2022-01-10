from lib.commands.command import Command
from lib.language.language_helper import LanguageHelper
from lib.language.language_id import LanguageID
from lib.session import Session
from os import path
from shutil import which
import subprocess


class PythonHelper(LanguageHelper):
    def __init__(self, session: Session):
        super().__init__(LanguageID.PYTHON, session)

    @property
    def file_extension(self) -> str:
        return ".py"

    @property
    def execution_directory(self) -> str:
        return path.join(self.session.base_directory, "lib", "helpers", "python")

    def solve_challenge(self) -> subprocess.Popen[str]:
        # Python uses a custom runner to inject helper logic
        command = filter(
            None,
            [
                which("python3"),
                "-m",
                "runner",
                self.session.base_directory,
                "--year",
                str(self.session.challenge.year),
                "--day",
                str(self.session.challenge.day),
                "--token",
                self.session.token,
                "--input",
                self.session.input_file,
                "--log",
                self.session.log_file,
                "--submit" if self.session.command == Command.SUBMIT else None,
            ],
        )

        return self.open_pipe(command)
