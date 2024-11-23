import AdventSupport
import ArgumentParser

extension Year: ExpressibleByArgument {
	public init?(argument: String) {
		self.init(rawValue: argument)
	}
}
