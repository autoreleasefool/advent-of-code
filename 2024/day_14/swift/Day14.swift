import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day14: Solver {
	public required init() {}

	// MARK: Part 1

	private let maxX = 101
	private let maxY = 103

	public func solvePart1(_ input: Input) async throws -> String? {
		var robots = getStartingRobots(from: input)

		for _ in 0..<100 {
			for i in robots.indices {
				robots[i].updatePosition(maxX: maxX, maxY: maxY)
			}
		}

		return safetyFactor(robots).description
	}

	private func buildQuadrant(xRange: ClosedRange<Int>, yRange: ClosedRange<Int>) -> Set<Point2> {
		product(xRange, yRange)
			.map { Point2($0, $1) }
			.toSet()
	}

	private func safetyFactor(_ robots: [Robot]) -> Int {
		let q1 = buildQuadrant(xRange: 0...maxX / 2 - 1, yRange: 0...maxY / 2 - 1)
		let q2 = buildQuadrant(xRange: maxX / 2 + 1...maxX, yRange: 0...maxY / 2 - 1)
		let q3 = buildQuadrant(xRange: 0...maxX / 2 - 1, yRange: maxY / 2 + 1...maxY)
		let q4 = buildQuadrant(xRange: maxX / 2 + 1...maxX, yRange: maxY / 2 + 1...maxY)

		let q1Count = robots.count(where: { q1.contains($0.position) })
		let q2Count = robots.count(where: { q2.contains($0.position) })
		let q3Count = robots.count(where: { q3.contains($0.position) })
		let q4Count = robots.count(where: { q4.contains($0.position) })

		return q1Count * q2Count * q3Count * q4Count
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		var robots = getStartingRobots(from: input)
		let expectedOutput = "*....***********************....*".map { $0 == "*" }

		return (1...100_000)
			.first { _ in
				for i in robots.indices {
					robots[i].updatePosition(maxX: maxX, maxY: maxY)
				}

				let robotPositions = robots.map(\.position).toSet()

				return (0...maxX).contains { x in
					let robotsInRow = (0...maxY).count { y in robotPositions.contains(Point2(x, y)) }
					guard robotsInRow > 20 else { return false }

					return (0...maxY)
						.map { y in robotPositions.contains(Point2(x, y)) }
						.contains(expectedOutput)
				}
			}?
			.description
	}

	// MARK: Helpers

	private func getStartingRobots(from input: Input) -> [Robot] {
		input
			.integersByLine()
			.filter { $0.count >= 4 }
			.map { Robot(position: Point2($0[0], $0[1]), velocity: Point2($0[2], $0[3])) }
	}
}

struct Robot {
	var position: Point2
	var velocity: Point2

	mutating func updatePosition(maxX: Int, maxY: Int) {
		position += velocity
		position = Point2(mod(position.x, maxX), mod(position.y, maxY))
	}
}
