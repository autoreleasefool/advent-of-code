import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day20: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: """
//###############
//#...#...#.....#
//#.#.#.#.#.###.#
//#S#...#.#.#...#
//#######.#.#.###
//#######.#.#...#
//#######.#.###.#
//###..E#...#...#
//###.#######.###
//#...###...#...#
//#.#####.#.###.#
//#.#...#.#.#...#
//#.#.#.#.#.#.###
//#...#...#...###
//###############
//""")
}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let grid = mapGridToPoints(input.characterGrid())
		let start = grid.first { $0.value == "S" }!.key
		let end = grid.first { $0.value == "E" }!.key

		let initialState = State(position: start)
		let maxTimePath = depthFirstSearch(
			start: start,
			goal: end,
			graph: grid,
			adjacent: { $0.adjacentPoints().filter { grid[$0] != "#" } }
		)!
		let maxTime = maxTimePath.count

		var remainingTimeToEnd: [Point2: Int] = [:]

//		var minDist: [Point2: Int] = [:]
		for (i, p) in maxTimePath.enumerated() {
			remainingTimeToEnd[p] = maxTime - i
//			minDist[p] = i
		}
//		print(minDist)

		var count = 0
		for (i, p) in maxTimePath.enumerated() {
			for adj in p.adjacentPoints() where grid[adj] == "#" {
				for exit in adj.adjacentPoints() where grid[exit] == "." || grid[exit] == "E" {
					let timeTaken = i + 2
					let remaining = remainingTimeToEnd[exit]!
					let totalTime = timeTaken + remaining
					if totalTime + 100 <= maxTime {
//					print(adj, exit, timeTaken, remainingTimeToEnd[exit]!)
//					if timeTaken + 64 < remainingTimeToEnd[exit]! {

						count += 1
					}
				}
			}
		}
		return count.description


//		var count = 0
//		var counts: [Int: Int] = [:]
//		var visited: Set<State> = []
//
//		var queue = [(initialState, 0)]
//		while let (state, distance) = queue.popLast() {
////			print(state.position, state.distance)
//			guard distance <= defaultTimeToEnd[state.position]! else { continue }
////			guard minDist[state.position] == nil || state.distance <= minDist[state.position]! else { continue }
//			guard visited.insert(state).inserted else { continue }
//
////			if minDist[state.position] == nil {
////				minDist[state.position] = state.distance
////			}
//
//			if state.position == end {
//				counts[maxTime - state.distance, default: 0] += 1
//				if maxTime - state.distance >= 100 {
//					count += 1
//				}
//				continue
//			}
//
//			for adj in state.position.adjacentPoints() {
//				if grid[adj] == "#" && state.cheats.count < 1 {
//					for exit in adj.adjacentPoints() where ["#", "E"].contains(grid[exit]) && exit != state.position {
//						var copy = state
//						copy.position = exit
//						copy.cheats.append([adj, exit])
//						copy.distance += 2
//						queue.append(copy)
//					}
//				} else if grid[adj] != nil {
//					var copy = state
//					copy.position = adj
//					copy.distance += 1
//					queue.append(copy)
//				}
//			}
//		}
//		print(counts)
//
//		return count.description
	}

	struct State: Hashable {
		var position: Point2
		var cheats: [[Point2]] = []
//		var path: [Point2] = []
//		var cheats = 2
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let grid = mapGridToPoints(input.characterGrid())
		let start = grid.first { $0.value == "S" }!.key
		let end = grid.first { $0.value == "E" }!.key

		let initialState = State(position: start)
		let maxTimePath = depthFirstSearch(
			start: start,
			goal: end,
			graph: grid,
			adjacent: { $0.adjacentPoints().filter { grid[$0] != "#" } }
		)!
		let maxTime = maxTimePath.count

		var remainingTimeToEnd: [Point2: Int] = [:]

//		var minDist: [Point2: Int] = [:]
		for (i, p) in maxTimePath.enumerated() {
			remainingTimeToEnd[p] = maxTime - i
//			minDist[p] = i
		}
//		print(minDist)

		var count = 0
		for (i, p) in maxTimePath.enumerated() {
			for adj in p.adjacentPoints() where grid[adj] == "#" {
				for exit in adj.adjacentPoints() where grid[exit] == "." || grid[exit] == "E" {
					let timeTaken = i + 2
					let remaining = remainingTimeToEnd[exit]!
					let totalTime = timeTaken + remaining
					if totalTime + 100 <= maxTime {
//					print(adj, exit, timeTaken, remainingTimeToEnd[exit]!)
//					if timeTaken + 64 < remainingTimeToEnd[exit]! {

						count += 1
					}
				}
			}
		}
		return count.description
	}
}
