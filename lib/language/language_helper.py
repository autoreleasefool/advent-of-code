from abc import ABC, abstractmethod, abstractproperty
from lib.language.language_id import LanguageID
from lib.session import Session
from lib.util.filesystem import cd
from os import listdir, path
from typing import List, Optional, Tuple
import subprocess


class LanguageHelper(ABC):
    id: LanguageID
    session: Session

    def __init__(self, id: LanguageID, session: Session):
        self.id = id
        self.session = session

    @abstractproperty
    def file_extension(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def solve_challenge(self) -> Optional[subprocess.Popen[str]]:
        raise NotImplementedError()

    def run(self) -> Tuple[int, str]:
        return self._run()

    def _run(self, within_execution_directory: bool = False) -> Tuple[int, str]:
        if not within_execution_directory and self.execution_directory:
            with cd(self.execution_directory):
                return self._run(within_execution_directory=True)

        print("---")
        p = self.solve_challenge()

        if p is None:
            return 1, "failed to run"

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
    def execution_directory(self) -> Optional[str]:
        return None

    @property
    def language_support_directory(self) -> str:
        return path.join(self.session.base_directory, "lib", "helpers", self.id.value)

    @property
    def starter_file(self) -> str:
        return path.join(self.language_support_directory, f"starter{self.file_extension}")

    @property
    def supporting_files_directory(self):
        return path.join(self.language_support_directory, "supporting_files")

    @property
    def helper_library(self):
        return path.join(self.language_support_directory, "aoc")

    @property
    def helper_files(self) -> List[str]:
        return list(
            map(lambda x: path.join(self.helper_library, x), listdir(self.helper_library))
        )

    @property
    def root_file(self) -> str:
        return path.join(
            self.session.working_directory,
            f"day{self.session.challenge.day_with_padding}{self.file_extension}",
        )

    def open_pipe(self, command: str) -> subprocess.Popen[str]:
        return subprocess.Popen(
            command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, text=True
        )
