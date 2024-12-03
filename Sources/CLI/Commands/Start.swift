import AdventSupport
import AppKit
import ArgumentParser
import Foundation
import Stencil

extension Commands {
	struct Start: AsyncParsableCommand {
		@Flag(help: "Open the Advent of Code website")
		var launchWebsite = false

		@Flag(help: "Fetch the input for the challenge")
		var fetchInput = false

		@SessionStorage("year")
		var sessionYear: Year = .y24

		@SessionStorage("day")
		var sessionDay: Int = 1

		mutating func run() async throws {
			let challenge = Challenge(year: sessionYear, day: sessionDay)

			try challenge.createTemplate()

			await withThrowingTaskGroup(of: Void.self) { group in
				if launchWebsite {
					group.addTask {
						try await challenge.waitToOpenWebsite()
					}
				}

				if fetchInput {
					group.addTask {
						try await challenge.waitToFetchInput()
					}
				}
			}
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
				"day": dayZeroPadded,
			]
		)

		let outputDirectory = workingDirectory
			.appending(path: "swift")

		try FileManager.default.createDirectory(at: outputDirectory, withIntermediateDirectories: true)

		let outputFile = outputDirectory
			.appending(path: "Day\(dayZeroPadded).swift")

		guard !FileManager.default.fileExists(atPath: outputFile.path()) else {
			print("Solution already exists at \(outputFile.path())")
			return
		}

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
