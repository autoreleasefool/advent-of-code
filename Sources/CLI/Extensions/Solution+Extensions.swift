import AdventSupport
import Foundation

extension Solution {
	func write(to challenge: Challenge) throws {
		guard part1 != nil || part2 != nil else { return }

		var output = ""

		if let part1 {
			output += "\(part1)"
		}

		if let part2 {
			output += "\n\(part2)"
		}

		guard let data = output.data(using: .utf8) else {
			return
		}

		try data.write(to: challenge.workingDirectory.appending(path: "output.txt"))
	}

	func validate(against challenge: Challenge) throws {
		let outputFile = challenge.workingDirectory.appending(path: "output.txt")

		guard FileManager.default.fileExists(atPath: outputFile.path()) else {
			return
		}

		let output = try String(contentsOf: outputFile, encoding: .utf8)
			.trimmingCharacters(in: .whitespacesAndNewlines)

		guard !output.isEmpty else { return }

		let parts = output.components(separatedBy: .newlines)

		if let expectedPart1 = parts.first, expectedPart1 != part1 {
			throw ValidationError.part1FailedValidation(expected: expectedPart1, received: part1)
		}

		if parts.count == 2, let expectedPart2 = parts.last, expectedPart2 != part2 {
			throw ValidationError.part2FailedValidation(expected: expectedPart2, received: part2)
		}
	}
}

extension Solution {
	enum ValidationError: LocalizedError {
		case part1FailedValidation(expected: String, received: String?)
		case part2FailedValidation(expected: String, received: String?)

		var errorDescription: String? {
			switch self {
			case let .part1FailedValidation(expected, received):
				"Part 1 failed validation, expected '\(expected)', received '\(String(describing: received))'"
			case let .part2FailedValidation(expected, received):
				"Part 2 failed validation, expected '\(expected)', received '\(String(describing: received))'"
			}
		}
	}
}