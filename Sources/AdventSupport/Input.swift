import Foundation

public struct Input {
	public let url: URL

	public init(challenge: Challenge) {
		self.url = challenge.workingDirectory
			.appending(path: "input.txt")
	}

	public func read() throws -> String {
		try String(contentsOf: url, encoding: .utf8)
			.trimmingCharacters(in: .whitespacesAndNewlines)
	}
}
