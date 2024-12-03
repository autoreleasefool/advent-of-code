import AdventSupport
import Foundation

public class Year2024Day03: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		input.lines()
			.reduce(into: 0) { sum, line in
				sum += line.matches(of: /mul\((\d{1,3}),(\d{1,3})\)/)
					.map { Int($0.output.1)! * Int($0.output.2)! }
					.reduce(0, +)
			}
			.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		var isEnabled = true

		return input.lines()
			.reduce(into: 0) { sum, line in
				sum += line.matches(of: /do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)/)
					.filter {
						if $0.output.0 == "do()" {
							isEnabled = true
							return false
						} else if $0.output.0 == "don't()" {
							isEnabled = false
							return false
						}

						return isEnabled
					}
					.map { Int($0.output.1!)! * Int($0.output.2!)! }
					.reduce(0, +)
			}
			.description
	}
}
