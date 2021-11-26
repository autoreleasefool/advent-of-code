from shutil import copy
import os

from aoc_util.commands.base_command import BaseCommand
from aoc_util.session import Session
from aoc_util.util.filesystem import copy_directory


class Create(BaseCommand):
    def run(self, session: Session):
        if os.path.exists(session.working_directory):
            print(f"did not create {session.challenge} because it already exists.")
            return

        supporting_directory = session.language.supporting_files_directory
        starter_file = session.language.starter_file

        # Create the directory for files to placed into
        os.makedirs(
            os.path.join(
                session.working_directory,
                session.language.src_prefix if session.language.src_prefix else "",
            )
        )

        if os.path.exists(starter_file):
            # Copy the base starter file and replace macros
            copy(starter_file, session.root_file)

            with open(session.root_file) as r:
                text = (
                    r.read()
                    .replace("__year__", str(session.challenge.year))
                    .replace("__day__", str(session.challenge.day))
                )
            with open(session.root_file, "w") as w:
                w.write(text)

            print(
                f"created starter file for {session.challenge} in {session.language.value}"
            )

        if os.path.exists(supporting_directory):
            # Copy any supporting files the language needs
            copy_directory(supporting_directory, session.working_directory)
            print(
                f"copied supporting files for {session.challenge} in {session.language.value}"
            )
