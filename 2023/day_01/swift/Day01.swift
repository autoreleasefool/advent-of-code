import AdventSupport
import Foundation

public class Year2023Day01: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		input.digitsByLine()
			.reduce(0) { total, digits in
				total + Int("\(digits.first!)\(digits.last!)")!
			}
			.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let stringToDigits = [
			"one": "1",
			"two": "2",
			"three": "3",
			"four": "4",
			"five": "5",
			"six": "6",
			"seven": "7",
			"eight": "8",
			"nine": "9",
		]

		let digits: [String] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] + Array(stringToDigits.keys)

		return input.lines()
			.reduce(0) { total, line in
				let firstDigit = digits.min {
					(line.range(of: $0)?.lowerBound ?? line.endIndex) < (line.range(of: $1)?.lowerBound ?? line.endIndex)
				}!

				let lastDigit = digits.max {
					(line.ranges(of: $0).last?.upperBound ?? line.startIndex) < (line.ranges(of: $1).last?.upperBound ?? line.startIndex)
				}!

				let calibrationValue = Int("\(stringToDigits[firstDigit] ?? firstDigit)\(stringToDigits[lastDigit] ?? lastDigit)")!

				return total + calibrationValue
			}
			.description
	}
}
