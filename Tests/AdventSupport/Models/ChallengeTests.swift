import Testing
@testable import AdventSupport

@Suite("Challenge Tests")
struct ChallengeTests {

	@Suite("dayZeroPadded")
	struct DayZeroPadded {

		@Test(
			"Prepends zero to single digits",
			arguments: zip(
				1...9,
				["01", "02", "03", "04", "05", "06", "07", "08", "09"]
			)
		)
		func prependsZero(day: Int, expected: String) {
			let challenge = Challenge(year: .y24, day: day)
			#expect(challenge.dayZeroPadded == expected)
		}

		@Test(
			"Does not prepend zero to double digits",
			arguments: zip(
				10...20,
				["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
			)
		)
		func doesNotPrependZero(day: Int, expected: String) {
			let challenge = Challenge(year: .y24, day: day)
			#expect(challenge.dayZeroPadded == expected)
		}
	}
}
