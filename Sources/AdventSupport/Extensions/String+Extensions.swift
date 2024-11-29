import CryptoKit
import Foundation

extension String {
	public static let alphabet = "abcdefghijklmnopqrstuvwxyz"
	public static let digits = "0123456789"
	public static let hexAlphabet = Array("0123456789abcdef".unicodeScalars)
}

// MARK: Transformation

extension String {
	public func integers() -> [Int] {
		matches(of: /-?\d+/)
			.map(\.output)
			.compactMap { Int($0) }
	}
}

// MARK: Indexing

extension String {
	public subscript(offset: Int) -> Character {
		self[index(startIndex, offsetBy: offset)]
	}
}

// MARK: Hashing

extension String {

	public var md5: String {
		String(
			Insecure.MD5
				.hash(data: self.data(using: .utf8)!)
				.reduce(into: "".unicodeScalars) { result, value in
					result.append(Self.hexAlphabet[Int(value / 0x10)])
					result.append(Self.hexAlphabet[Int(value % 0x10)])
				}
		)
	}

	public func md5(times: Int = 1) -> String {
		var hash = self
		for _ in 0..<times { hash = hash.md5 }
		return hash
	}
}
