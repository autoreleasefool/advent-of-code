import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day10: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: """
//89010123
//78121874
//87430965
//96549874
//45678903
//32019012
//01329801
//10456732
//""")
	}

	private var grid: [Point2: Character] = [:]
	private var countedFromTrailhead: [Point2: Set<Point2>] = [:]

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		grid = mapGridToPoints(input.characterGrid())

		var total = 0
		for (point, value) in grid where value == "0" {
//			print("Trailhead: ", point)
			total += score(point, point)
		}
		return total.description
	}

	private func score(_ point: Point2, _ trailhead: Point2) -> Int {
		guard grid[point] != nil else { return 0 }


		if grid[point] == "9" {
			if countedFromTrailhead[trailhead, default: []].insert(point).inserted {
				return 1
			} else {
				return 0
			}
//		guard counted.insert(point).inserted else {
//				return 0
//			}
//
////			print("Terminus, point: \(point)")
//			return 1
		}

		guard grid[point]!.isNumber, let value = Int(String(grid[point]!)) else { return 0 }

		var s = 0
		for d in Direction.allCases {
			let newPoint = point.move(d)
			guard grid[newPoint] != nil, let newValue = Int(String(grid[newPoint]!)) else { continue }

			if newValue == value + 1 {
//				print("Moving from \(point) to \(newPoint)")
				s += score(newPoint, trailhead)
			}
		}
		return s
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		grid = mapGridToPoints(input.characterGrid())

		var total = 0
		for (point, value) in grid where value == "0" {
//			print("Trailhead: ", point)
			total += rating(point, point)
		}

		return total.description
	}

	func rating(_ point: Point2, _ trailhead: Point2) -> Int {
		guard grid[point] != nil else { return 0 }

		if grid[point] == "9" {
			print("Terminus, point: \(point)")
			return 1
//			if countedFromTrailhead[trailhead, default: []].insert(point).inserted {
//				return 1
//			} else {
//				return 0
//			}
//		guard counted.insert(point).inserted else {
//				return 0
//			}
//
////			print("Terminus, point: \(point)")
//			return 1
		}

		guard grid[point]!.isNumber, let value = Int(String(grid[point]!)) else { return 0 }

		var s = 0
		for d in Direction.allCases {
			let newPoint = point.move(d)
			guard grid[newPoint] != nil, let newValue = Int(String(grid[newPoint]!)) else { continue }

			if newValue == value + 1 {
//				print("Moving from \(point) to \(newPoint)")
				s += rating(newPoint, trailhead)
			}
		}
		return s
	}
}
