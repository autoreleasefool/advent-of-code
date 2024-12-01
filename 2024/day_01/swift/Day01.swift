import AdventSupport
import Foundation

public class Year2024Day01: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let locationIds = input.integersByLine()
			.reduce(into: Array(repeating: [Int](), count: 2)) { (result: inout [[Int]], value: [Int]) in
				result[0].append(value[0])
				result[1].append(value[1])
			}
			.map { $0.sorted() }

		return zip(locationIds[0], locationIds[1])
			.reduce(into: 0) { $0 += abs($1.0 - $1.1) }
			.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let locationIds = input.integersByLine()
			.reduce(into: Array(repeating: [Int](), count: 2)) { (result: inout [[Int]], value: [Int]) in
				result[0].append(value[0])
				result[1].append(value[1])
			}

		let similarityList = locationIds[1].countOccurrences()

		return locationIds[0]
			.reduce(into: 0) { $0 += similarityList[$1, default: 0] * $1 }
			.description
	}
}
