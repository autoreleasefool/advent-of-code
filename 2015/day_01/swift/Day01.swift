import AdventSupport
import Foundation

public class Year2015Day01: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		input.contents
			.reduce(0) { floor, c in floor + (c == "(" ? 1 : -1) }
			.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		var floor = 0
		for (index, c) in input.contents.enumerated() {
			floor += c == "(" ? 1 : -1
			if floor == -1 {
				return (index + 1).description
			}
		}

		return ""
	}
}
