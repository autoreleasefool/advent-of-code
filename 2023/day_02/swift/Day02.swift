import AdventSupport
import Foundation

public class Year2023Day02: Solver {
	public required init() {}

	public func solve(_ input: Input) async throws -> Solution {
		let part1Solution = try await solvePart1(input)
		let part2Solution = try await solvePart2(input)

		return Solution(part1: part1Solution, part2: part2Solution)
	}

	struct CubeSet {
		let red: Int
		let green: Int
		let blue: Int
	}

	struct Game {
		let id: Int
		let cubeSets: [CubeSet]
	}

	// MARK: Part 1

	private func solvePart1(_ input: Input) async throws -> String? {
		input
			.lines()
			.map { line in
				Game(
					id: Int(line.firstMatch(of: /Game (\d+):/)?.output.1 ?? "")!,
					cubeSets: parseCubeSets(from: line)
				)
			}
			.filter(isGamePossible(_:))
			.map(\.id)
			.reduce(0, +)
			.description
	}

	private func isGamePossible(_ game: Game) -> Bool {
		let availableCubes = [
			"red": 12,
			"green": 13,
			"blue": 14,
		]

		return game.cubeSets.allSatisfy { cubeSet in
			cubeSet.red <= availableCubes["red"]!
			&& cubeSet.green <= availableCubes["green"]!
			&& cubeSet.blue <= availableCubes["blue"]!
		}
	}

	// MARK: Part 2

	private func solvePart2(_ input: Input) async throws -> String? {
		input
			.lines()
			.map {
				let cubeSets = parseCubeSets(from: $0)
				let maxCubes = cubeSets.reduce(CubeSet(red: 0, green: 0, blue: 0)) { maxes, cubeSet in
					CubeSet(
						red: max(cubeSet.red, maxes.red),
						green: max(cubeSet.green, maxes.green),
						blue: max(cubeSet.blue, maxes.blue)
					)
				}

				return maxCubes.red * maxCubes.green * maxCubes.blue
			}
			.reduce(0, +)
			.description
	}


	// MARK: Helpers

	private func parseCubeSets(from line: String) -> [CubeSet] {
		let hands = line[line.firstIndex(of: ":")!...].components(separatedBy: ";")
		return hands.map {
			let red = Int($0.firstMatch(of: /(\d+) red/)?.output.1 ?? "0")!
			let blue = Int($0.firstMatch(of: /(\d+) blue/)?.output.1 ?? "0")!
			let green = Int($0.firstMatch(of: /(\d+) green/)?.output.1 ?? "0")!

			return CubeSet(red: red, green: green, blue: blue)
		}
	}
}
