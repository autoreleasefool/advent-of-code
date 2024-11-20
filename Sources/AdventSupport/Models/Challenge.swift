import Foundation

public struct Challenge {
	public let year: Year
	public let day: Int

	public init(year: Year, day: Int) {
		self.year = year
		self.day = day
	}

	public var workingDirectory: URL {
		URL(filePath: FileManager.default.currentDirectoryPath)
			.appending(path: "\(year)")
			.appending(path: "day_\(String(format: "%02d", day))")
	}

	public var solverClassName: String {
		"Year\(year).Year\(year)Day\(String(format: "%02d", day))"
	}
}
