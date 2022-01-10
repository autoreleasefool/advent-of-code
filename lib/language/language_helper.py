from abc import ABC, abstractmethod, abstractproperty
from lib.language.language_id import LanguageID
from lib.session import Session
from lib.util.filesystem import cd
from os import path
from typing import Optional, Tuple
import subprocess


class LanguageHelper(ABC):
    def __init__(self, id: LanguageID):
        self.id = id

    @abstractproperty
    def file_extension(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def solve_challenge(self, session: Session) -> subprocess.Popen[str]:
        raise NotImplementedError()

    def run(self, session: Session) -> Tuple[int, str]:
        return self._run(session)

    def _run(
        self, session: Session, within_working_directory: bool = False
    ) -> Tuple[int, str]:
        if not within_working_directory and self.execution_directory:
            with cd(self.execution_directory):
                return self._run(session, within_working_directory=True)

        print("---")
        p = self.solve_challenge(session)

        output = []
        while True:
            stream = p.stdout.readline()

            if stream == "" and p.poll() is not None:
                break

            if stream:
                output.append(stream.rstrip())
                print(stream.rstrip())

        print("---")
        return p.returncode, "\n".join(output)

    @property
    def starter_file(self) -> str:
        return path.join(
            ".", "lib", "helpers", self.id.value, f"starter{self.file_extension}"
        )

    @property
    def supporting_files_directory(self):
        return path.join(".", "lib", "helpers", self.id.value, "supporting_files")

    @property
    def helper_library(self):
        return path.join(".", "lib", "helpers", self.id.value, "aoc")

    @property
    def execution_directory(self) -> Optional[str]:
        return None

    def root_file(self, session: Session) -> str:
        return path.join(
            session.working_directory,
            f"day{session.challenge.day_with_padding}{self.file_extension}",
        )

    def open_pipe(self, command: str) -> subprocess.Popen[str]:
        return subprocess.Popen(
            command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, text=True
        )
