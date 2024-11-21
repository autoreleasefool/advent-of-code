import AppKit

public protocol Solver {
	init()

	func solve(_ input: Input) async throws -> Solution
}

public struct Solution {
	public let part1: String?
	public let part2: String?

	public init(part1: String? = nil, part2: String? = nil) {
		self.part1 = part1
		self.part2 = part2
	}

	public func log() {
		print("==== Solution ====")
		if let part1 {
			print("Part 1: \(part1)")
		}
		if let part2 {
			print("Part 2: \(part2)")
		}
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
