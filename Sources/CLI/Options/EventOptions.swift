import ArgumentParser

struct EventOptions: ParsableArguments {
	@Option var year: Int?
	@Option var day: Int?
}
