import AdventSupport
import Foundation

public class Year2024Day04: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
		self.grid = mapGridToPoints(input.characterGrid())
	}

	private var grid: [Point2: Character]!

	// MARK: Part 1


	public func solvePart1(_ input: Input) async throws -> String? {
		grid
			.filter { $0.value == "X" }
			.reduce(into: 0) { count, startPoint in
				count += CompoundDirection.allCases
					.count { findXmas(from: startPoint.key, direction: $0.point) }
			}
			.description
	}

	private func findXmas(from: Point2, direction: Point2) -> Bool {
		"XMAS"
			.enumerated()
			.allSatisfy { index, char in
				grid[from + direction * index] == char
			}
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		grid
			.filter { $0.value == "A" }
			.reduce(into: 0) { count, startPoint in
				let northEast = grid[startPoint.key + CompoundDirection.northEast.point]
				let southWest = grid[startPoint.key + CompoundDirection.southWest.point]

				let northWest = grid[startPoint.key + CompoundDirection.northWest.point]
				let southEast = grid[startPoint.key + CompoundDirection.southEast.point]

				guard let northEast, let northWest, let southEast, let southWest else { return }

				let hasFirstMas = "MS".contains(northEast) && "MS".contains(southWest) && northEast != southWest
				let hasSecondMas = "MS".contains(northWest) && "MS".contains(southEast) && northWest != southEast

				if hasFirstMas && hasSecondMas {
					count += 1
				}
			}
			.description
	}
}
