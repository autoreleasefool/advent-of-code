import AdventSupport
import Foundation

public class Year2024Day11: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		calculateLength(input.integers(), toDepth: 25).description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		calculateLength(input.integers(), toDepth: 75).description
	}

	// MARK: Helpers

	private var lengthToDepthCache: [Int: [Int: Int]] = [:]

	private func calculateLength(_ integers: [Int], toDepth depth: Int) -> Int {
		guard depth > 0 else { return integers.count }

		return integers
			.reduce(into: 0) { totalLength, i in
				if let valueCache = lengthToDepthCache[i], let valueToDepth = valueCache[depth] {
					totalLength += valueToDepth
					return
				}

				let subLength: Int
				if i == 0 {
					subLength = calculateLength([1], toDepth: depth - 1)
				} else {
					let strI = String(i)
					if strI.count % 2 == 0 {
						let firstHalf = Int(strI[strI.startIndex..<strI.index(strI.startIndex, offsetBy: strI.count / 2)])!
						let secondHalf = Int(strI[strI.index(strI.startIndex, offsetBy: strI.count / 2)...])!

						subLength = calculateLength([firstHalf, secondHalf], toDepth: depth - 1)
					} else {
						subLength = calculateLength([i * 2024], toDepth: depth - 1)
					}
				}

				lengthToDepthCache[i, default: [:]][depth] = subLength
				totalLength += subLength
			}
	}
}
