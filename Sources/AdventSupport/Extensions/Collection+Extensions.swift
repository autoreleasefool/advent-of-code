import Collections
import Foundation

extension Collection where Element: Hashable {
	public func toSet() -> Set<Element> {
		Set(self)
	}

	public func toOrderedSet() -> OrderedSet<Element> {
		OrderedSet(self)
	}
}

extension Array {
	public mutating func popFirst() -> Element? {
		isEmpty ? nil : removeFirst()
	}
}
