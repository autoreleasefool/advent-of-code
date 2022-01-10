from argparse import ArgumentParser
from lib.language import language_helper
from lib.util.filesystem import copy_directory
from lib.session import Session
from shutil import copy
import os


class Create:
    @classmethod
    def build_parser(cls, parser: ArgumentParser):
        parser.description = "Create a starter file for the set challenge"

    def run(self, session: Session):
        if os.path.exists(session.working_directory):
            print(f"did not create {session.challenge} because it already exists.")
            return

        helper = language_helper(session.language)
        supporting_directory = helper.supporting_files_directory
        starter_file = helper.starter_file
        root_file = helper.root_file(session)

        # Create the directory for files to placed into
        os.makedirs(session.working_directory)

        if os.path.exists(starter_file):
            # Copy the base starter file and replace macros
            copy(starter_file, root_file)

            with open(root_file) as r:
                text = (
                    r.read()
                    .replace("__year__", str(session.challenge.year))
                    .replace("__day__", str(session.challenge.day))
                )
            with open(root_file, "w") as w:
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
