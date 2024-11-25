import Foundation
import RegexBuilder

public struct Input {
	public let contents: String

	public init(challenge: Challenge) throws {
		self.contents = try String(
			contentsOf: challenge.workingDirectory
				.appending(path: "input.txt"),
			encoding: .utf8
		)
		.trimmingCharacters(in: .whitespacesAndNewlines)
	}

	public init(contents: String) {
		self.contents = contents
	}

	public func lines() -> [String] {
		contents.components(separatedBy: .newlines)
	}

	/// List of numbers from the input, when they are separated by newlines.
	public func numbers() -> [Double] {
		lines().compactMap(Double.init)
	}

	/// List of integers from the input, when they are separated by newlines.
	public func integers() -> [Int] {
		lines().compactMap(Int.init)
	}

	/// List of integers on each line of the puzzle input.
	public func integersByLine() -> [[Int]] {
		lines()
			.map { $0.integers() }
	}

	public func digitsByLine() -> [[Int]] {
		lines()
			.map {
				$0.compactMap { $0.wholeNumberValue }
			}
	}

	public func digitGrid() -> [[Int]] {
		digitsByLine()
	}

	public func characterGrid() -> [[Character]] {
		lines().map { Array($0) }
	}
}
