import Foundation

extension Collection where Element: Hashable {
	public func toSet() -> Set<Element> {
		Set(self)
	}
}
