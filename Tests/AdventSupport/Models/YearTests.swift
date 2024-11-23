import Testing
@testable import AdventSupport

@Suite("Year tests")
struct YearTests {
	@Test(
		"Int value is correct",
		arguments: zip(
			Year.allCases,
			2015...2024
		)
	)
	func intValueIsCorrect(year: Year, expectedIntValue: Int) {
		#expect(year.intValue == expectedIntValue)
	}
}
