import AdventSupport
import Foundation

public class Year2024Day08: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let grid = mapGridToPoints(input.characterGrid())

		var antinodes: Set<Point2> = []
		var nodes: [Character: Set<Point2>] = [:]

		for (point, value) in grid where value != "." {
			nodes[value, default: []].insert(point)
		}

		for (antenna, points) in nodes {
			for pointA in points {
				for pointB in points where pointA != pointB {
					let dx = pointA.x - pointB.x
					let dy = pointA.y - pointB.y

					let firstAntinode = Point2(x: pointA.x + dx, y: pointA.y + dy)
					let secondAntinode = Point2(x: pointB.x - dx, y: pointB.y - dy)
					let thirdAntinode = Point2(x: pointB.x + dx, y: pointB.y + dy)
					let fourthAntinode = Point2(x: pointB.x - dx, y: pointB.y - dy)

					if firstAntinode != pointA && firstAntinode != pointB {
						antinodes.insert(firstAntinode)
					}

					if secondAntinode != pointA && secondAntinode != pointB {
						antinodes.insert(secondAntinode)
					}

					if thirdAntinode != pointA && thirdAntinode != pointB {
						antinodes.insert(thirdAntinode)
					}

					if fourthAntinode != pointA && fourthAntinode != pointB {
						antinodes.insert(fourthAntinode)
					}
				}
			}
		}

		return antinodes.intersection(grid.keys).count.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let grid = mapGridToPoints(input.characterGrid())

		var antinodes: Set<Point2> = []
		var nodes: [Character: Set<Point2>] = [:]

		for (point, value) in grid where value != "." {
			nodes[value, default: []].insert(point)
		}

		for (antenna, points) in nodes {
			for pointA in points {
				for pointB in points where pointA != pointB {
					let dx = pointA.x - pointB.x
					let dy = pointA.y - pointB.y
					let delta = Point2(dx, dy)

					var increasingPoint = pointA
					while grid[increasingPoint] != nil {
						increasingPoint += delta
						antinodes.insert(increasingPoint)
					}

					var decreasingPoint = pointA
					while grid[decreasingPoint] != nil {
						decreasingPoint -= delta
						antinodes.insert(decreasingPoint)
					}
				}
			}
		}

		return antinodes.intersection(grid.keys).count.description
	}
}
