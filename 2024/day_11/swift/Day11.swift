import AdventSupport
import Foundation

public class Year2024Day11: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		var integers = input.integersByLine()[0]

		for _ in 0..<25 {
			var nextIntegers: [Int] = []
			for i in integers {
				if i == 0 {
					nextIntegers.append(1)
				} else {
					let string = String(i)
					if string.count % 2 == 0 {
						nextIntegers.append(Int(string[string.startIndex..<string.index(string.startIndex, offsetBy: string.count / 2)])!)
						nextIntegers.append(Int(string[string.index(string.startIndex, offsetBy: string.count / 2)...])!)
					} else {
						nextIntegers.append(i * 2024)
					}
				}
			}
			integers = nextIntegers
		}

		return integers.count.description
	}

	// MARK: Part 2

	// Stone: [Steps: Length]
	private var cache: [Int: [Int: Int]] = [:]

	public func solvePart2(_ input: Input) async throws -> String? {
//		var cache: [Int: [Int: Int]] = [:]
		var integers = input.integersByLine()[0]

		return calculateLength(integers, toDepth: 75).description

//		return totalLength.description
	}

	var totalHits = 0
	var totalMisses = 0

	func calculateLength(_ integers: [Int], toDepth: Int) -> Int {
//		print("Calculate length for \(integers) to depth \(toDepth)")
//		print(toDepth)

		if toDepth == 0 {
//			print(integers)
			return integers.count
		}

		var totalLength = 0

		for i in integers {
//			print(i)
			if let cached = cache[i], let depthCache = cached[toDepth] {
//				print("Cache hit")
//				totalHits += 1
//				print("Cache Hit for \(i) at \(toDepth): \(depthCache)")
				totalLength += depthCache
				continue
			}
//			print("Cache miss")
//			totalMisses += 1

			let subLength: Int
			if i == 0 {
				 subLength = calculateLength([1], toDepth: toDepth - 1)
			} else {
				let string = String(i)
				if string.count % 2 == 0 {
					subLength = calculateLength([
						Int(string[string.startIndex..<string.index(string.startIndex, offsetBy: string.count / 2)])!,
						Int(string[string.index(string.startIndex, offsetBy: string.count / 2)...])!
					], toDepth: toDepth - 1)
				} else {
					subLength = calculateLength([i * 2024], toDepth: toDepth - 1)
//					nextIntegers.append(i * 2024)
				}
			}

			cache[i, default: [:]][toDepth] = subLength
//			print("Caching \(i) at \(toDepth): \(subLength)")
			totalLength += subLength
		}

		return totalLength
	}

//		integers = [16192]
//		var totalLength = 0
//		var numberOfZeros = 0
//		for i in integers {
//			print("Starting \(i)")
//			var integers = [i]
//
//			for step in 0..<75 {
//				print("Step \(step)")
////				print(integers)
//				integers = integers.filter { ![0, 2, 4, 40, 48, 4048, 8096, 8].contains($0) }
//				print(integers)
//				numberOfZeros += integers.count(where: { $0 == 0 })
////				integers = integers.filter { String($0).count > 2 }
//
//				var nextIntegers: [Int] = []
//				for i in integers {
//					if i == 0 {
//						nextIntegers.append(1)
//					} else {
//						let string = String(i)
//						if string.count % 2 == 0 {
//							nextIntegers.append(Int(string[string.startIndex..<string.index(string.startIndex, offsetBy: string.count / 2)])!)
//							nextIntegers.append(Int(string[string.index(string.startIndex, offsetBy: string.count / 2)...])!)
//						} else {
//							nextIntegers.append(i * 2024)
//						}
//					}
//				}
//				integers = nextIntegers
//			}
//
//			totalLength += integers.count
//		}
//
//		return totalLength.description
//	}
}
