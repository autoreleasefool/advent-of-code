import AdventSupport
import ArgumentParser
import Foundation
import Stencil

extension Commands {
	struct Start: AsyncParsableCommand {
		@SessionStorage("year")
		var sessionYear: Year = .y24

		@SessionStorage("day")
		var sessionDay: Int = 1

		mutating func run() async throws {
			let challenge = Challenge(year: sessionYear, day: sessionDay)

			try challenge.createTemplate()
		}
	}
}

// MARK: Challenge Extension

extension Challenge {
	func createTemplate() throws {
		let environment = Environment(loader: FileSystemLoader(bundle: [.main, .module]))

		let rendered = try environment.renderTemplate(
			name: "Template/Day.swift.stencil",
			context: [
				"year": "\(year)",
				"day": dayZeroPadded
			]
		)

		let outputDirectory = workingDirectory
			.appending(path: "swift")

		try FileManager.default.createDirectory(at: outputDirectory, withIntermediateDirectories: true)

		let outputFile = outputDirectory
			.appending(path: "Day\(dayZeroPadded).swift")

		try rendered.data(using: .utf8)?.write(to: outputFile)
	}
}

// MARK: Error

extension Commands.Start {
	enum CommandError: LocalizedError {
		case failedToCreateTemplate

		var errorDescription: String? {
			switch self {
			case .failedToCreateTemplate:
				"Failed to create template"
			}
		}
	}
}
