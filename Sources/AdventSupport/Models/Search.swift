import Foundation

public func depthFirstSearch<K: Hashable, V>(
	start: K,
	goal: K,
	graph: [K: V],
	adjacent: (K) -> [K]
) -> [K]? {
	search(
		start: start,
		goal: goal,
		graph: graph,
		adjacent: adjacent,
		next: { $0.popLast() }
	)
}

public func breadthFirstSearch<K: Hashable, V>(
	start: K,
	goal: K,
	graph: [K: V],
	adjacent: (K) -> [K]
) -> [K]? {
	search(
		start: start,
		goal: goal,
		graph: graph,
		adjacent: adjacent,
		next: { $0.popFirst() }
	)
}

public func search<K: Hashable, V>(
	start: K,
	goal: K,
	graph: [K: V],
	adjacent: (K) -> [K],
	next: (inout [(K, [K])]) -> (K, [K])?
) -> [K]? {
	var queue: [(K, [K])] = [(start, [start])]
	var visited: Set<K> = []

	while let (next, path) = next(&queue) {
		guard visited.insert(next).inserted else { continue }

		if next == goal {
			return path
		}

		for adj in adjacent(next) {
			queue.append((adj, path + [adj]))
		}
	}

	return nil
}

public func binarySearch<K>(
	items: [K],
	compare: (Int, K) -> Int
) -> Int? {
	var lower = 0
	var upper = items.count - 1

	while lower <= upper {
		let mid = (lower + upper) / 2
		let result = compare(mid, items[mid])
		if result == 0 {
			return mid
		} else if result < 0 {
			lower = mid + 1
		} else {
			upper = mid - 1
		}
	}

	return nil
}
