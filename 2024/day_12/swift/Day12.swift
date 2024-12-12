import AdventSupport
import Foundation

public class Year2024Day12: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: """
//AAAAAA
//AAABBA
//AAABBA
//ABBAAA
//ABBAAA
//AAAAAA
//""")
	}

	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		let grid = mapGridToPoints(input.characterGrid())
		var visited: Set<Point2> = []
		var price = 0
		for (p, v) in grid {
			guard !visited.contains(p) else { continue }
			var region: Set<Point2> = [p]

			var queue: [Point2] = [p]
			while let next = queue.popLast() {
				guard !visited.contains(next) else { continue }

				if grid[next] == v {
					visited.insert(next)
					region.insert(next)
					queue.append(contentsOf: next.adjacentPoints())
				}
			}

			let area = region.count
			let perimeter = region.flatMap { $0.adjacentPoints() }.filter { !region.contains($0) }.count
			price += area * perimeter
//			print("Region \(region) of \(v) has area \(area) and perimeter \(perimeter)")
		}



		return price.description
	}

	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		let grid = mapGridToPoints(input.characterGrid())
		var visited: Set<Point2> = []
		var price = 0
		for (p, v) in grid {
			guard !visited.contains(p) else { continue }
			var region: Set<Point2> = [p]

			var queue: [Point2] = [p]
			while let next = queue.popLast() {
				guard !visited.contains(next) else { continue }

				if grid[next] == v {
					visited.insert(next)
					region.insert(next)
					queue.append(contentsOf: next.adjacentPoints())
				}
			}

			let area = region.count
//			let perimeter = region.flatMap { $0.adjacentPoints() }.filter { !region.contains($0) }.count

			var numberOfSides = 0
			let leftmost = region.min { $0.x < $1.x }!
			let rightmost = region.max { $0.x < $1.x }!
			let topmost = region.min { $0.y < $1.y }!
			let bottommost = region.max { $0.y < $1.y }!

//			guard v == "E" else { continue }

			var scannedLeft: Set<Point2> = []
			var scannedRight: Set<Point2> = []
			for y in topmost.y...bottommost.y {

				var inEdge = false

//				print("Scanning left to right from \(leftmost.x - 1) to \(rightmost.x + 1)")
				for scanX in leftmost.x - 1...rightmost.x + 1 {
					let point = Point2(x: scanX, y: y)
//					print("Point: \(point)")

					if region.contains(point) {
						if !scannedLeft.contains(point) {
							if !inEdge {
//								print("Found edge at \(point)")
								numberOfSides += 1
								inEdge = true

								var scanUp1 = point.up
								var scanUp2 = point.left.up
								while region.contains(scanUp1) && !region.contains(scanUp2) {
									scannedLeft.insert(scanUp1)
									scanUp1 = scanUp1.up
									scanUp2 = scanUp2.up
								}
//								print("Stopped at \(scanUp1) and \(scanUp2): \(region.contains(scanUp1)), \(!region.contains(scanUp2))")

								var scanDown1 = point.down
								var scanDown2 = point.left.down
								while region.contains(scanDown1) && !region.contains(scanDown2) {
									scannedLeft.insert(scanDown1)
									scanDown1 = scanDown1.down
									scanDown2 = scanDown2.down
								}
//								print("Stopped at \(scanDown1) and \(scanDown2): \(region.contains(scanDown1)), \(!region.contains(scanDown2))")
							}

							scannedLeft.insert(point)
						}
						inEdge = true


					} else {
						inEdge = false
					}
				}

//				scanned = []
				inEdge = false

//				print("Scanning right to left from \(rightmost.x + 1) to \(leftmost.x - 1)")
				for scanX in (leftmost.x - 1...rightmost.x + 1).reversed() {
					let point = Point2(x: scanX, y: y)

//					print("Point: \(point)")


					if region.contains(point) {
						if !scannedRight.contains(point) {
							if !inEdge {
//								print("Found edge at \(point)")
								numberOfSides += 1
								inEdge = true

								var scanUp1 = point.up
								var scanUp2 = point.right.up
								while region.contains(scanUp1) && !region.contains(scanUp2) {
									scannedRight.insert(scanUp1)
									scanUp1 = scanUp1.up
									scanUp2 = scanUp2.up
								}

								var scanDown1 = point.down
								var scanDown2 = point.right.down
								while region.contains(scanDown1) && !region.contains(scanDown2) {
									scannedRight.insert(scanDown1)
									scanDown1 = scanDown1.down
									scanDown2 = scanDown2.down
								}
							}
							scannedRight.insert(point)
						}

						inEdge = true

					} else {
						inEdge = false
					}
				}
			}





			var scannedDown: Set<Point2> = []
			var scannedUp: Set<Point2> = []
			for x in leftmost.x...rightmost.x {

				var inEdge = false

//				print("Scanning left to right from \(leftmost.x - 1) to \(rightmost.x + 1)")
				for scanY in topmost.y - 1...bottommost.y + 1 {
					let point = Point2(x: x, y: scanY)
//					print("Point: \(point)")

					if region.contains(point) {
						if !scannedDown.contains(point) {
							if !inEdge {
//								print("Found edge at \(point)")
								numberOfSides += 1
								inEdge = true

								var scanLeft1 = point.left
								var scanLeft2 = point.up.left
								while region.contains(scanLeft1) && !region.contains(scanLeft2) {
									scannedDown.insert(scanLeft1)
									scanLeft1 = scanLeft1.left
									scanLeft2 = scanLeft2.left
								}
//								print("Stopped at \(scanUp1) and \(scanUp2): \(region.contains(scanUp1)), \(!region.contains(scanUp2))")

								var scanRight1 = point.right
								var scanRight2 = point.up.right
								while region.contains(scanRight1) && !region.contains(scanRight2) {
									scannedDown.insert(scanRight1)
									scanRight1 = scanRight1.right
									scanRight2 = scanRight2.right
								}
//								print("Stopped at \(scanDown1) and \(scanDown2): \(region.contains(scanDown1)), \(!region.contains(scanDown2))")
							}

							scannedDown.insert(point)
						}
						inEdge = true


					} else {
						inEdge = false
					}
				}

//				scanned = []
				inEdge = false

//				print("Scanning right to left from \(rightmost.x + 1) to \(leftmost.x - 1)")
				for scanY in (topmost.y - 1...bottommost.y + 1).reversed() {
					let point = Point2(x: x, y: scanY)

//					print("Point: \(point)")


					if region.contains(point) {
						if !scannedUp.contains(point) {
							if !inEdge {
//								print("Found edge at \(point)")
								numberOfSides += 1
								inEdge = true

								var scanLeft1 = point.left
								var scanLeft2 = point.down.left
								while region.contains(scanLeft1) && !region.contains(scanLeft2) {
									scannedUp.insert(scanLeft1)
									scanLeft1 = scanLeft1.left
									scanLeft2 = scanLeft2.left
								}

								var scanRight1 = point.right
								var scanRight2 = point.down.right
								while region.contains(scanRight1) && !region.contains(scanRight2) {
									scannedUp.insert(scanRight1)
									scanRight1 = scanRight1.right
									scanRight2 = scanRight2.right
								}
							}
							scannedUp.insert(point)
						}

						inEdge = true

					} else {
						inEdge = false
					}
				}
			}







//			var numberOfSides = 0
//			var visitedAdj: Set<Point2> = []
//			let perimeter = region.flatMap { $0.adjacentPoints() }.filter { !region.contains($0) }
//			for point in perimeter {
//				for adj in point.adjacentPoints() where !region.contains(adj) && !visitedAdj.contains(adj) {
//					visitedAdj.insert(adj)
//					var next = adj
//
//					for dir in Direction.allCases {
//
//					}
//				}
//			}
//			var visitedAdj: Set<Point2> = []
//			for point in region {
//				for adj in point.adjacentPoints() where !region.contains(adj) && !visitedAdj.contains(adj) {
//					visitedAdj.insert(adj)
//					let adjInRegion = adj.adjacentPoints().filter { region.contains($0) }
//				}
//			}

			price += area * numberOfSides
			print("Region \(region) of \(v) has area \(area) and \(numberOfSides) sides")
		}



		return price.description
	}
}
