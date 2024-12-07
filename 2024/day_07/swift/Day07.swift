import AdventSupport
import Algorithms
import Foundation

public class Year2024Day07: Solver {
	public required init() {}

	// MARK: Part 1
	private var allowConcat: Bool = false

	public func solvePart1(_ input: Input) async throws -> String? {
		input
			.integersByLine()
			.filter {
				let testValue = $0[0]
				let otherValues = Array($0[1...])
				return equationExists(testValue: testValue, values: otherValues)
			}
			.map(\.first!)
			.reduce(0, +)
			.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		allowConcat = true
		return input
			.integersByLine()
			.filter {
				let testValue = $0[0]
				let otherValues = Array($0[1...])
				return equationExists(testValue: testValue, values: otherValues)
			}
			.map(\.first!)
			.reduce(0, +)
			.description
	}

	// MARK: Helpers

	private func equationExists(testValue: Int, values: [Int]) -> Bool {
		guard values.count > 1 else {
			return values.first == testValue
		}

		let remainingValues = values.count > 2 ? Array(values[2...]) : []
		let valuesSum = [values[0] + values[1]] + remainingValues
		let valuesProduct = [values[0] * values[1]] + remainingValues
		let valuesConcat = [Int("\(values[0])\(values[1])")!] + remainingValues

		return equationExists(testValue: testValue, values: valuesSum) ||
			equationExists(testValue: testValue, values: valuesProduct) ||
			(allowConcat && equationExists(testValue: testValue, values: valuesConcat))
	}
}
