public enum Year: String, CaseIterable, Sendable, Codable, LosslessStringConvertible {
	case y15 = "2015"
	case y16 = "2016"
	case y17 = "2017"
	case y18 = "2018"
	case y19 = "2019"
	case y20 = "2020"
	case y21 = "2021"
	case y22 = "2022"
	case y23 = "2023"
	case y24 = "2024"

	public var description: String { rawValue }
	public var intValue: Int { Int(rawValue)! }

	public init?(_ description: String) {
		self.init(rawValue: description)
	}
}
