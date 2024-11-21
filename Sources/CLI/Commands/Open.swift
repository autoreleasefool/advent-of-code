import AdventSupport
import AppKit
import ArgumentParser

extension Commands {
	struct Open: AsyncParsableCommand {
		@SessionStorage("year")
		var year: Year = .y24

		@SessionStorage("day")
		var day: Int = 1

		mutating func run() async throws {
			let challenge = Challenge(year: year, day: day)

			challenge.openWebsite()
		}
	}
}
