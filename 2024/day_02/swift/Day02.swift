import AdventSupport
import Foundation

public class Year2024Day02: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		input.integersByLine()
			.filter { $0.isSorted(incrementing: true) || $0.isSorted(incrementing: false) }
			.map { $0.sorted() }
			.filter {
				zip($0, $0.dropFirst()).allSatisfy { (1...3).contains($0.1 - $0.0) }
			}
			.count
			.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		input.integersByLine()
			.map { report in
				report.enumerated().map { i, _ in
					var updatedReport = report
					updatedReport.remove(at: i)
					return updatedReport
				}
			}
			.filter {
				$0.contains {
					let initialReport = $0
					let sortedReport = initialReport.sorted()
					return (initialReport.isSorted(incrementing: true) || initialReport.isSorted(incrementing: false))
						&& zip(sortedReport, sortedReport.dropFirst()).allSatisfy { (1...3).contains($0.1 - $0.0) }
				}
			}
			.count
			.description
	}
}
