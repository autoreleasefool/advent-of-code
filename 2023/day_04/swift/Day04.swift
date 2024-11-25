import AdventSupport
import Foundation

public class Year2023Day04: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		input
			// One scratchcard per line
			.lines()
			// Split into winning numbers and player numbers
			.map {
				$0.components(separatedBy: "|")
					.map { $0.integers() }
			}
			// Drop the scratch card #
			.map { (Set($0.first!.dropFirst()), $0.last!) }
			// Count the number of winning player numbers
			.map { winningNumbers, playerNumbers in playerNumbers.count(where: { winningNumbers.contains($0) }) }
			// Only consider scratch cards with at least one winning number
			.filter { (matches: Int) -> Bool in matches > 0 }
			// Calculate the prize for each scratch card
			.map { (matches: Int) -> Int in Int(pow(2.0, Double(matches - 1))) }
			.reduce(0, +)
			.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		var scratchCardCopies: [Int: Int] = [:]

		input
			// One scratchcard per line
			.lines()
			.enumerated()
			// Split into winning numbers and player numbers
			.map {
				(
					$0.offset,
					$0.element.components(separatedBy: "|")
						.map { $0.integers() }
				)
			}
			// Drop the scratch card #
			.map { ($0, Set($1.first!.dropFirst()), $1.last!) }
			// Count the number of winning player numbers
			.map { cardNumber, winningNumbers, playerNumbers in
				(cardNumber, playerNumbers.count(where: { winningNumbers.contains($0) }))
			}
			.filter { _, matches in matches > 0 }
			.forEach { cardNumber, matches in
				(1...matches)
					.forEach { scratchCardCopies[cardNumber + $0, default: 0] += 1 + (scratchCardCopies[cardNumber] ?? 0) }
			}

		return (input.lines().count + scratchCardCopies.values.reduce(0, +)).description
	}
}
