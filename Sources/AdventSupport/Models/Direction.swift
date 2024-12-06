import Algorithms
import Collections
import Foundation

public enum Direction: Hashable, Sendable, CaseIterable, Comparable {
	case north
	case east
	case south
	case west
}

// MARK: Adjacencies

extension Direction {
	public var turnRight: Direction {
		switch self {
		case .north: .east
		case .east: .south
		case .south: .west
		case .west: .north
		}
	}

	public var turnLeft: Direction {
		switch self {
		case .north: .west
		case .west: .south
		case .south: .east
		case .east: .north
		}
	}
}

// MARK: Point

extension Direction {
	public var point: Point2 {
		switch self {
		case .north: Point2(0, -1)
		case .south: Point2(0, 1)
		case .west: Point2(-1, 0)
		case .east: Point2(1, 0)
		}
	}
}

// MARK: - CompoundDirection

public struct CompoundDirection: Hashable, Sendable, CaseIterable {
	public let directions: [Direction]

	public static var allCases: [CompoundDirection] {
		(Direction.allCases + Direction.allCases + [nil])
			.combinations(ofCount: 2)
			.map { $0.compacted() }
			.reduce(into: Set<Set<Direction>>()) { $0.insert(Set($1)) }
			.map { CompoundDirection(directions: Array($0)) }
	}

	public static var north: CompoundDirection { CompoundDirection(directions: [.north]) }
	public static var south: CompoundDirection { CompoundDirection(directions: [.south]) }
	public static var east: CompoundDirection { CompoundDirection(directions: [.east]) }
	public static var west: CompoundDirection { CompoundDirection(directions: [.west]) }
	public static var northEast: CompoundDirection { CompoundDirection(directions: [.north, .east]) }
	public static var northWest: CompoundDirection { CompoundDirection(directions: [.north, .west]) }
	public static var southEast: CompoundDirection { CompoundDirection(directions: [.south, .east]) }
	public static var southWest: CompoundDirection { CompoundDirection(directions: [.south, .west]) }
}

// MARK: Point

extension CompoundDirection {
	public var point: Point2 {
		directions.map(\.point).reduce(Point2.zero, +)
	}
}
