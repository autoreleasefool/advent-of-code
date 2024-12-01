import AdventSupport
import Foundation

public class Year2016Day14: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		await findKeys(salt: input.contents, stretch: 1).description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		await findKeys(salt: input.contents, stretch: 2017).description
	}

	// MARK: Helpers

	private func findKeys(salt: String, stretch: Int) async -> Int {
		var keys: Set<Int> = []
		var candidateKeys: [Character: [(Int, String)]] = [:]
		var computedHashes: [Int: String] = [:]
		var index = -1

		while keys.count < 64 {
			index += 1

			if computedHashes[index] == nil {
				computedHashes.merge(
					await generateHashes(salt: salt, range: index..<(index + 1000), stretch: stretch)
				) { _, new in new }
			}

			let hash = computedHashes[index]!
			computedHashes[index] = nil

			hash
				.matches(of: /(.)\1\1\1\1/)
				.map(\.output.1)
				.toSet()
				.forEach { quintuple in
					let repeatedChar = quintuple.first!
					var removeCandidates = false
					for (candidateIndex, _) in candidateKeys[repeatedChar] ?? [] where candidateIndex + 1000 >= index {
						removeCandidates = true
						keys.insert(candidateIndex)
					}

					if removeCandidates {
						candidateKeys[repeatedChar] = []
					}
				}

			if let triple = hash.firstMatch(of: /(.)\1\1/) {
				candidateKeys[triple.output.1.first!, default: []].append((index, hash))
			}
		}

		return Array(keys).sorted()[..<64].max() ?? 0
	}

	private func generateHashes(salt: String, range: Range<Int>, stretch: Int) async-> [Int: String] {
		await withTaskGroup(of: [Int: String].self) { group in
			for subRange in range.evenlyChunked(in: 100) {
				group.addTask {
					subRange
						.reduce(into: [:]) { results, index in
							results[index] = "\(salt)\(index)".md5(times: stretch)
						}
				}
			}

			return await group.reduce(into: [:]) { results, hashes in
				results.merge(hashes) { _, new in new }
			}
		}
	}
}
