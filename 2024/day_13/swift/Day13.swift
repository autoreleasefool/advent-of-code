import AdventSupport
import Foundation

public class Year2024Day13: Solver {
	public required init() {}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		solve(input, tokenLimit: 100, prizeOffset: 0).description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		solve(input, tokenLimit: Int.max, prizeOffset: 10000000000000).description
	}

	// MARK: Helpers

	private func solve(_ input: Input, tokenLimit: Int, prizeOffset: Int) -> Int {
		let machines: [[[Int]]] = input
			.integersByLine()
			.chunks(ofCount: 4)
			.filter { $0.count >= 3 }
			.map { Array($0) }

		let intersections: [(Double, Double)] = machines
			.map {
				(
					a: Point2(x: $0[0][0], y: $0[0][1]),
					b: Point2(x: $0[1][0], y: $0[1][1]),
					p: Point2(x: $0[2][0] + prizeOffset, y: $0[2][1] + prizeOffset)
				)
			}
			.map {
				let a1 = Double($0.a.x)
				let a2 = Double($0.a.y)
				let b1 = Double($0.b.x)
				let b2 = Double($0.b.y)
				let c1 = Double(-$0.p.x)
				let c2 = Double(-$0.p.y)

				let x1: Double = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
				let y1: Double = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)

				return (x1, y1)
			}

		return intersections
			.filter { floor($0.0) == $0.0 && floor($0.1) == $0.1 }
			.map { (Int($0.0), Int($0.1)) }
			.filter { $0.0 <= tokenLimit && $0.1 <= tokenLimit }
			.reduce(0) { $0 + $1.0 * 3 + $1.1 }
	}
}
