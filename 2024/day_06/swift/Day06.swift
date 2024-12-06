import AdventSupport
import Foundation

public class Year2024Day06: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: """
//....#.....
//.........#
//..........
//..#.......
//.......#..
//..........
//.#..^.....
//........#.
//#.........
//......#...
//""")
	}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let grid = mapGridToPoints(input.characterGrid())

		var facing = Direction.north
		var position = grid.first { $0.value.isGuard }!.key
		var visited: Set<Point2> = [position]

		while grid[position] != nil {
			visited.insert(position)
			moveGuard(&position, dir: &facing, in: grid)
		}

		return visited.count.description
	}

	func moveGuard(_ point: inout Point2, dir: inout Direction, in grid: [Point2: Character]) {
		var nextPosition = point.move(dir)
		while grid[nextPosition]?.isObstruction == true {
			dir = switch dir {
			case .north: .east
			case .east: .south
			case .south: .west
			case .west: .north
			}

			nextPosition = point.move(dir)
		}

		point = nextPosition
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let oGrid = mapGridToPoints(input.characterGrid())
//		print(oGrid.count)

		let startPosition = oGrid.first { $0.value.isGuard }!.key
		var count = 0

		for (newObstruction, existing) in oGrid where newObstruction != startPosition && !existing.isObstruction {
			var grid = oGrid
			grid[newObstruction] = "#"

			var facing = Direction.north
			var position = startPosition
			var visited: Set<State> = []

			while grid[position] != nil {
				guard visited.insert(State(position: position, direction: facing)).inserted else {
//					print(newObstruction, position, facing)
					count += 1
					break
				}

				moveGuard(&position, dir: &facing, in: grid)
			}
		}

		return count.description
	}

	struct State: Hashable {
		let position: Point2
		let direction: Direction
	}
}

extension Character {
	var isGuard: Bool { self == "^" }
	var isObstruction: Bool { self == "#" }
}
