import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day19: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: """
//r, wr, b, g, bwu, rb, gb, br
//
//brwrr
//bggr
//gbbr
//rrbgbr
//ubwu
//bwurrg
//brgr
//bbrgwb
//""")
}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let patterns = input.lines().first!.components(separatedBy: ", ")
		let desiredDesigns = Array(input.lines().dropFirst(2))

		print(patterns)
		print(desiredDesigns)
		print("(\(patterns.joined(separator: "|")))+")

		var count = 0
		for design in desiredDesigns {
			if design.wholeMatch(of: try! Regex("(\(patterns.joined(separator: "|")))+")) != nil {
				count += 1
			}
		}

		return count.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let patterns = input.lines().first!.components(separatedBy: ", ").map { "(?<\($0)>\($0))"}
		let desiredDesigns = Array(input.lines().dropFirst(2))
		print("here")

//		print(patterns)
//		print(desiredDesigns)
//		print("(\(patterns.joined(separator: "|")))+")

		var count = 0
		var matches: Set<String> = []
		let permutations = patterns.uniquePermutations()
		print(Array(permutations).count * desiredDesigns.count)
		for (index, pattern) in permutations.enumerated() {
			let regex = try! Regex("(\(pattern.joined(separator: "|")))+")
//			print("(\(pattern.joined(separator: "|")))+")
			print(index)
			for design in desiredDesigns {
				if let match = design.wholeMatch(of: regex) {
					matches.insert(
						match.output
							.dropFirst()
							.filter { $0.substring != nil }
							.sorted(by: { $0.range!.lowerBound < $1.range!.lowerBound })
							.map { String($0.value.debugDescription) }
							.joined(separator: ",") + "---" + design
					)
//					print(design)
//					match.output
//					print(match.output.first(where: { $0.substring != nil && $0.name != nil })?.name)
//					count += 1
//					return nil
				}
			}
		}

		return matches.count.description
	}
}
