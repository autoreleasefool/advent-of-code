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
}
