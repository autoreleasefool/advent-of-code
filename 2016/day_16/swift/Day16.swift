import AdventSupport
import Foundation

public class Year2016Day16: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		fillDisk(initialState: input.contents, diskSize: 272)
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		fillDisk(initialState: input.contents, diskSize: 35651584)
	}

	// MARK: Helpers

	private func fillDisk(initialState: String, diskSize: Int) -> String {
		var state = initialState
		while state.count < diskSize {
			state = expandState(state)
		}

		return generateChecksum(state: state, diskSize: diskSize)
	}

	private func expandState(_ state: String) -> String {
		let a = state
		let b = String(a.reversed().map { $0 == "0" ? "1" : "0" })
		return "\(a)0\(b)"
	}

	private func generateChecksum(state: String, diskSize: Int) -> String {
		func reduce(_ state: String) -> String {
			String(
				state
					.chunks(ofCount: 2)
					.map { $0.first == $0.last ? "1" : "0" }
			)
		}

		var checksum = reduce(String(state.prefix(diskSize)))
		while checksum.count.isMultiple(of: 2) {
			checksum = reduce(checksum)
		}

		return checksum
	}
}
