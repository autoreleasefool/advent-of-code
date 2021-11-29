from enum import Enum
from os import path


class Language(Enum):
    HASKELL = "haskell"
    PYTHON = "python"
    RUBY = "ruby"
    RUST = "rust"
    SWIFT = "swift"

    @property
    def file_extension(self):
        if self == Language.HASKELL:
            return ".hs"
        elif self == Language.PYTHON:
            return ".py"
        elif self == Language.RUBY:
            return ".rb"
        elif self == Language.RUST:
            return ".rs"
        elif self == Language.SWIFT:
            return ".swift"

    @property
    def compiled_extension(self):
        if self == Language.HASKELL:
            return ".hsx"
        elif self == Language.PYTHON:
            return None
        elif self == Language.RUBY:
            return None
        elif self == Language.RUST:
            return None
        elif self == Language.SWIFT:
            return ".o"

    @property
    def compilation_command(self):
        if self == Language.HASKELL:
            return ["stack", "ghc", "--"]
        elif self == Language.PYTHON:
            return None
        elif self == Language.RUBY:
            return None
        elif self == Language.RUST:
            return None
        elif self == Language.SWIFT:
            return ["swiftc"]

    @property
    def src_prefix(self):
        if self == Language.HASKELL:
            return None
        elif self == Language.PYTHON:
            return None
        elif self == Language.RUBY:
            return None
        elif self == Language.RUST:
            return "src"
        elif self == Language.SWIFT:
            return None

    @property
    def starter_file(self):
        return path.join(".", "util", self.value, f"starter{self.file_extension}")

    @property
    def supporting_files_directory(self):
        return path.join(".", "util", self.value, "supporting_files")
