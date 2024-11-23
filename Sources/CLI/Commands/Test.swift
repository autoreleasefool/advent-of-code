import AdventSupport
import Algorithms
import ArgumentParser
import Foundation

extension Commands {
	struct Test: AsyncParsableCommand {
		mutating func run() async throws {
			let allYears = Year.allCases
			let allDays = 1...25

			for (year, day) in product(allYears, allDays) {
				let challenge = Challenge(year: year, day: day)
				guard challenge.hasStarted else { continue }

				let solver: Solver
				do {
					solver = try challenge.retrieveSolver()
				} catch {
					print("⚠️ (\(year), \(day)): Solution unavailable")
					continue
				}

				try await challenge.fetchInput()

				let input = (try? Input(challenge: challenge)) ?? Input(contents: "")

				let solution = try await solver.solve(input)

				guard solution.part1 != nil && solution.part2 != nil else {
					print("❌ (\(year), \(day)): Missing solution")
					continue
				}

				do {
					try solution.validate(against: challenge)
					print("✅ (\(year), \(day)): \(solution.part1 ?? "-") | \(solution.part2 ?? "-")")
				} catch {
					print("❌ (\(year), \(day)): \(error.localizedDescription)")
				}
			}
		}
	}
}
