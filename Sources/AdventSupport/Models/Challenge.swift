import Foundation

public struct Challenge {
	public let year: Year
	public let day: Int

	public var dayZeroPadded: String {
		String(format: "%02d", day)
	}

	public init(year: Year, day: Int) {
		self.year = year
		self.day = day
	}

	public var workingDirectory: URL {
		URL(filePath: FileManager.default.currentDirectoryPath)
			.appending(path: "\(year)")
			.appending(path: "day_\(dayZeroPadded)")
	}

	public var solverClassName: String {
		"Year\(year).Year\(year)Day\(dayZeroPadded)"
	}
}
