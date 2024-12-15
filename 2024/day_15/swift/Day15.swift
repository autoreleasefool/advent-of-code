import AdventSupport
import Foundation

public class Year2024Day15: Solver {
	public required init() {}

	// MARK: Part 1

	private var grid = [Point2: Character]()

	public func solvePart1(_ input: Input) async throws -> String? {
		let splits = input.contents.split(separator: "\n\n")
		grid = mapGridToPoints(String(splits[0]).components(separatedBy: .newlines).map { Array($0) })
		let commands = String(splits[1])

		var robot = grid.first { $0.value == "@" }!.key
		for command in commands {


			let direction: Direction
			switch command {
			case "<": direction = .west
			case "^": direction = .north
			case ">": direction = .east
			case "v": direction = .south
			default: continue
			}

			if let objectsMoved = p1ObjectsMoved(from: robot, direction: direction) {
				for object in objectsMoved + [robot] {
					grid[object + direction.point] = grid[object]
					grid[object] = "."
				}

				robot += direction.point
			}
		}

		return calculateTotalBoxScore().description
	}

	private func p1ObjectsMoved(from: Point2, direction: Direction) -> [Point2]? {
		let next = from + direction.point
		switch grid[next] {
		case "#":
			return nil
		case ".":
			return []
		case "O":
			if let moreObjects = p1ObjectsMoved(from: next, direction: direction) {
				return moreObjects + [next]
			} else {
				return nil
			}
		default:
			return []
		}
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let splits = input.contents.split(separator: "\n\n")
		grid = mapGridToPoints(String(splits[0]).components(separatedBy: .newlines).map { Array($0) })
		let commands = String(splits[1])

		for y in 0...grid.keys.max(by: { $0.y < $1.y })!.y {
			for x in (0...grid.keys.max(by: { $0.x < $1.x })!.x).reversed() {
				switch grid[Point2(x, y)] {
				case "#", ".":
					grid[Point2(2 * x, y)] = grid[Point2(x, y)]
					grid[Point2(2 * x + 1, y)] = grid[Point2(x, y)]
				case "O":
					grid[Point2(2 * x, y)] = "["
					grid[Point2(2 * x + 1, y)] = "]"
				case "@":
					grid[Point2(2 * x, y)] = "@"
					grid[Point2(2 * x + 1, y)] = "."
				default:
					continue
				}
			}
		}

		var robot = grid.first { $0.value == "@" }!.key
		for command in commands {
			let direction: Direction
			switch command {
			case "<": direction = .west
			case "^": direction = .north
			case ">": direction = .east
			case "v": direction = .south
			default: continue
			}

			if let objectsMoved = self.p2ObjectsMoved(from: robot, direction: direction) {
				for object in objectsMoved + [robot] {
					grid[object + direction.point] = grid[object]
					grid[object] = "."
				}

				robot += direction.point
			}
		}

		return calculateTotalBoxScore().description
	}

	private func p2ObjectsMoved(from: Point2, direction: Direction) -> [Point2]? {
		var next = from + direction.point
		switch grid[next] {
		case "#":
			return nil
		case ".":
			return []
		case "[", "]":
			switch direction {
			case .east, .west:
				if let moreObjects = p2ObjectsMoved(from: next, direction: direction) {
					return moreObjects + [next]
				} else {
					return nil
				}
			case .north, .south:
				let primarySetMoved = p2ObjectsMoved(from: next, direction: direction)
				let otherPosition = next + (grid[next] == "[" ? Direction.east.point : Direction.west.point)
				let secondarySetMoved = p2ObjectsMoved(from: otherPosition, direction: direction)
				if let primarySetMoved, let secondarySetMoved {
					return Array((primarySetMoved + secondarySetMoved + [next, otherPosition]).uniqued())
				} else {
					return nil
				}
			}
		default:
			return []
		}
	}

	// MARK: Helpes

	private func calculateTotalBoxScore() -> Int {
		grid
			.filter { $0.value == "O" || $0.value == "[" }
			.reduce(0) { $0 + $1.key.y * 100 + $1.key.x }
	}
}
