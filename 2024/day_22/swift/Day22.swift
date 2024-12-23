import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day22: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
		input = Input(contents: """
1
2
3
2024
""")
}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		input
			.integersByLine()
			.map {
				var secret = $0[0]
				for _ in 0..<2_000 {
					secret = evolve(secret: secret)
				}
				return secret
			}
			.reduce(0, +)
			.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		return nil
	}

	// MARK: Helpers

	private func evolve(secret: Int) -> Int {
		var secret = secret

		// Step 1
		secret = ((secret * 64) ^ secret) % 16_777_216

		// Step 2
		secret = ((secret / 32) ^ secret) % 16_777_216

		// Step 3
		secret = ((secret * 2048) ^ secret) % 16_777_216

		return secret
	}
}
