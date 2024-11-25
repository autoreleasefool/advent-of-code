extension String {
	public static let alphabet = "abcdefghijklmnopqrstuvwxyz"
	public static let digits = "0123456789"
}

// MARK: Transformation

extension String {
	public func integers() -> [Int] {
		matches(of: /-?\d+/)
			.map(\.output)
			.compactMap { Int($0) }
	}
}
