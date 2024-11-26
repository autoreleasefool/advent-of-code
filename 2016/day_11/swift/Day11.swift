import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2016Day11: Solver {
	public required init() {}

	public func solvePart1(_ input: Input) async throws -> String? {
		findMinimumSteps(input)
	}

	public func solvePart2(_ input: Input) async throws -> String? {
		let updatedInput = Input(
			contents: [
				input
					.lines().first! +
					"elerium generator, elerium-compatible microchip, dilithium generator, dilithium-compatible microchip",
				input.lines().dropFirst().joined(separator: "\n")
			].joined(separator: "\n")
		)

		return findMinimumSteps(updatedInput)
	}

	// MARK: Helpers

	private func findMinimumSteps(_ input: Input) -> String {
		let items = input.lines()
			.flatMap { $0.matches(of: /(\w+) generator/) }
			.reduce(into: [String: Int]()) { map, item in
				guard !map.keys.contains(String(item.output.1)) else { return }
				map[String(item.output.1)] = map.count + 1
			}

		let floors = input.lines()
			.map {
				Floor(
					items: $0.matches(of: /(\w+)( gen|-com)/)
						.map { items[String($0.output.1)]! * ($0.output.2 == " gen" ? 1 : -1) }
				)
			}

		var visited: Set<String> = []
		var queue = [(Facility(elevator: 0, floors: floors), 0)]

		while let (facility, steps) = queue.popFirst() {
			guard visited.insert(facility.hashValue).inserted else { continue }

			if facility.floors.dropLast().allSatisfy(\.isEmpty) {
				return steps.description
			}

			queue.append(
				contentsOf: facility
					.neighbours()
					.map { ($0, steps + 1) }
			)
		}

		return ""
	}
}



struct Facility {
	var elevator: Int
	var floors: [Floor]

	var isValid: Bool {
		floors.allSatisfy(\.isValid)
	}

	var hashValue: String {
		elevator.description + floors.map(\.hashValue).joined()
	}

	var description: String {
		let allItems = floors.flatMap(\.items).toSet().filter { $0 > 0 }.sorted()
		return floors
			.enumerated()
			.reversed()
			.map { (floorNumber, floor) in
				"F\(floorNumber) " +
					(floorNumber == elevator ? "E " : ". ") +
					allItems
					.map { item in
						(floor.items.contains(item) ? " \(item) " : " . ") +
							(floor.items.contains(-item) ? " \(-item)" : " . ")
					}
					.joined(separator: " ")
			}
			.joined(separator: "\n") +
			"\n--------------------"
	}

	func neighbours() -> [Facility] {
		let newElevatorFloors = [
			elevator < floors.count - 1 ? elevator + 1 : nil,
			elevator > 0 ? elevator - 1 : nil
		]
			.compactMap { $0 }

		let moveableItemCombinations = product(
			[Int?](floors[elevator].items) + [nil],
			floors[elevator].items
		)
			.filter { $0 != $1 }

		return product(newElevatorFloors, moveableItemCombinations)
			.map { (newElevatorFloor: Int, itemsToMove: (Int?, Int)) -> Facility in
				Facility(
					elevator: newElevatorFloor,
					floors: floors
						.enumerated()
						.map { index, floor in
							if index == elevator {
								Floor(items: floor.items.filter { $0 != itemsToMove.0 && $0 != itemsToMove.1 })
							} else if index == newElevatorFloor {
								Floor(items: floor.items + [itemsToMove.0, itemsToMove.1].compactMap { $0 })
							} else {
								floor
							}
						}
				)
			}
			.filter(\.isValid)
	}
}

struct Floor {
	var items: [Int]

	var isEmpty: Bool { items.isEmpty }
	var isValid: Bool {
		isEmpty ||
			!items.contains(where: { $0 > 0 }) ||
			items.filter { $0 < 0 }.allSatisfy { items.contains(-$0) }
	}

	var hashValue: String {
		items.count.description + items.filter { $0 > 0 }.reduce(0, +).description
	}
}
