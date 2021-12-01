from argparse import ArgumentParser
from os import path
from shutil import which
from typing import List
import subprocess
import time

from aoc_util.commands.command import Command
from aoc_util.language import Language
from aoc_util.session import Session
from aoc_util.util.filesystem import cd


class Run:
    @classmethod
    def build_parser(cls, parser: ArgumentParser):
        parser.description = "Run the set challenge script"
        parser.add_argument("--save", action="store_true", help="save the output")

    def run(self, session: Session):
        session.validate(require_token=True)
        print(f"=====\nRunning {session.challenge}:")

        command = self._get_command(session)

        start_time = time.perf_counter()
        return_code, output = self._run(session, command)
        end_time = time.perf_counter()

        if return_code != 0:
            print(f"error: {output}")
            return

        print(f"runtime: {(end_time - start_time)}")

        # If saving, overwrite the current solution
        if session.command == Command.RUN or session.command == Command.TEST:
            if output and session.command_args.save:
                print(f"saving output {output}")
                with open(session.challenge.output_file, "w") as f:
                    f.write(output)
            else:
                # When not saving, compare the solution to the current solution and report
                if path.exists(session.challenge.output_file):
                    with open(session.challenge.output_file) as f:
                        solution = f.read()
                        if solution == output:
                            print("your solution appears correct!")
                        else:
                            print(
                                f"solution does not match one foud in {session.challenge.output_file}"
                            )
                            print(f"\texpected: {solution}")
                            print(f"\treceived: {output}")
                else:
                    print("solution does not exist for validation. skipping...")

        # When running the submit command, return the output
        if session.command == Command.SUBMIT:
            return output

    def _run(self, session: Session, command: List[str], nested=False):
        if session.compilation_directory and not nested:
            # Some languages require commands to be run from the source directory, so cd in
            with cd(session.compilation_directory):
                return self._run(session, command, nested=True)

        print("---")
        p = subprocess.Popen(
            command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, text=True
        )
        output = []

        while True:
            stream = p.stdout.readline()

            if stream == "" and p.poll() is not None:
                break

            if stream:
                output.append(stream.strip())
                print(stream.strip())

        print("---")
        return p.returncode, "\n".join(output)

    def _get_command(self, session: Session):
        if session.language == Language.PYTHON:
            # Python uses a custom runner to inject helper logic
            return filter(
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
        elif session.language == Language.SWIFT or session.language == Language.HASKELL:
            # Swift and haskell compile to an executable, the run the executable
            compile_result = self._compile(session)
            if compile_result.returncode != 0:
                print("compilation failed")
                return None
            return [session.compiled_file]
        elif session.language == Language.RUBY:
            # Ruby runs a given source file
            return [session.language.value, session.root_file]
        elif session.language == Language.RUST:
            # Rust compiles and executes within a directory
            return ["cargo", "run"]

    def _compile(self, session: Session):
        return subprocess.run(
            session.language.compilation_command
            + [
                session.root_file,
                "-o",
                session.compiled_file,
            ]
        )
