import AdventSupport
import ArgumentParser
import Foundation
import Year2015

extension Commands {
	struct Run: AsyncParsableCommand {
		@Flag(help: "Save the output")
		var save = false

		@SessionStorage("year")
		var sessionYear: Year = .y24

		@SessionStorage("day")
		var sessionDay: Int = 1

		mutating func run() async throws {
			let challenge = Challenge(year: sessionYear, day: sessionDay)
			try await challenge.fetchInput()

			let input = Input(challenge: challenge)

			let solver = try challenge.retrieveSolver()

			let solution = try await solver.solve(input)

			if save {
				try solution.write(to: challenge)
			} else {
				try solution.validate(against: challenge)
				print("Solution appears correct!")
			}
		}
	}
}

// MARK: Challenge Extension

fileprivate extension Challenge {
	func retrieveSolver() throws -> Solver {
		guard let solverClass = Bundle.main.classNamed(solverClassName),
					let solverType = solverClass as? Solver.Type else {
			throw Commands.Run.CommandError.solutionClassNotFound(solverClassName)
		}
		
		return solverType.init()
	}
}

// MARK: Error

extension Commands.Run {
	enum CommandError: LocalizedError {
		case solutionClassNotFound(String)

		var errorDescription: String? {
			switch self {
			case let .solutionClassNotFound(className):
				return "Could not find solution class \(className)"
			}
		}
	}
}
