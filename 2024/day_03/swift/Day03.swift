import AdventSupport
import Foundation

public class Year2024Day03: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
	}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		var sum = 0
		for line in input.lines() {
//			print(line)
//			print(line.matches(of: /mul\((\d){1,3},(\d){1,3}\)/))
			for match in line.matches(of: /mul\((\d{1,3}),(\d{1,3})\)/) {
				let m1 = Int(match.output.1)!
				let m2 = Int(match.output.2)!
				print(m1, m2)
				sum += m1 * m2
			}
		}
		return sum.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		var sum = 0
		var enabled = true
		for line in input.lines() {
//			print(line)
//			print(line.matches(of: /mul\((\d){1,3},(\d){1,3}\)/))
			for match in line.matches(of: /do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)/) {
				if String(match.output.0) == "do()" {
					enabled = true
				} else if String(match.output.0) == "don't()" {
					enabled = false
				} else if enabled {
					let m1 = Int(match.output.1!)!
					let m2 = Int(match.output.2!)!
					print(m1, m2)
					sum += m1 * m2
				}
			}

//			for match in line.matches(of: /mul\((\d{1,3}),(\d{1,3})\)/) {
//				let m1 = Int(match.output.1)!
//				let m2 = Int(match.output.2)!
//				print(m1, m2)
//				sum += m1 * m2
//			}
		}
		return sum.description
	}
}
