import Foundation
import Synchronization

@propertyWrapper
struct SessionStorage<Value: LosslessStringConvertible> {
	private let key: String
	private let initialValue: Value
	private var storage: SessionStorageSource {
		SessionStorageSource.shared
	}

	init(wrappedValue initialValue: Value, _ key: String) {
		self.key = key
		self.initialValue = initialValue
	}

	var wrappedValue: Value {
		get {
			do {
				return try storage.read(key: key) ?? initialValue
			} catch {
				print("Error reading \(key): \(error)")
				return initialValue
			}
		}
		set {
			do {
				try storage.write(newValue, to: key)
			} catch {
				print("Error writing \(newValue) to \(key): \(error)")
			}
		}
	}
}

extension SessionStorage: Decodable where Value: Decodable {}

fileprivate final class SessionStorageSource: Sendable {
	static let shared = SessionStorageSource()

	private let queue = DispatchQueue(label: "SessionStorageSource")
	private let sourceFile = URL(filePath: FileManager.default.currentDirectoryPath)
		.appending(path: ".aoc_cache")

	func read<V: LosslessStringConvertible>(key: String) throws -> V? {
		try queue.sync {
			let data = try Data(contentsOf: sourceFile)
			let json = try JSONSerialization.jsonObject(with: data) as? [String: Any]
			guard let value = json?[key] as? String else { return nil }
			return V(value)
		}
	}

	func write<V: LosslessStringConvertible>(_ value: V, to key: String) throws {
		try queue.sync {
			var json: [String: Any]
			if FileManager.default.fileExists(atPath: sourceFile.path()) {
				let data = try Data(contentsOf: sourceFile)
				json = (try JSONSerialization.jsonObject(with: data) as? [String: Any]) ?? [:]
				try FileManager.default.removeItem(at: sourceFile)
			} else {
				json = [:]
			}

			json[key] = value.description
			let outData = try JSONSerialization.data(withJSONObject: json)
			try outData.write(to: sourceFile)
		}
	}
}
