import AdventSupport
import Foundation

public class Year2015Day02: Solver {
	public required init() {}

	public func solve(_ input: Input) async throws -> Solution {
		let part1Solution = try await solvePart1(input)
		let part2Solution = try await solvePart2(input)

		return Solution(part1: part1Solution, part2: part2Solution)
	}

	// MARK: Part 1

	private func solvePart1(_ input: Input) async throws -> String? {
		input.integersByLine()
			.reduce(0) { total, dimensions in
				let l = dimensions[0]
				let w = dimensions[1]
				let h = dimensions[2]

				let sides = [l * w, w * h, h * l]
				return total + 2 * sides.reduce(0, +) + sides.min()!
			}
			.description
	}

	// MARK: Part 2

	private func solvePart2(_ input: Input) async throws -> String? {
		input.integersByLine()
			.reduce(0) { total, dimensions in
				let l = dimensions[0]
				let w = dimensions[1]
				let h = dimensions[2]

				let perimeters = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
				return total + l * w * h + perimeters.min()!
			}
			.description
	}
}
