import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day23: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let connections = getConnections(from: input)

		return connections
			.filter { $0.key.hasPrefix("t") }
			.flatMap {
				var systems: [String] = []
				var queue: [[String]] = [[$0.key]]
				while let system = queue.popFirst() {
					let last = system.last!

					if system.count == 3 {
						systems.append(system.sorted().joined(separator: ","))
					} else {
						for next in connections[last]! {
							guard system.allSatisfy({ connections[$0]!.contains(next) }) else { continue }
							queue.append(system + [next])
						}
					}
				}

				return systems
			}
			.toSet()
			.count.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let connections = getConnections(from: input)

		var systems: Set<String> = []

		for start in connections.keys {
			var queue: [[String]] = [[start]]
			while let system = queue.popFirst() {
				guard systems.insert(system.sorted().joined(separator: ",")).inserted else { continue }
				let last = system.last!

				for next in connections[last]! {
					guard system.allSatisfy({ connections[$0]!.contains(next) }) else { continue }
					queue.append(system + [next])
				}
			}
		}

		return systems.max(by: { $0.count < $1.count })!
	}

	// MARK: Helpers

	private func getConnections(from input: Input) -> [String: Set<String>] {
		input.lines()
			.compactMap { $0.firstMatch(of: /(\w+)-(\w+)/) }
			.map { (String($0.output.1), String($0.output.2)) }
			.reduce(into: [:]) { connections, connection in
				connections[connection.0, default: []].insert(connection.1)
				connections[connection.1, default: []].insert(connection.0)
			}
	}
}
