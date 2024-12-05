import AdventSupport
import Foundation

public class Year2024Day05: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let precedingRules: [Int: Set<Int>] = input
			.lines()
			.compactMap { $0.wholeMatch(of: /(\d+)\|(\d+)/) }
			.map { (Int($0.output.1)!, Int($0.output.2)!) }
			.reduce(into: [:]) { rules, newRule in
				rules[newRule.0, default: []].insert(newRule.1)
			}

		return input
			.lines()
			.filter { $0.contains(",") }
			.map { $0.integers() }
			.filter { updateFollowsRules(update: $0, rules: precedingRules) }
			.map { $0[$0.count / 2] }
			.reduce(0, +)
			.description
	}

	private func updateFollowsRules(update: [Int], rules: [Int: Set<Int>]) -> Bool {
		update
			.enumerated()
			.allSatisfy { precedingIndex, precedingValue in
				update[precedingIndex + 1..<update.count]
					.allSatisfy { followingValue in
						rules[followingValue]?.contains(precedingValue) != true
					}
			}
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let precedingRules: [Int: Set<Int>] = input
			.lines()
			.compactMap { $0.wholeMatch(of: /(\d+)\|(\d+)/) }
			.map { (Int($0.output.1)!, Int($0.output.2)!) }
			.reduce(into: [:]) { rules, newRule in
				rules[newRule.0, default: []].insert(newRule.1)
			}

		return input
			.lines()
			.filter { $0.contains(",") }
			.map { $0.integers() }
			.filter { !updateFollowsRules(update: $0, rules: precedingRules) }
			.map {
				$0.dropFirst()
					.reduce(into: [$0.first!]) { fixedUpdate, nextValue in
						let insertionIndex = fixedUpdate
							.enumerated()
							.first { precedingRules[nextValue]?.contains($0.element) == true }
							.map { $0.offset } ?? fixedUpdate.count

						fixedUpdate.insert(nextValue, at: insertionIndex)
					}
			}
			.map { $0[$0.count / 2] }
			.reduce(0, +)
			.description
	}
}
