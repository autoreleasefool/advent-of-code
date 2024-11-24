import AdventSupport
import ArgumentParser
import Foundation
import Year2015

extension Commands {
	struct Run: AsyncParsableCommand {
		@Flag(help: "Save the output")
		var save = false

		@Flag(name: .shortAndLong, help: "Copy the latest solution to the clipboard")
		var copyToClipboard = false

		@SessionStorage("year")
		var sessionYear: Year = .y24

		@SessionStorage("day")
		var sessionDay: Int = 1

		mutating func run() async throws {
			let challenge = Challenge(year: sessionYear, day: sessionDay)
			try await challenge.fetchInput(verbose: true)

			let input = try Input(challenge: challenge)

			let solver = try challenge.retrieveSolver()

			let solution = try await solver.solve(input)

			solution.log()

			if copyToClipboard {
				solution.copyToClipboard()
			}

			if save {
				try solution.write(to: challenge, verbose: true)
			} else {
				try solution.validate(against: challenge, verbose: true)
			}
		}
	}
}
