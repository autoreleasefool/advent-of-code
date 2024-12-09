import AdventSupport
import Foundation

public class Year2024Day09: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: "2333133121414131402")
	}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		var disk: [Int] = []
		for (index, c) in input.contents.enumerated() {
			let digit = Int(String(c))!
			if index % 2 == 0 {
				disk.append(contentsOf: Array(repeating: index / 2, count: digit))
			} else {
				disk.append(contentsOf: Array(repeating: -1, count: digit))
			}
		}

		var j = disk.count - 1
		for i in 0..<disk.count {
			if disk[i] != -1 {
				continue
			}

			while disk[j] == -1 && j > i {
				j -= 1
			}

			if (j <= i) {
				break
			}

			disk[i] = disk[j]
			disk[j] = -1
		}

		var checksum = 0
		for i in 0..<disk.count where disk[i] != -1 {
			checksum += disk[i] * i
		}

		return checksum.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		var disk: [Int] = []
		var spaces: [Int: Int] = [:]
		var files: [Int: Int] = [:]
		for (index, c) in input.contents.enumerated() {
			let digit = Int(String(c))!
			if index % 2 == 0 {
				files[disk.count] = digit
				disk.append(contentsOf: Array(repeating: index / 2, count: digit))
			} else {
				spaces[disk.count] = digit
				disk.append(contentsOf: Array(repeating: -1, count: digit))
			}
		}

//		print(disk.map { $0 == -1 ? "." : "\($0)" }.joined())

		var spaceKeys = spaces.keys.sorted()
		for f in files.keys.sorted().reversed() {
			guard let s = spaceKeys.first(where: { (spaces[$0] ?? 0) >= files[f]! }) else { continue }

			guard s < f else {
				continue
			}

			for i in s..<s + files[f]! {
				disk[i] = disk[f]
			}
			for i in f..<f + files[f]! {
				disk[i] = -1
			}

//			print(disk.map { $0 == -1 ? "." : "\($0)" }.joined())

			if spaces[s]! == files[f]! {
				spaces[s] = nil
			} else if spaces[s]! > files[f]! {
				let remaining = spaces[s]! - files[f]!
				spaces[s] = nil
				spaces[s + files[f]!] = remaining
			}
			spaceKeys = spaces.keys.sorted()
		}

//		var spaces: [Int: Int] = [:]
//		var inSpace: Int? = nil
//		var spaceChecker = 0
//		while spaceChecker < disk.count {
//			if disk[spaceChecker] == -1 {
//				if inSpace == nil {
//					inSpace = spaceChecker
//				}
//			} else {
//				if let inSpaceStart = inSpace {
//					inSpace = nil
//					spaces[inSpaceStart] = spaceChecker - inSpaceStart
//				}
//			}
//
//			spaceChecker += 1
//		}

		

//		var j = disk.count - 1
//		for i in 0..<disk.count {
//			if disk[i] != -1 {
//				continue
//			}
//
//			while disk[j] == -1 && j > i {
//				j -= 1
//			}
//
//			if (j <= i) {
//				break
//			}
//
//			disk[i] = disk[j]
//			disk[j] = -1
//		}

		var checksum = 0
		for i in 0..<disk.count where disk[i] != -1 {
			checksum += disk[i] * i
		}

//		print(disk.map { $0 == -1 ? "." : "\($0)" }.joined())

		return checksum.description
	}
}
