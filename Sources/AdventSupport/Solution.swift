import AppKit

public protocol Solver {
	init()

	func setUp(_ input: inout Input) async throws
	func solvePart1(_ input: Input) async throws -> String?
	func solvePart2(_ input: Input) async throws -> String?
}

extension Solver {
	public func setUp(_: inout Input) async throws {}
}

extension Solver {
	public func solve(_ input: inout Input, verbose: Bool) async throws -> Solution {
		func verbosePrint(_ string: String) {
			if verbose {
				print(string)
			}
		}

		let clock = ContinuousClock()

		try await setUp(&input)

		verbosePrint("Solving Part 1")
		var part1Solution: String?
		let part1Duration = try await clock.measure {
			part1Solution = try await solvePart1(input)
		}
		verbosePrint("Part 1: \(part1Solution ?? "N/A") in \(part1Duration.description)")

		verbosePrint("Solving Part 2")
		var part2Solution: String?
		let part2Duration = try await clock.measure {
			part2Solution = try await solvePart2(input)
		}
		verbosePrint("Part 2: \(part2Solution ?? "N/A") in \(part2Duration.description)")

		return Solution(
			part1: part1Solution,
			part1Duration: part1Duration,
			part2: part2Solution,
			part2Duration: part2Duration
		)
	}
}

public struct Solution {
	public let part1: String?
	public let part1Duration: Duration?
	public let part2: String?
	public let part2Duration: Duration?

	public init(
		part1: String? = nil,
		part1Duration: Duration? = nil,
		part2: String? = nil,
		part2Duration: Duration? = nil
	) {
		self.part1 = part1
		self.part1Duration = part1Duration
		self.part2 = part2
		self.part2Duration = part2Duration
	}

	public func copyToClipboard() {
		if let part2 {
			print("Copying Part 2 solution to clipboard")
			NSPasteboard.general.clearContents()
			NSPasteboard.general.setString(part2, forType: .string)
		} else if let part1 {
			print("Copying Part 1 solution to clipboard")
			NSPasteboard.general.clearContents()
			NSPasteboard.general.setString(part1, forType: .string)
		} else {
			print("No solution to copy to clipboard")
		}
	}
}
