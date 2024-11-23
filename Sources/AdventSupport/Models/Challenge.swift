import Foundation

public struct Challenge: Sendable {
	public let year: Year
	public let day: Int

	public var dayZeroPadded: String {
		String(format: "%02d", day)
	}

	public init(year: Year, day: Int) {
		self.year = year
		self.day = day
	}

	public var startTime: Date {
		let calendar = Calendar(identifier: .gregorian)
		var components = DateComponents()
		components.year = year.intValue
		components.month = 12
		components.day = day
		components.hour = 0
		components.minute = 0
		components.second = 0
		components.timeZone = TimeZone(abbreviation: "EST")
		return calendar.date(from: components)!
	}

	public var hasStarted: Bool {
		Date() >= startTime
	}

	public var website: URL {
		URL(string: "https://adventofcode.com/\(year)/day/\(day)")!
	}

	public var websiteInput: URL {
		website.appending(path: "input")
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
