import re


def try_int(i):
    try:
        return int(i)
    except:
        return None


def parse_regex(regex, line, container=list, intify=True):
    try:
        groups = re.search(regex, line).groups()
        if intify:
            groups = [try_int(g) if try_int(g) is not None else g for g in groups]
        return container(groups)
    except:
        return None


def parse_number_line(line):
    return [int(match) for match in re.findall(r"-?\d+", line)]
