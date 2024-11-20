import AdventSupport
import AppKit
import ArgumentParser

extension Commands {
	struct Open: AsyncParsableCommand {
		@SessionStorage("year")
		var year: Year = .y24

		@SessionStorage("day")
		var day: Int = 1

		var urlString: String {
			"https://adventofcode.com/\(year)/day/\(day)"
		}

		var calendarUrl: URL? {
			URL(string: urlString)
		}

		mutating func run() async throws {
			guard let calendarUrl else {
				print("Unable to launch. Confirm year and day have been set correctly: (\(year), \(day))")

				struct CannotParseUrl: LocalizedError {
					var url: String
					var errorDescription: String? { "Cannot parse \(url)" }
				}

				throw CannotParseUrl(url: urlString)
			}

			NSWorkspace.shared.open(calendarUrl)
		}
	}
}
