import AdventSupport
import Foundation

public class Year2016Day17: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let passcode = input.contents

		var queue: [(Point2, [Direction])] = [(Point2(0, 0), [])]

		while !queue.isEmpty {
			let (position, path) = queue.removeFirst()

			if position == Point2(3, 3) {
				return path.map(\.value).joined()
			}

			for (direction, isOpen) in findDoorState(passcode: passcode, path: path) where isOpen {
				let newPosition = position + direction.point
				guard newPosition.x >= 0, newPosition.y >= 0, newPosition.x < 4, newPosition.y < 4 else {
					continue
				}

				queue.append((newPosition, path + [direction]))
			}
		}

		return nil
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let passcode = input.contents

		var queue: [(Point2, [Direction])] = [(Point2(0, 0), [])]
		var longestPath = 0

		while !queue.isEmpty {
			let (position, path) = queue.removeFirst()

			if position == Point2(3, 3) {
				longestPath = max(longestPath, path.count)
				continue
			}

			for (direction, isOpen) in findDoorState(passcode: passcode, path: path) where isOpen {
				let newPosition = position + direction.point
				guard newPosition.x >= 0, newPosition.y >= 0, newPosition.x < 4, newPosition.y < 4 else {
					continue
				}

				queue.append((newPosition, path + [direction]))
			}
		}

		return longestPath.description
	}

	// MARK: Helpers

	private func findDoorState(passcode: String, path: [Direction]) -> [Direction: Bool] {
		let path = path.map(\.value).joined()
		let hash = "\(passcode)\(path)".md5
		return [
			.north: "bcdef".contains(hash[0]),
			.south: "bcdef".contains(hash[1]),
			.west: "bcdef".contains(hash[2]),
			.east: "bcdef".contains(hash[3])
		]
	}
}

extension Direction {
	var value: String {
		switch self {
		case .north: "U"
		case .south: "D"
		case .west: "L"
		case .east: "R"
		}
	}
}

extension Direction {
	var point: Point2 {
		switch self {
		case .north: Point2(0, -1)
		case .south: Point2(0, 1)
		case .west: Point2(-1, 0)
		case .east: Point2(1, 0)
		}
	}
}
