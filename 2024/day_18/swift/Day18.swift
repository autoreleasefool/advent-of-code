import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day18: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		var grid = buildGrid()

		input.integersByLine()
			.prefix(1024)
			.map { Point2($0[0], $0[1]) }
			.forEach { grid[$0] = "#" }

		let start: Point2 = .zero
		let end: Point2 = Point2(70, 70)

		let path = breadthFirstSearch(
			start: start,
			goal: end,
			graph: grid,
			adjacent: { adjacentPoints($0, in: grid) }
		)!.dropFirst()

		return path.count.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let corruptionPoints = input.integersByLine()
			.map { Point2($0[0], $0[1]) }

		let start: Point2 = .zero
		let end: Point2 = Point2(70, 70)

		let firstBlockedPath = binarySearch(
			items: corruptionPoints,
			compare: { index, _ in
				var grid = buildGrid()
				corruptionPoints
					.prefix(index)
					.forEach { grid[$0] = "#" }

				let path = breadthFirstSearch(
					start: start,
					goal: end,
					graph: grid,
					adjacent: { adjacentPoints($0, in: grid) }
				)

				if path != nil {
					return -1
				} else {
					grid[corruptionPoints[index - 1]] = "."
					return breadthFirstSearch(
						start: start,
						goal: end,
						graph: grid,
						adjacent: { adjacentPoints($0, in: grid) }
					) == nil ? 1 : 0
				}
			}
		)

		let lastCorruptionPoint = corruptionPoints[firstBlockedPath! - 1]
		return "\(lastCorruptionPoint.x),\(lastCorruptionPoint.y)"
	}

	// MARK: Helpers

	private func adjacentPoints(_ point: Point2, in grid: [Point2: Character]) -> [Point2] {
		point.adjacentPoints()
			.filter { grid[$0] == "." }
	}

	private func buildGrid() -> [Point2: Character] {
		product((0...70), (0...70))
			.map { Point2($0, $1) }
			.reduce(into: [:]) { $0[$1] = "." }
	}
}
