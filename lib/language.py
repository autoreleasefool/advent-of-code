from enum import Enum
from os import path


class Language(Enum):
    PYTHON = "python"

    @property
    def file_extension(self):
        if self == Language.PYTHON:
            return ".py"

    @property
    def compiled_extension(self):
        if self == Language.PYTHON:
            return None

    @property
    def compilation_command(self):
        if self == Language.PYTHON:
            return None

    @property
    def src_prefix(self):
        if self == Language.PYTHON:
            return None

    @property
    def starter_file(self):
        return path.join(
            ".", "lib", "helpers", self.value, f"starter{self.file_extension}"
        )

    @property
    def supporting_files_directory(self):
        return path.join(".", "lib", "helpers", self.value, "supporting_files")
