import ArgumentParser

@main
struct AOC: AsyncParsableCommand {
	static let configuration = CommandConfiguration(
		abstract: "Advent of Code",
		subcommands: [
			Commands.Calendar.self,
			Commands.Login.self,
		]
	)
}

enum Commands {}
