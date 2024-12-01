import AdventSupport
import AppKit
import Foundation

extension Challenge {

	// MARK: Meta

	func retrieveSolver() throws -> Solver {
		guard let solverClass = Bundle.main.classNamed(solverClassName),
					let solverType = solverClass as? Solver.Type else {
			struct SolutionClassNotFound: LocalizedError {
				let className: String
				var errorDescription: String? { "Could not find solution class \(className)" }
			}

			throw SolutionClassNotFound(className: solverClassName)
		}

		return solverType.init()
	}

	// MARK: Website

	func waitToOpenWebsite() async throws {
		let secondsToWait = startTime.timeIntervalSinceNow + 2.0
		if secondsToWait > 0 {
			print("Waiting \(secondsToWait.rounded())s to open in browser.")
			try await Task.sleep(until: .now + .seconds(secondsToWait))
		}

		openWebsite()
	}

	func openWebsite() {
		print("Opening \(website)")
		NSWorkspace.shared.open(website)
	}

	// MARK: Input

	func waitToFetchInput() async throws {
		let secondsToWait = startTime.timeIntervalSinceNow + 2.0
		if secondsToWait > 0 {
			print("Waiting \(secondsToWait.rounded())s to fetch input.")
			try await Task.sleep(until: .now + .seconds(secondsToWait))
		}

		try await fetchInput(verbose: true)
	}

	func fetchInput(verbose: Bool = false) async throws {
		func verbosePrint(_ string: String) {
			if verbose { print(string) }
		}

		let inputFile = workingDirectory.appending(path: "input.txt")

		verbosePrint("Fetching input, storing to \(inputFile)")

		guard !FileManager.default.fileExists(atPath: inputFile.path()) else {
			verbosePrint("Input exists at \(inputFile), not fetching")
			return
		}

		@SessionStorage("token")
		var token = ""

		guard !token.isEmpty else {
			verbosePrint("No token available, exiting.")
			return
		}

		var request = URLRequest(url: websiteInput)
		request.setValue("https://github.com/autoreleasefool/advent-of-code", forHTTPHeaderField: "User-Agent")
		request.setValue("session=\(token)", forHTTPHeaderField: "Cookie")

		let (data, _) = try await URLSession.shared.data(for: request)

		guard let inputString = String(bytes: data, encoding: .utf8),
					!inputString.contains("Puzzle input") && !inputString.contains("Please don't repeatedly") else {
			verbosePrint("Invalid token, exiting.")
			return
		}

		try data.write(to: inputFile)
	}
}
