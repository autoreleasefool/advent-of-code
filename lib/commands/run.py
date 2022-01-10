from argparse import ArgumentParser
from lib.commands import Command
from lib.language import language_helper
from lib.session import Session
from os import path
import time


class Run:
    @classmethod
    def build_parser(cls, parser: ArgumentParser):
        parser.description = "Run the set challenge script"
        parser.add_argument("--save", action="store_true", help="save the output")

    def run(self, session: Session):
        session.validate(require_token=True)
        print(f"=====\nRunning {session.challenge}:")

        start_time = time.perf_counter()
        helper = language_helper(session.language)
        return_code, output = helper.run(session)
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
                            print("✅ your solution appears correct!")
                        else:
                            print(
                                f"❌ solution does not match one found in {session.challenge.output_file}"
                            )
                            print(f"\texpected: {solution}")
                            print(f"\treceived: {output}")
                else:
                    print("⚠️ solution does not exist for validation. skipping...")

        # When running the submit command, return the output
        if session.command == Command.SUBMIT:
            return output
