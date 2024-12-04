import Collections
import Foundation

extension Collection where Element: Hashable {
	public func toSet() -> Set<Element> {
		Set(self)
	}

	public func toOrderedSet() -> OrderedSet<Element> {
		OrderedSet(self)
	}

	public func countOccurrences() -> [Element: Int] {
		self.reduce(into: [:]) { $0[$1, default: 0] += 1 }
	}
}

extension Array {
	public mutating func popFirst() -> Element? {
		isEmpty ? nil : removeFirst()
	}

	public subscript(safely index: Int) -> Element? {
		indices.contains(index) ? self[index] : nil
	}
}

extension Collection where Element: Comparable {
	public func isSorted(incrementing: Bool = true) -> Bool {
		incrementing ? self.sorted() == Array(self) : self.sorted().reversed() == Array(self)
	}
}
