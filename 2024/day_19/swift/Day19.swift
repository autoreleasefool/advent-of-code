import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day19: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let towels = input.lines().first!.components(separatedBy: ", ")
		let designs = Array(input.lines().dropFirst(2))
		let towelRegex = try! Regex("(\(towels.joined(separator: "|")))+")

		return designs
			.filter { $0.wholeMatch(of: towelRegex) != nil }
			.count.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let towels = input.lines().first!.components(separatedBy: ", ")
		let designs = Array(input.lines().dropFirst(2))

		var cache: [String: Int] = [:]

		func traverse(string: String) -> Int {
			if string.isEmpty {
				return 1
			}

			if let cache = cache[String(string)] {
				return cache
			}

			let count = towels
				.filter { string.starts(with: $0) }
				.reduce(0) {
					$0 + traverse(string: String(string.dropFirst($1.count)))
				}

			cache[string] = count
			return count
		}

		return designs
			.reduce(0) { $0 + traverse(string: $1) }
			.description
	}
}
