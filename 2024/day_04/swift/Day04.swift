import AdventSupport
import Foundation

public class Year2024Day04: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(
//			contents: """
//MMMSXXMASM
//MSAMXMSMSA
//AMXSXMAAMM
//MSAMASMSMX
//XMASAMXAMM
//XXAMMXXAMA
//SMSMSASXSS
//SAXAMASAAA
//MAMMMXMMMM
//MXMXAXMASX
//"""
//		)
	}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let grid = input.characterGrid()

		var count = 0
		for (y, row) in grid.enumerated() {
			for (x, cell) in row.enumerated() {
				if cell == "X" {
					var searched = Set<Set<Direction?>>()
					for dir in Direction.allCases {
						for dir2 in Direction.allCases + [nil] {
							guard dir != dir2 else { continue }
							guard searched.insert([dir, dir2]).inserted else { continue }
							if findXmas(from: Point2(x, y), firstDir: dir, secondDir: dir2, in: grid) {
								count += 1
							}
						}
					}
				}
			}
		}
		return count.description
	}

	func findXmas(from: Point2, firstDir: Direction, secondDir: Direction?, in grid: [[Character]]) -> Bool{
		var xmas = "XMAS"
		var current = from

//		var pp = from == Point2(5, 0)
//		if pp {
//			print(current, xmas, firstDir, secondDir)
//		}

		while !xmas.isEmpty && current.y >= 0 && current.y < grid.count && current.x >= 0 && current.x < grid[current.y].count {

			if grid[current.y][current.x] == xmas.first {
				xmas.removeFirst()
				current += firstDir.point
				if let secondDir {
					current += secondDir.point
				}
			} else {
				break
			}

//			print(current, xmas)
		}

//		if xmas.isEmpty {
//			print(from, firstDir.value, secondDir?.value ?? "")
//		}
		return xmas.isEmpty
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let grid = input.characterGrid()

		var count = 0
		for (y, row) in grid.enumerated() {
			for (x, cell) in row.enumerated() {
				guard y > 0 && y < grid.count - 1 && x > 0 && x < row.count - 1 else { continue }
				if cell == "A" {
					let topLeft = grid[y - 1][x - 1]
					let topRight = grid[y - 1][x + 1]
					let bottomLeft = grid[y + 1][x - 1]
					let bottomRight = grid[y + 1][x + 1]

					let firstMas = "MS".contains(topLeft) && "MS".contains(bottomRight) && topLeft != bottomRight
					let secondMas = "MS".contains(topRight) && "MS".contains(bottomLeft) && topRight != bottomLeft

					if firstMas && secondMas {
						count += 1
					}
				}
			}
		}

		return count.description
	}
}

extension Direction {
	var value: String {
		switch self {
		case .north: "U"
		case .south: "D"
		case .west: "L"
		case .east: "R"
		}
	}
}

extension Direction {
	var point: Point2 {
		switch self {
		case .north: Point2(0, -1)
		case .south: Point2(0, 1)
		case .west: Point2(-1, 0)
		case .east: Point2(1, 0)
		}
	}
}
