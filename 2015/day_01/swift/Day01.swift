import AdventSupport
import Foundation

public class Year2015Day01: Solver {
	public required init() {}

	public func solve(_ input: Input) async throws -> Solution {
		let part1Solution = try await solvePart1(input)
		let part2Solution = try await solvePart2(input)

		return Solution(part1: part1Solution, part2: part2Solution)
	}

	// MARK: Part 1

	private func solvePart1(_ input: Input) async throws -> String {
		try input.read()
			.reduce(0) { floor, c in floor + (c == "(" ? 1 : -1) }
			.description
	}

	// MARK: Part 2

	private func solvePart2(_ input: Input) async throws -> String {
		var floor = 0
		for (index, c) in try input.read().enumerated() {
			floor += c == "(" ? 1 : -1
			if floor == -1 {
				return (index + 1).description
			}
		}

		return ""
	}
}
