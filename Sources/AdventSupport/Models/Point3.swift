import Algorithms
import Foundation

public struct Point3: Hashable, Sendable {
	public var x: Int
	public var y: Int
	public var z: Int

	public init(x: Int, y: Int, z: Int) {
		self.x = x
		self.y = y
		self.z = z
	}

	public init(_ x: Int, _ y: Int, _ z: Int) {
		self.x = x
		self.y = y
		self.z = z
	}

	public init(_ point: Point2, z: Int = 0) {
		self.x = point.x
		self.y = point.y
		self.z = z
	}

	public init(_ point: Point3) {
		self.x = point.x
		self.y = point.y
		self.z = point.z
	}

	// MARK: Constants

	public static let zero = Point3(0, 0, 0)
}

// MARK: Adjacent Points

extension Point3 {
	public func adjacentPoints(includingDiagonals: Bool = false, includingSelf: Bool = false) -> [Point3] {
		product(-1...1, product(-1...1, -1...1))
			.map { x, yz in (x: x, y: yz.0, z: yz.1) }
			.filter { includingDiagonals || ($0.x + $0.y + $0.z == 1) }
			.filter { includingSelf || !($0.x == 0 && $0.y == 0 && $0.z == 0) }
			.map { self + Point3($0.x, $0.y, $0.z) }
	}
}

// MARK: Comparable

extension Point3: Comparable {
	public static func < (lhs: Point3, rhs: Point3) -> Bool {
		lhs.x == rhs.x ? lhs.y == rhs.y ? lhs.z < rhs.z : lhs.y < rhs.y : lhs.x < rhs.x
	}
}

// MARK: Operations

extension Point3 {
	public static func + (lhs: Point3, rhs: Point3) -> Point3 {
		Point3(lhs.x + rhs.x, lhs.y + rhs.y, lhs.z + rhs.z)
	}

	public static func += (lhs: inout Point3, rhs: Point3) {
		lhs = lhs + rhs
	}

	public static func - (lhs: Point3, rhs: Point3) -> Point3 {
		Point3(lhs.x - rhs.x, lhs.y - rhs.y, lhs.z - rhs.z)
	}

	public static func -= (lhs: inout Point3, rhs: Point3) {
		lhs = lhs - rhs
	}

	public static func * (lhs: Point3, rhs: Int) -> Point3 {
		Point3(lhs.x * rhs, lhs.y * rhs, lhs.z * rhs)
	}

	public static func *= (lhs: inout Point3, rhs: Int) {
		lhs = lhs * rhs
	}
}

// MARK: Debug

extension Point3: CustomDebugStringConvertible {
	public var debugDescription: String {
		"(\(x),\(y),\(z))"
	}
}
