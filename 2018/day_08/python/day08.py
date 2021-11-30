from aoc import AOC


aoc = AOC(year=2018, day=8)
data = aoc.load()


## Part 1


def build_node(raw_node):
    header = {
        "children": raw_node[0],
        "metadata": raw_node[1],
    }

    node_length = 2
    children = []
    for _ in range(header["children"]):
        child = build_node(raw_node[node_length : -header["metadata"]])
        node_length += child["length"]
        children.append(child)

    metadata = raw_node[node_length : node_length + header["metadata"]]
    node_length += header["metadata"]

    return {
        "header": header,
        "length": node_length,
        "children": children,
        "metadata": metadata,
    }


root_node = build_node(data.numbers_by_line()[0])


def sum_metadata(node):
    total = sum(node["metadata"])
    for child in node["children"]:
        total += sum_metadata(child)
    return total


aoc.p1(sum_metadata(root_node))


## Part 2


def build_node(raw_node):
    header = {
        "children": raw_node[0],
        "metadata": raw_node[1],
    }

    node_length = 2
    children = []
    for _ in range(header["children"]):
        child = build_node(raw_node[node_length : -header["metadata"]])
        node_length += child["length"]
        children.append(child)

    metadata = raw_node[node_length : node_length + header["metadata"]]
    node_length += header["metadata"]

    return {
        "header": header,
        "length": node_length,
        "children": children,
        "metadata": metadata,
    }


root_node = build_node(data.numbers_by_line()[0])


def value_of_node(node):
    if not node["children"]:
        return sum(node["metadata"])

    meta_cache = {}
    value = 0
    for metadata in node["metadata"]:
        index = metadata - 1
        if index == -1:
            continue

        if index < node["header"]["children"]:
            if index not in meta_cache:
                meta_cache[index] = value_of_node(node["children"][index])
            value += meta_cache[index]
    return value


aoc.p2(value_of_node(root_node))
