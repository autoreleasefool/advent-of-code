// swift-tools-version: 6.0

import PackageDescription

let package = Package(
	name: "aoc",
	platforms: [
		.macOS(.v15),
	],
	dependencies: [
		.package(url: "https://github.com/apple/swift-algorithms.git", from: "1.2.0"),
		.package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.2.2"),
		.package(url: "https://github.com/pointfreeco/swift-concurrency-extras.git", from: "1.3.0"),
		.package(url: "https://github.com/stencilproject/Stencil.git", from: "0.15.1"),
	],
	targets: [
		.executableTarget(
			name: "advent-of-code",
			dependencies: [
				"Year2015",
				"Year2016",
				"Year2017",
				"Year2018",
				"Year2019",
				"Year2020",
				"Year2021",
				"Year2022",
				"Year2023",
				"Year2024",
				.product(name: "ArgumentParser", package: "swift-argument-parser"),
				.product(name: "ConcurrencyExtras", package: "swift-concurrency-extras"),
				.product(name: "Stencil", package: "stencil"),
			],
			path: "Sources/CLI",
			resources: [
				.copy("Template")
			]
		),
		.target(
			name: "AdventSupport",
			dependencies: [
				.product(name: "Algorithms", package: "swift-algorithms"),
				.product(name: "ConcurrencyExtras", package: "swift-concurrency-extras"),
			]
		),
		.target(
			name: "Year2015",
			dependencies: ["AdventSupport"],
			path: "2015"
		),
		.target(
			name: "Year2016",
			dependencies: ["AdventSupport"],
			path: "2016"
		),
		.target(
			name: "Year2017",
			dependencies: ["AdventSupport"],
			path: "2017"
		),
		.target(
			name: "Year2018",
			dependencies: ["AdventSupport"],
			path: "2018"
		),
		.target(
			name: "Year2019",
			dependencies: ["AdventSupport"],
			path: "2019"
		),
		.target(
			name: "Year2020",
			dependencies: ["AdventSupport"],
			path: "2020"
		),
		.target(
			name: "Year2021",
			dependencies: ["AdventSupport"],
			path: "2021"
		),
		.target(
			name: "Year2022",
			dependencies: ["AdventSupport"],
			path: "2022"
		),
		.target(
			name: "Year2023",
			dependencies: ["AdventSupport"],
			path: "2023"
		),
		.target(
			name: "Year2024",
			dependencies: ["AdventSupport"],
			path: "2024"
		),
	]
)
