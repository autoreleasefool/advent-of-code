import Foundation

extension FixedWidthInteger {
	public var size: Int {
		String(self).count
	}
}
