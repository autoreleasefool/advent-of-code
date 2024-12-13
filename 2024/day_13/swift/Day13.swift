import AdventSupport
import Foundation

public class Year2024Day13: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//			input = Input(contents: """
//	Button A: X+94, Y+34
//	Button B: X+22, Y+67
//	Prize: X=8400, Y=5400
//	
//	Button A: X+26, Y+66
//	Button B: X+67, Y+21
//	Prize: X=12748, Y=12176
//	
//	Button A: X+17, Y+86
//	Button B: X+84, Y+37
//	Prize: X=7870, Y=6450
//	
//	Button A: X+69, Y+23
//	Button B: X+27, Y+71
//	Prize: X=18641, Y=10279
//	""")
	}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		var fewestTokens = 0

//		print(input.integersByLine().chunks(ofCount: 4))
		for machineChunk in input.integersByLine().chunks(ofCount: 4) {
			print(machineChunk)
			guard machineChunk.count >= 3 else { continue }
			let machine = Array(machineChunk)
//			print(machine)
			let aValue = Point2(x: machine[0][0], y: machine[0][1])
//			print(aValue)
			let bValue = Point2(x: machine[1][0], y: machine[1][1])
//			print(bValue)
			let prize = Point2(x: machine[2][0], y: machine[2][1])
//			print(prize)

			var initialState = State(aPresses: 0, bPresses: 0, aValue: aValue, bValue: bValue)
			var visited: Set<State> = []
			var queue = [initialState]

			var fewestTokensByMachine: Int?
//			print(initialState)

			while !queue.isEmpty, let state = queue.popFirst() {
//				print(visited.count)
				if visited.contains(state) {
//					print("Visited")
					continue
				}
				visited.insert(state)

//				if state.aPresses > 100 || state.bPresses > 100 {
////					print("Too many")
////					print(queue.count)
//					continue
//				}

				if state.x > prize.x || state.y > prize.y {
//					print("Too far")
					continue
				}

				if state.tokensSpent > fewestTokensByMachine ?? Int.max {
//					print("Too many tokens")
					continue
				}

				if state.point == prize {
//					print("Found \(state.point) at \(state.tokensSpent)")
					fewestTokensByMachine = min(fewestTokensByMachine ?? Int.max, state.tokensSpent)
				} else {
					var aPressed = state
					aPressed.aPresses += 1
					var bPressed = state
					bPressed.bPresses += 1

					queue.append(aPressed)
					queue.append(bPressed)
				}
			}

//			print("Here")

//			print(fewestTokensByMachine)

			if let fewestTokensByMachine {
				fewestTokens += fewestTokensByMachine
			}

//			print("Fewest tokens \(fewestTokens)")
		}

		return fewestTokens.description
	}

	struct State: Hashable {
		var aPresses: Int
		var bPresses: Int
		let aValue: Point2
		let bValue: Point2

		var tokensSpent: Int {
			aPresses * 3 + bPresses
		}

		var x: Int {
			aValue.x * aPresses + bValue.x * bPresses
		}

		var y: Int {
			aValue.y * aPresses + bValue.y * bPresses
		}

		var point: Point2 { Point2(x, y) }
	}
	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		var fewestTokens = 0

//		print(input.integersByLine().chunks(ofCount: 4))
		for machineChunk in input.integersByLine().chunks(ofCount: 4) {
			print(machineChunk)
			guard machineChunk.count >= 3 else { continue }
			let machine = Array(machineChunk)
//			print(machine)
			let aValue = Point2(x: machine[0][0], y: machine[0][1])
//			print(aValue)
			let bValue = Point2(x: machine[1][0], y: machine[1][1])
//			print(bValue)
			let prize = Point2(x: machine[2][0], y: machine[2][1])
//			print(prize)

			let a1 = Double(aValue.x)
			let b1 = Double(bValue.x)
			let c1 = Double(-(prize.x + 10000000000000))

			let a2 = Double(aValue.y)
			let b2 = Double(bValue.y)
			let c2 = Double(-(prize.y + 10000000000000))

			let x1 = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
			let y1 = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)

			print(x1, y1)

			if floor(x1) == x1 && floor(y1) == y1 {

				fewestTokens += Int(x1) * 3 + Int(y1)
			}

//			if x1 > 0 && y1 > 0 {
//				fewestTokens +=
//			}

//			var initialState = State(aPresses: 0, bPresses: 0, aValue: aValue, bValue: bValue)
//			var visited: Set<State> = []
//			var queue = [initialState]
//
//			var fewestTokensByMachine: Int?
////			print(initialState)
//
//			while !queue.isEmpty, let state = queue.popFirst() {
////				print(visited.count)
//				if visited.contains(state) {
////					print("Visited")
//					continue
//				}
//				visited.insert(state)
//
////				if state.aPresses > 100 || state.bPresses > 100 {
//////					print("Too many")
//////					print(queue.count)
////					continue
////				}
//
//				if state.x > prize.x || state.y > prize.y {
////					print("Too far")
//					continue
//				}
//
//				if state.tokensSpent > fewestTokensByMachine ?? Int.max {
////					print("Too many tokens")
//					continue
//				}
//
//				if state.point == prize {
////					print("Found \(state.point) at \(state.tokensSpent)")
//					fewestTokensByMachine = min(fewestTokensByMachine ?? Int.max, state.tokensSpent)
//				} else {
//					var aPressed = state
//					aPressed.aPresses += 1
//					var bPressed = state
//					bPressed.bPresses += 1
//
//					queue.append(aPressed)
//					queue.append(bPressed)
//				}
//			}

//			print("Here")

//			print(fewestTokensByMachine)

//			if let fewestTokensByMachine {
//				fewestTokens += fewestTokensByMachine
//			}

//			print("Fewest tokens \(fewestTokens)")
		}

		return fewestTokens.description
	}
}
