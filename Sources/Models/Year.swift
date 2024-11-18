import ArgumentParser

enum Year: String, CaseIterable, Codable, LosslessStringConvertible, ExpressibleByArgument {
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

	var description: String { rawValue }

	init?(_ description: String) {
		self.init(rawValue: description)
	}

	init?(argument: String) {
		self.init(rawValue: argument)
	}
}
