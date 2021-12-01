import re


def parse_regex(regex, line, container=list):
    try:
        return container(re.search(regex, line).groups())
    except:
        return None


def parse_number_line(line):
    return [int(match) for match in re.findall(r"-?\d+", line)]
