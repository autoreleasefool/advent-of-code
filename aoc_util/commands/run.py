from os import path
from typing import List
import subprocess
import time

from aoc_util.commands.base_command import BaseCommand
from aoc_util.language import Language
from aoc_util.session import Session
from aoc_util.util.filesystem import cd


class Run(BaseCommand):
    def run(self, session: Session):
        session.validate(require_token=True)
        print(f"=====\nRunning {session.challenge}:")

        start_time = time.perf_counter()
        process: subprocess.CompletedProcess[str] = None

        # Execute the command to run the given language and challenge's solution
        if session.language.compile_from_directory:
            # Some languages require commands to be run from the source directory, so cd in
            with cd(session.working_directory):
                process = self._run(session)
        else:
            process = self._run(session)
        end_time = time.perf_counter()

        if process is None:
            print(f"failed to run {session.challenge}")
            return

        # Capture the output for comparison
        response = process.stdout.decode("utf-8").strip()
        error = process.stderr.decode("utf-8").strip()

        if error:
            print(error)

        if process.returncode != 0:
            print(response)
            return

        print(f"---\n{response}\n---")
        print(f"runtime: {(end_time - start_time)}")

        # If saving, overwrite the current solution
        if response and session.save:
            print(f"saving output {response}")
            with open(session.challenge.output_file, "w") as f:
                f.write(response)
        else:
            # When not saving, compare the solution to the current solution and report
            if path.exists(session.challenge.output_file):
                with open(session.challenge.output_file) as f:
                    solution = f.read()
                    if solution == response:
                        print("your solution appears correct!")
                    else:
                        print(
                            f"solution does not match one foud in {session.challenge.output_file}"
                        )
                        print(f"\texpected: {solution}")
                        print(f"\treceived: {response}")
            else:
                print("solution does not exist for validation. skipping...")

    def _run(self, session: Session):
        if session.language == Language.PYTHON:
            # Python uses a custom runner to inject helper logic
            with cd(path.join(".", "util", "python")):
                return self._execute(
                    [
                        "python",
                        "-m",
                        "runner",
                        "--year",
                        str(session.challenge.year),
                        "--day",
                        str(session.challenge.day),
                        "--session",
                        session.token,
                    ]
                )
        elif session.language == Language.SWIFT or session.language == Language.HASKELL:
            # Swift and haskell compile to an executable, the run the executable
            compile_result = self._compile(session)
            if compile_result.returncode != 0:
                print("compilation failed")
                return None
            return self._execute([session.compiled_file])
        elif session.language == Language.RUBY:
            # Ruby runs a given source file
            return self._execute([session.language.value, session.root_file])
        elif session.language == Language.RUST:
            # Rust compiles and executes within a directory
            return self._execute(["cargo", "run"])

    def _execute(self, command: List[str]):
        return subprocess.run(command, capture_output=True)

    def _compile(self, session: Session):
        return subprocess.run(
            session.language.compilation_command
            + [
                session.root_file,
                "-o",
                session.compiled_file,
            ]
        )
