import ArgumentParser

@main
struct AOC: AsyncParsableCommand {
	static let configuration = CommandConfiguration(
		abstract: "Advent of Code",
		subcommands: [
			Commands.Calendar.self,
			Commands.Login.self,
			Commands.Open.self,
			Commands.Run.self,
			Commands.Start.self,
			Commands.Test.self,
		]
	)
}

enum Commands {}
