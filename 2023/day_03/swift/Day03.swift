import AdventSupport
import Foundation

public class Year2023Day03: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
		self.grid = input.characterGrid()
	}

	private var grid: [[Character]]!

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		schematicValues()
			.map { pointsForSchemaValue($0.value, startPoint: $0.key) }
			.filter { (points, _) in isPartNumber(points) }
			.map { $0.partNumber }
			.reduce(0, +)
			.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let gears = grid
			.enumerated()
			.flatMap { (y, row) in
				row
					.enumerated()
					.filter { $0.element == "*" }
					.map { (x, value) in Point2(x: x, y: y) }
			}
			.toSet()

		let gearParts = schematicValues()
			.map { pointsForSchemaValue($0.value, startPoint: $0.key) }
			.reduce(into: [:]) { gearParts, schemaValue in
				neighbours(to: schemaValue.points)
					.forEach { gearParts[$0, default: []].append(schemaValue.partNumber) }
			}

		return gearParts
			.filter { gears.contains($0.key) }
			.filter { $0.value.count == 2 }
			.map { $0.value.reduce(1, *) }
			.reduce(0, +)
			.description
	}

	// MARK: Helpers

	private func pointsForSchemaValue(_ value: Int, startPoint: Point2) -> (points: [Point2], partNumber: Int) {
		(
			points: (startPoint.x..<(startPoint.x + value.size)).map { Point2(x: $0, y: startPoint.y) },
			partNumber: value
		)
	}

	private func neighbours(to points: [Point2]) -> Set<Point2> {
		points.flatMap { $0.adjacentPoints(includingDiagonals: true) }
			.toSet()
			.subtracting(points)
	}

	private func isPartNumber(_ points: [Point2]) -> Bool {
		neighbours(to: points)
			.compactMap { grid[$0] }
			.contains { $0 != "." && !$0.isNumber }
	}

	private func schematicValues() -> [Point2: Int] {
		var schematicValues: [Point2: Int] = [:]

		for (y, row) in grid.enumerated() {
			var start = row.startIndex
			while start < row.endIndex {
				guard row[start].isNumber else {
					start = row.index(after: start)
					continue
				}

				var end = row.index(after: start)
				while end < row.endIndex && row[end].isNumber {
					end = row.index(after: end)
				}

				let startPoint = Point2(
					x: row.distance(from: row.startIndex, to: start),
					y: y
				)

				schematicValues[startPoint] = Int(String(row[start..<end]))!

				start = row.index(after: end)
			}
		}

		return schematicValues
	}
}
