import AdventSupport
import ArgumentParser

extension Commands {
	struct Calendar: AsyncParsableCommand {
		@Argument(
			help: "Event year",
			completion: .list(Year.allCases.map(\.rawValue))
		)
		var year: Year?

		@Argument(
			help: "Challenge day",
			completion: .list([1...25].map(\.description))
		)
		var day: Int?

		@SessionStorage("year")
		var sessionYear: Year = .y24

		@SessionStorage("day")
		var sessionDay: Int = 1

		mutating func run() async throws {
			if let year {
				sessionYear = year
			}

			if let day {
				sessionDay = day
			}

			print("Calendar is set to (\(sessionYear), \(sessionDay))")
		}
	}
}
