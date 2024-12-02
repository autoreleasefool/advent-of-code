import AdventSupport
import Foundation

public class Year2024Day02: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: """
//7 6 4 2 1
//1 2 7 8 9
//9 7 6 2 1
//1 3 2 4 5
//8 6 4 4 1
//1 3 6 7 9
//"""
//)
	}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		var answer = 0

		let lines = input.integersByLine()
		for (i, line) in lines.enumerated() {
			let isInc = line.sorted() == line
			let isDec = Array(line.sorted().reversed()) == line
			let sortedLin = line.sorted()
//			print(sortedLin)
			var isAdj = true
			for (j, l) in sortedLin.dropLast().enumerated() {
				let diff = sortedLin[j + 1] - sortedLin[j]
				if !(1...3).contains(diff) {
					isAdj = false

				}
			}

			if isAdj && (isInc || isDec) {
				answer += 1
			}
		}

//		input.integersByLine()
//			.filter { $0.sorted() == $0 || Array($0.sorted().reversed()) == $0 }


		return answer.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		var answer = 0

		let lines = input.integersByLine()
		for (i, ll) in lines.enumerated() {

//			var isValid = false
			for iRemove in 0..<ll.count {
				var line = ll
				line.remove(at: iRemove)

//				if isValid { break }
				let isInc = line.sorted() == line
				let isDec = Array(line.sorted().reversed()) == line
				let sortedLin = line.sorted()
				//			print(sortedLin)
				var isAdj = true
				for (j, l) in sortedLin.dropLast().enumerated() {
					let diff = sortedLin[j + 1] - sortedLin[j]
					if !(1...3).contains(diff) {
						isAdj = false
					}
				}

				if isAdj && (isInc || isDec) {
					answer += 1
					break
				}
			}
		}

//		input.integersByLine()
//			.filter { $0.sorted() == $0 || Array($0.sorted().reversed()) == $0 }


		return answer.description
	}
}
