// swift-tools-version: 6.0

import PackageDescription

let package = Package(
	name: "aoc",
	platforms: [
		.macOS(.v15),
	],
	dependencies: [
		.package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.2.2"),
		.package(url: "https://github.com/pointfreeco/swift-concurrency-extras.git", from: "1.3.0"),
	],
	targets: [
		.executableTarget(
			name: "advent-of-code",
			dependencies: [
				.product(name: "ArgumentParser", package: "swift-argument-parser"),
				.product(name: "ConcurrencyExtras", package: "swift-concurrency-extras"),
			]
		),
	]
)
