from shutil import copy
import os

from aoc_util.commands.base_command import BaseCommand
from aoc_util.session import Session
from aoc_util.util.filesystem import copy_directory


class Create(BaseCommand):
    def run(self, session: Session):
        if os.path.exists(session.working_directory):
            return

        supporting_directory = session.language.supporting_files_directory
        starter_file = session.language.starter_file

        os.makedirs(
            os.path.join(
                session.working_directory,
                session.language.src_prefix if session.language.src_prefix else "",
            )
        )

        if os.path.exists(starter_file):
            starter_dest = os.path.join(
                session.working_directory,
                session.language.src_prefix if session.language.src_prefix else "",
                f"day{session.challenge.day_with_padding}{session.language.file_extension}",
            )

            copy(starter_file, starter_dest)

            with open(starter_dest) as r:
                text = (
                    r.read()
                    .replace("__year__", str(session.challenge.year))
                    .replace("__day__", str(session.challenge.day))
                )
            with open(starter_dest, "w") as w:
                w.write(text)

        if os.path.exists(supporting_directory):
            copy_directory(supporting_directory, session.working_directory)
