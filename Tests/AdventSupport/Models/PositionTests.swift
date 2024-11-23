import Testing
@testable import AdventSupport

@Suite("Position tests")
struct PositionTests {
	@Suite("Grid tests")
	struct MapGridToPoints {
		@Test("NxN grid")
		func nxnGrid() {
			let grid = [
				["#", ".", "#"],
				[".", "#", "."],
				["#", ".", "#"],
			]

			let points = mapGridToPoints(grid)
			#expect(
				points == [
					Point2(0, 0): "#",
					Point2(1, 0): ".",
					Point2(2, 0): "#",
					Point2(0, 1): ".",
					Point2(1, 1): "#",
					Point2(2, 1): ".",
					Point2(0, 2): "#",
					Point2(1, 2): ".",
					Point2(2, 2): "#",
				]
			)
		}

		@Test("NxM grid")
		func mxnGrid() {
			let grid = [
				["#", ".", "#"],
				[".", "#", "."],
			]

			let points = mapGridToPoints(grid)
			#expect(
				points == [
					Point2(0, 0): "#",
					Point2(1, 0): ".",
					Point2(2, 0): "#",
					Point2(0, 1): ".",
					Point2(1, 1): "#",
					Point2(2, 1): ".",
				]
			)
		}
	}
}
