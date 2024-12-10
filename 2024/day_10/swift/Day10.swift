import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day10: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
		self.grid = mapGridToPoints(input.characterGrid())
	}

	private var grid: [Point2: Character]!

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		grid
			.filter { $0.value == "0" }
			.map { $0.key }
			.reduce(0) { totalScore, trailhead in
				var summitsReached: Set<Point2> = []
				return totalScore + trailheadScore(from: trailhead, summitsReached: &summitsReached)
			}
			.description
	}

	private func trailheadScore(from: Point2, summitsReached: inout Set<Point2>, uniqueSummits: Bool = true) -> Int {
		guard grid[from] != "9" else {
			return !uniqueSummits || summitsReached.insert(from).inserted ? 1 : 0
		}

		guard let gridDigit = grid[from], let value = Int(String(gridDigit)) else { return 0 }

		return Direction.allCases
			.map { from.move($0) }
			.filter { grid[$0] != nil && Int(String(grid[$0]!)) == value + 1 }
			.reduce(0) { totalScore, point in
				totalScore + trailheadScore(from: point, summitsReached: &summitsReached, uniqueSummits: uniqueSummits)
			}
	}

	private func trailheadRating(from: Point2) -> Int {
		var summitsReached: Set<Point2> = []
		return trailheadScore(from: from, summitsReached: &summitsReached, uniqueSummits: false)
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		grid
			.filter { $0.value == "0" }
			.map { $0.key }
			.reduce(0) { totalScore, trailhead in
				totalScore + trailheadRating(from: trailhead)
			}
			.description
	}
}
