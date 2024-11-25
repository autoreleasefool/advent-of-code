import AdventSupport
import Algorithms
import ArgumentParser
import Foundation

extension Commands {
	struct Test: AsyncParsableCommand {
		mutating func run() async throws {
			for year in Year.allCases {
				try await testYear(year)
			}
		}

		private func testYear(_ year: Year) async throws {
			print("===== \(year) =====")

			var totalDuration: Duration = .zero

			for day in 1...25 {
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

				var input = (try? Input(challenge: challenge)) ?? Input(contents: "")

				let solution = try await solver.solve(&input)

				guard solution.part1 != nil && solution.part2 != nil else {
					print("❌ (\(year), \(day)): Missing solution")
					continue
				}

				let challengeDuration = (solution.part1Duration ?? .zero) + (solution.part2Duration ?? .zero)
				totalDuration += challengeDuration

				do {
					try solution.validate(against: challenge)
					print("✅ (\(year), \(day)): \(solution.part1 ?? "-") | \(solution.part2 ?? "-") | \(challengeDuration)")
				} catch {
					print("❌ (\(year), \(day)): \(error.localizedDescription)")
				}
			}

			print("Total duration for \(year): \(totalDuration)")
		}
	}
}
