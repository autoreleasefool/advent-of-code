import AdventSupport
import Algorithms
import Collections
import Foundation

public class Year2024Day17: Solver {
	public required init() {}

	public func setUp(_ input: inout Input) async throws {
//		input = Input(contents: """
//Register A: 729
//Register B: 0
//Register C: 0
//
//Program: 0,1,5,4,3,0
//""")
//		input = Input(contents: """
//Register A: 2024
//Register B: 0
//Register C: 0
//
//Program: 0,3,5,4,3,0
//""")
}


	// MARK: Part 2

	public func solvePart2(_ input: Input) async throws -> String? {
		var registers: [String: Int128] = [:]
		let lines = input.integersByLine()
		let program: [Int128] = lines[4].map { Int128($0) }

		var testValue: Int128 = 0
		var inc: Int128 = 1
		var expectedOutput = [program[0], program[1]]
		var lastExpectedReached: Int128 = -1
		while true {
//			for i in Int128(0)..<8 {
				let initialValue = testValue + 0
				registers["A"] = initialValue
				registers["B"] = Int128(lines[1][0])
				registers["C"] = Int128(lines[2][0])

				var output: [Int128] = []
				while output.count < expectedOutput.count {
					output.append(runToOutput(registers: &registers, program: program))
				}

				if output == program {
					return initialValue.description
				}

				if output == expectedOutput {
					print("Last found \(expectedOutput) at \(lastExpectedReached)")
					if lastExpectedReached > 0 && initialValue - lastExpectedReached > 8 {
						print(initialValue, lastExpectedReached)
//						lastExpectedReached = -1
						inc = initialValue - lastExpectedReached
						lastExpectedReached = -1
						print("Found \(expectedOutput), updating inc to \(inc)")
						expectedOutput += [program[expectedOutput.count]]
					}

					lastExpectedReached = initialValue
				}
//			}

			testValue += inc

//
//			let output1 = runToOutput(registers: &registers, program: program)
//			let output2 = runToOutput(registers: &registers, program: program)
//			let output3 = runToOutput(registers: &registers, program: program)
//			if output1 == instructions[0] && output2 == instructions[1] && output3 == instructions[2] {
//				print(initialValue)
//			}
		}

		return nil
	}

	private func runToOutput(registers: inout [String: Int128], program: [Int128]) -> Int128 {
		func comboOperand(_ pointer: Int) -> Int128 {
			switch program[pointer] {
			case 0: return 0
			case 1: return 1
			case 2: return 2
			case 3: return 3
			case 4: return registers["A"]!
			case 5: return registers["B"]!
			case 6: return registers["C"]!
			default: fatalError("Invalid operand")
			}
		}

		var pointer = 0
		while pointer < program.count - 1 {
			switch program[pointer] {
			case 0:
				let numerator = registers["A"]!
				let denominator = pow(2.0, Double(comboOperand(pointer + 1)))
				registers["A"] = numerator / Int128(denominator)
			case 1:
				let first = registers["B"]!
				let second = program[pointer + 1]
				registers["B"] = first ^ Int128(second)
			case 2:
				let operand = comboOperand(pointer + 1)
				registers["B"] = operand % 8
			case 3:
				if registers["A"] != 0 {
					pointer = Int(program[pointer + 1])
					continue
				}
			case 4:
				let first = registers["B"]!
				let second = registers["C"]!
				registers["B"] = first ^ second
			case 5:
				let operand = comboOperand(pointer + 1) % 8
				return operand
			case 6:
				let numerator = registers["A"]!
				let denominator = pow(2.0, Double(comboOperand(pointer + 1)))
				registers["B"] = numerator / Int128(denominator)
			case 7:
				let numerator = registers["A"]!
				let denominator = pow(2.0, Double(comboOperand(pointer + 1)))
				registers["C"] = numerator / Int128(denominator)
			default:
				fatalError("Invalid instruction")
			}

			pointer += 2
		}

		fatalError("Missing output")
	}






	// MARK: Part 1

	public func solvePart1(_ input: Input) async throws -> String? {
		var registers: [String: Int] = [:]
		let lines = input.integersByLine()

		registers["A"] = lines[0][0]
		registers["B"] = lines[1][0]
		registers["C"] = lines[2][0]
		let instructions: [Int] = lines[4]
//		print(registers, instructions)

		func comboOperand(_ pointer: Int) -> Int {
			switch instructions[pointer] {
			case 0: return 0
			case 1: return 1
			case 2: return 2
			case 3: return 3
			case 4: return registers["A"]!
			case 5: return registers["B"]!
			case 6: return registers["C"]!
			default: fatalError("Invalid operand")
			}
		}

		var pointer: Int = 0
		var output: [Int] = []
		while pointer < instructions.count - 1 {
			switch instructions[pointer] {
			case 0:
				let numerator = registers["A"]!
				let denominator = pow(2.0, Double(comboOperand(pointer + 1)))
				registers["A"] = numerator / Int(denominator)
			case 1:
				let first = registers["B"]!
				let second = instructions[pointer + 1]
				registers["B"] = first ^ second
			case 2:
				let operand = comboOperand(pointer + 1)
				registers["B"] = operand % 8
			case 3:
				if registers["A"] != 0 {
					pointer = instructions[pointer + 1]
					continue
				}
			case 4:
				let first = registers["B"]!
				let second = registers["C"]!
				registers["B"] = first ^ second
			case 5:
				let operand = comboOperand(pointer + 1) % 8
				output.append(operand)
			case 6:
				let numerator = registers["A"]!
				let denominator = pow(2.0, Double(comboOperand(pointer + 1)))
				registers["B"] = numerator / Int(denominator)
			case 7:
				let numerator = registers["A"]!
				let denominator = pow(2.0, Double(comboOperand(pointer + 1)))
				registers["C"] = numerator / Int(denominator)
			default:
				fatalError("Invalid instruction")
			}

			pointer += 2
		}

//		print(registers)
		return output.map(String.init).joined(separator: ",")
	}
}
