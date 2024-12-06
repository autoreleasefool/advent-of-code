import AdventSupport
import Foundation

public class Year2024Day06: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
		self.grid = mapGridToPoints(input.characterGrid())
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

	private var grid: [Point2: Character]!

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		var guardFacing: Direction = .north
		var guardPosition = grid.first { $0.value == "^" }!.key
		var visitedPositions: Set<Point2> = []

		while grid[guardPosition] != nil {
			visitedPositions.insert(guardPosition)
			moveGuard(from: &guardPosition, towards: &guardFacing)
		}

		return visitedPositions.count.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let startingGrid = grid!
		var positionsForObstructions = 0
		let startingGuardPosition = grid.first { $0.value == "^" }!.key

		for (newObstruction, existingValue) in startingGrid where newObstruction != startingGuardPosition && existingValue != "#" {
			grid = startingGrid
			grid[newObstruction] = "#"

			var guardFacing: Direction = .north
			var guardPosition = startingGuardPosition
			var visitedStates: Set<GuardState> = []

			while grid[guardPosition] != nil {
				let newState = GuardState(position: guardPosition, direction: guardFacing)
				guard visitedStates.insert(newState).inserted else {
					// We have entered a loop
					positionsForObstructions += 1
					break
				}

				moveGuard(from: &guardPosition, towards: &guardFacing)
			}
		}

		return positionsForObstructions.description
	}

	// MARK: Helpers

	private func moveGuard(from guardPosition: inout Point2, towards: inout Direction) {
		var nextPosition = guardPosition.move(towards)
		while grid[nextPosition] == "#" {
			towards = towards.turnRight
			nextPosition = guardPosition.move(towards)
		}
		guardPosition = nextPosition
	}

	struct GuardState: Hashable {
		let position: Point2
		let direction: Direction
	}
}
