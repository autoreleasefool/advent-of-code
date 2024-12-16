import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day16: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: """
//###############
//#.......#....E#
//#.#.###.#.###.#
//#.....#.#...#.#
//#.###.#####.#.#
//#.#.#.......#.#
//#.#.#####.###.#
//#...........#.#
//###.#.#####.#.#
//#...#.....#.#.#
//#.#.#.###.#.#.#
//#.....#...#.#.#
//#.###.#.#.#.#.#
//#S..#.....#...#
//###############
//""")
	}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let grid = mapGridToPoints(input.characterGrid())

		let start = grid.first { $0.value == "S" }!.key
		let initialState = State(position: start)
		var queue: [(State, Int)] = [(initialState, 0)]
//		var visited: Set<State> = []
		var prev: [State: State] = [:]
		var minStateScore: [State: Int] = [:]

		var minScore = Int.max
		var minState: State?
		while let (next, score) = queue.popFirst() {
			guard minStateScore[next] == nil || score < minStateScore[next]!,
						score < minScore
			else { continue }

			minStateScore[next] = score

			if grid[next.position] == "E" {
				if score < minScore {
					minScore = score
					minState = next
				}
				continue
			}

//			visited.insert(next)

			for direction in [next.direction.turnRight, next.direction.turnLeft] {
				var updated = next
				updated.direction = direction
				prev[updated] = next
				queue.append((updated, score + 1000))
			}

			var updated = next
			updated.position = updated.position.move(updated.direction)
			if grid[updated.position] != "#" {
				prev[updated] = next
				queue.append((updated, score + 1))
			}

//			for adjacent in next.position.adjacentPoints() where grid[adjacent] != "#" {
//				var updated = next
//				updated.position = adjacent
//				updated.score += 1
//				prev[updated] = next
//				queue.append(updated)
//			}
		}

//		while minState != nil {
//			print(minState)
//			minState = prev[minState!]
//		}

		return minScore.description
	}

	struct State: Hashable {
		var position: Point2
		var direction: Direction = .east
//		var score: Int = 0
	}

	private var grid: [Point2: Character] = [:]

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		grid = mapGridToPoints(input.characterGrid())

		let start = grid.first { $0.value == "S" }!.key
		let initialState = State(position: start)
		var queue: [(State, Int)] = [(initialState, 0)]
		var prev: [State: State] = [:]
		var minStateScore: [State: Int] = [:]

		var minScore = Int.max
		var minState: State?
		while let (next, score) = queue.popFirst() {
			guard minStateScore[next] == nil || score < minStateScore[next]!,
						score <= minScore
			else { continue }

			minStateScore[next] = score

			if grid[next.position] == "E" {
				if score < minScore {
					minScore = score
					minState = next
				}
				continue
			}

			for direction in [next.direction.turnRight, next.direction.turnLeft] {
				var updated = next
				updated.direction = direction
				prev[updated] = next
				queue.append((updated, score + 1000))
			}

			var updated = next
			updated.position = updated.position.move(updated.direction)
			if grid[updated.position] != "#" {
				prev[updated] = next
				queue.append((updated, score + 1))
			}

		}


//		let start = grid.first { $0.value == "S" }!.key
//		let initialState = State(position: start)
		queue = [(initialState, 0)]
		var paths: [UUID: [[State]]] = [:]
//		var visited: Set<State> = []
//		prev: [State: State] = [:]
//		var minStateScore: [State: Int] = [:]

//		var paths: [[State]] = []
		while let (next, score) = queue.popFirst() {
			guard score <= minScore else { return nil }
			guard minScoreAtState[next] == nil || score <= minScoreAtState[next]! else { return nil }

			//		var visited = v
			//		visited.insert(state)
			if grid[next.position] == "E" {

				return [[]]
			}

			var allSubpaths: [[State]] = []

			var subState1 = state
			subState1.direction = state.direction.turnRight
			let subPaths1 = traverse(from: subState1, score: score + 1000,  maxScore: maxScore)
			if let subPaths1 {
				minScoreAtState[state] = score
				allSubpaths.append(contentsOf: subPaths1.map { [state] + $0 })
			}

			var subState2 = state
			subState2.direction = state.direction.turnLeft
			let subPaths2 = traverse(from: subState2, score: score + 1000, maxScore: maxScore)
			if let subPaths2 {
				minScoreAtState[state] = score
				allSubpaths.append(contentsOf: subPaths2.map { [state] + $0 })
			}

			var subState3 = state
			subState3.position = state.position.move(state.direction)
			if grid[subState3.position] != "#" {
				let subPaths3 = traverse(from: subState3, score: score + 1, maxScore: maxScore)
				if let subPaths3 {
					minScoreAtState[state] = score
					allSubpaths.append(contentsOf: subPaths3.map { [state] + $0 })
				}
			}
		}

		return allSubpaths













//		var visited: Set<State> = []
//		let paths = traverse(from: initialState, score: 0, maxScore: minScore)
//		print(paths?.count)
//
//		let allPoints = Set(paths!.flatMap { $0.map { $0.position } })
//		print(allPoints.count)

		return minScore.description
	}

	private var minScoreAtState: [State: Int] = [:]

//	private func traverse(from state: State, score: Int, maxScore: Int) -> [[State]]? {
////		guard !v.contains(state) else { return nil }
//		guard score <= maxScore else { return nil }
//		guard minScoreAtState[state] == nil || score < minScoreAtState[state]! else { return nil }
//
////		var visited = v
////		visited.insert(state)
//		if grid[state.position] == "E" {
//			return [[state]]
//		}
//
//		var allSubpaths: [[State]] = []
//
//		var subState1 = state
//		subState1.direction = state.direction.turnRight
//		let subPaths1 = traverse(from: subState1, score: score + 1000,  maxScore: maxScore)
//		if let subPaths1 {
//			minScoreAtState[state] = score
//			allSubpaths.append(contentsOf: subPaths1.map { [state] + $0 })
//		}
//
//		var subState2 = state
//		subState2.direction = state.direction.turnLeft
//		let subPaths2 = traverse(from: subState2, score: score + 1000, maxScore: maxScore)
//		if let subPaths2 {
//			minScoreAtState[state] = score
//			allSubpaths.append(contentsOf: subPaths2.map { [state] + $0 })
//		}
//
//		var subState3 = state
//		subState3.position = state.position.move(state.direction)
//		if grid[subState3.position] != "#" {
//			let subPaths3 = traverse(from: subState3, score: score + 1, maxScore: maxScore)
//			if let subPaths3 {
//				minScoreAtState[state] = score
//				allSubpaths.append(contentsOf: subPaths3.map { [state] + $0 })
//			}
//		}
//
//		return allSubpaths
//	}
}
