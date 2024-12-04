import AdventSupport
import Foundation

public class Year2016Day18: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		countSafeSpaces(
			in: buildMap(startingFrom: input.contents, upTo: 40)
		)
		.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		countSafeSpaces(
			in: buildMap(startingFrom: input.contents, upTo: 400_000)
		)
		.description
	}

	// MARK: Helpers

	private func buildMap(startingFrom: String, upTo: Int) -> [[Character]] {
		var map = [Array(startingFrom)]

		while map.count < upTo {
			var nextRow: [Character] = []
			for i in 0..<map.last!.count {
				let left = map.last![safely: i - 1] ?? "."
				let center = map.last![i]
				let right = map.last![safely: i + 1] ?? "."

				let traps = [left.isTrap, center.isTrap, right.isTrap]
				let isTrap = [[true, true, false], [false, true, true], [true, false, false], [false, false, true]].contains(traps)
				nextRow.append(isTrap ? "^" : ".")
			}
			map.append(nextRow)
		}

		return map
	}

	private func countSafeSpaces(in map: [[Character]]) -> Int {
		map.reduce(into: 0) { $0 += $1.count - $1.count(where: \.isTrap) }
	}
}

extension Character {
	var isTrap: Bool {
		self == "^"
	}
}
