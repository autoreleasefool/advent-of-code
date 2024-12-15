import Algorithms
import Foundation

public struct Point2: Hashable, Sendable {
	public var x: Int
	public var y: Int

	public init(x: Int, y: Int) {
		self.x = x
		self.y = y
	}

	public init(_ x: Int, _ y: Int) {
		self.x = x
		self.y = y
	}

	public init(_ point: Point2) {
		self.x = point.x
		self.y = point.y
	}

	// MARK: Constants

	public static let zero = Point2(x: 0, y: 0)
}

// MARK: Adjacent Points

extension Point2 {
	public func adjacentPoints(includingDiagonals: Bool = false, includingSelf: Bool = false) -> [Point2] {
		product(-1...1, -1...1)
			.filter { includingDiagonals || $0.0 == 0 || $0.1 == 0 }
			.filter { includingSelf || !($0.0 == 0 && $0.1 == 0) }
			.map { Point2(x: x + $0.0, y: y + $0.1) }
	}
}

// MARK: Directions

extension Point2 {
	public mutating func moveUp() {
		y -= 1
	}

	public mutating func moveDown() {
		y += 1
	}

	public mutating func moveLeft() {
		x -= 1
	}

	public mutating func moveRight() {
		x += 1
	}

	public mutating func moveNorth() { moveUp() }
	public mutating func moveSouth() { moveDown() }
	public mutating func moveWest() { moveLeft() }
	public mutating func moveEast() { moveRight() }

	public var up: Point2 {
		var point2 = self
		point2.moveUp()
		return point2
	}

	public var down: Point2 {
		var point2 = self
		point2.moveDown()
		return point2
	}

	public var left: Point2 {
		var point2 = self
		point2.moveLeft()
		return point2
	}

	public var right: Point2 {
		var point2 = self
		point2.moveRight()
		return point2
	}

	public var north: Point2 { up }
	public var south: Point2 { down }
	public var west: Point2 { left }
	public var east: Point2 { right }

	public func move(_ direction: Direction) -> Point2 {
		switch direction {
		case .north: north
		case .south: south
		case .east: east
		case .west: west
		}
	}
}

// MARK: Comparable

extension Point2: Comparable {
	public static func < (lhs: Point2, rhs: Point2) -> Bool {
		lhs.x == rhs.x ? lhs.y < rhs.y : lhs.x < rhs.x
	}
}

// MARK: Operations

extension Point2 {
	public static func + (lhs: Point2, rhs: Point2) -> Point2 {
		Point2(x: lhs.x + rhs.x, y: lhs.y + rhs.y)
	}

	public static func += (lhs: inout Point2, rhs: Point2) {
		lhs = lhs + rhs
	}

	public static func - (lhs: Point2, rhs: Point2) -> Point2 {
		Point2(x: lhs.x - rhs.x, y: lhs.y - rhs.y)
	}

	public static func -= (lhs: inout Point2, rhs: Point2) {
		lhs = lhs - rhs
	}

	public static func * (lhs: Point2, rhs: Int) -> Point2 {
		Point2(x: lhs.x * rhs, y: lhs.y * rhs)
	}

	public static func *= (lhs: inout Point2, rhs: Int) {
		lhs = lhs * rhs
	}
}

// MARK: Map

public func mapGridToPoints<T>(_ grid: [[T]]) -> [Point2: T] {
	grid.enumerated().reduce(into: [:]) { grid, row in
		row.element.enumerated().forEach { grid[Point2(x: $0.0, y: row.offset)] = $0.element }
	}
}

public func printGrid<T>(_ grid: [Point2: T]) {
	for y in 0...grid.keys.max(by: { $0.y < $1.y })!.y {
		for x in 0...grid.keys.max(by: { $0.x < $1.x })!.x {
			print(grid[Point2(x, y)] ?? " ", terminator: "")
		}

		print()
	}
}

extension Array {
	public subscript<T>(_ point: Point2) -> T? where Element == [T] {
		guard point.y >= 0, point.y < count else { return nil }
		guard point.x >= 0, point.x < self[point.y].count else { return nil }
		return self[point.y][point.x]
	}
}

// MARK: Debug

extension Point2: CustomDebugStringConvertible {
	public var debugDescription: String {
		"(\(x), \(y))"
	}
}
