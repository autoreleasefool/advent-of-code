import AdventSupport
import Foundation

public class Year2024Day15: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: """
//##########
//#..O..O.O#
//#......O.#
//#.OO..O.O#
//#..O@..O.#
//#O#..O...#
//#O..O..O.#
//#.OO.O.OO#
//#....O...#
//##########
//
//<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
//vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
//><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
//<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
//^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
//^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
//>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
//<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
//^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
//v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
//""")
//		input = Input(contents: """
//########
//#..O.O.#
//##@.O..#
//#...O..#
//#.#.O..#
//#...O..#
//#......#
//########
//
//<^^>>>vv<v>>v<<
//""")
//		input = Input(contents: """
//#######
//#...#.#
//#.....#
//#..OO@#
//#..O..#
//#.....#
//#######
//
//<vv<<^^<<^^
//""")
	}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let splits = input.contents.split(separator: "\n\n")
		var grid = mapGridToPoints(String(splits[0]).components(separatedBy: .newlines).map { Array($0) })
		let commands = String(splits[1])
//		print(commands)

		for command in commands {
			var robot = grid.first { $0.value == "@" }!.key
//			print(command, robot)

			var velocity: Point2 = .zero
			switch command {
			case "<": velocity = .init(x: -1, y: 0)
			case "^": velocity = .init(x: 0, y: -1)
			case ">": velocity = .init(x: 1, y: 0)
			case "v": velocity = .init(x: 0, y: 1)
			default: continue
			}

			guard velocity != .zero else { continue }

			var next = robot + velocity
			while true {
				if grid[next] == "#" {
//					print("break")
					break
				} else if grid[next] == "." {
//					print("space found")
					let negativeVelocity = velocity * -1
					var prev = next
					next = next + negativeVelocity

					while prev != robot {
						grid[prev] = grid[next]
						prev = next
						next = next + negativeVelocity
					}
					grid[robot] = "."
					break
				} else {
					next = next + velocity
//					print("next")
				}
			}
//			printGrid(grid)
		}

		var total = 0
		for (p, v) in grid {
			if v == "O" {
				total += p.y * 100 + p.x
			}
		}

		return total.description
	}

	private func printGrid(_ grid: [Point2: Character]) {
		for y in 0...grid.keys.max(by: { $0.y < $1.y })!.y {
			for x in 0...grid.keys.max(by: { $0.x < $1.x })!.x {
				print(grid[Point2(x, y)] ?? " ", terminator: "")
			}

			print()
		}
	}

	// MARK: Part 2

	private var grid: [Point2: Character]!

	public func solvePart2(_ input: Input) async throws -> String? {
		let splits = input.contents.split(separator: "\n\n")
		grid = mapGridToPoints(String(splits[0]).components(separatedBy: .newlines).map { Array($0) })

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

		printGrid(grid)

		let commands = String(splits[1])
//		print(commands)

		for command in commands {
			var robot = grid.first { $0.value == "@" }!.key
//			print(command, robot)

			let direction: Direction
			switch command {
			case "<": direction = .west
			case "^": direction = .north
			case ">": direction = .east
			case "v": direction = .south
			default: continue
			}

//			let oppositeDirection = direction.turnRight.turnRight

			if let objectsMoved = self.objectsMoved(from: robot, direction: direction) {
				for object in objectsMoved + [robot] {
					grid[object + direction.point] = grid[object]
					grid[object] = "."
				}
			}

//			printGrid(grid)
		}



		var total = 0
		for (p, v) in grid {
			if v == "[" {
				total += p.y * 100 + p.x
			}
		}

		return total.description
	}

	private func objectsMoved(from: Point2, direction: Direction) -> [Point2]? {
//		var objects = [Point2]()
//		print("Moving from", from, "in direction", direction, "to", from + direction.point)
		var next = from + direction.point
		switch grid[next] {
		case "#":
			return nil
		case ".":
			return []
		case "[", "]":
			switch direction {
			case .east, .west:
				if let moreObjects = objectsMoved(from: next, direction: direction) {
					return moreObjects + [next]
				} else {
					return nil
				}
			case .north, .south:
				let primarySetMoved = objectsMoved(from: next, direction: direction)
				let otherPosition = next + (grid[next] == "[" ? Direction.east.point : Direction.west.point)
//				print(next, otherPosition, grid[next] == "[" ? Direction.east.point : Direction.west.point, Direction.west.point)
				let secondarySetMoved = objectsMoved(from: otherPosition, direction: direction)
				if let primarySetMoved, let secondarySetMoved {
//					print(primarySetMoved, secondarySetMoved, [next])
					return Array((primarySetMoved + secondarySetMoved + [next, otherPosition]).uniqued())
				} else {
					return nil
				}
			}
		default:
			return []
		}
	}
}
