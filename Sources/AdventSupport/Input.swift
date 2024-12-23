import Foundation
import RegexBuilder

public struct Input {
	public let contents: String

	public init(challenge: Challenge) throws {
		let inputFile = challenge.workingDirectory.appending(path: "input.txt")
		if FileManager.default.fileExists(atPath: inputFile.path()) {
			self.contents = try String(
				contentsOf: challenge.workingDirectory
					.appending(path: "input.txt"),
				encoding: .utf8
			)
			.trimmingCharacters(in: .newlines)
		} else {
			print("No input found at \(inputFile.path())")
			self.contents = ""
		}
	}

	public init(contents: String) {
		self.contents = contents
	}

	public func lines() -> [String] {
		contents.components(separatedBy: .newlines)
	}

	/// List of integers from the input, when they are separated by newlines.
	public func integers() -> [Int] {
		contents.integers()
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
