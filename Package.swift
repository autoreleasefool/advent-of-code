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
	],
	targets: [
		.executableTarget(
			name: "advent-of-code",
			dependencies: [
				"Year2015",
				.product(name: "ArgumentParser", package: "swift-argument-parser"),
				.product(name: "ConcurrencyExtras", package: "swift-concurrency-extras"),
			],
			path: "Sources/CLI"
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
			dependencies: [
				"AdventSupport"
			],
			path: "2015"
		),
	]
)
