import ArgumentParser

extension Commands {
	struct Login: AsyncParsableCommand {
		@Argument(help: "Session token from adventofcode.com")
		var token: String

		@SessionStorage("token")
		var sessionToken: String = ""

		mutating func run() async throws {
			self.sessionToken = token
			print("Updated session token")
		}
	}
}
