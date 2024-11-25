import AdventSupport
import Foundation

public class Year2015Day02: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
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

	public func solvePart2(_ input: Input) async throws -> String? {
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
