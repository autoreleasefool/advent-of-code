from aoc import AOC, chunk, flatten
from typing import List, Tuple
from math import prod

aoc = AOC(year=2021, day=16)
data = aoc.load()


def read_binary(hexa: str) -> List[int]:
    # Convert hexadecimal to binary, padding all hex values to 4 digit binary vlaues
    return flatten([list(str(bin(int(c, 16))[2:].rjust(4, "0"))) for c in hexa])


def read_value(packet: List[int], len: int) -> Tuple[List[int], int]:
    # Read an int from the start of the packet and return the packet's remainder, and the value
    return packet[len:], int("".join(packet[:len]), 2)


def perform_operation(op: int, values: List[int]) -> int:
    if op == 0:
        return sum(values)
    elif op == 1:
        return prod(values)
    elif op == 2:
        return min(values)
    elif op == 3:
        return max(values)
    elif op == 5:
        return 1 if values[0] > values[1] else 0
    elif op == 6:
        return 1 if values[0] < values[1] else 0
    elif op == 7:
        return 1 if values[0] == values[1] else 0


def read_literal(packet: List[int]) -> Tuple[List[int], int]:
    # Read the literal value
    literal = []
    for c in chunk(5, packet):
        literal.append(c[1:])
        if c[0] == "0":
            break
    packet = packet[len(literal) * 5 :]
    literal = int("".join(flatten(literal)), 2)

    return packet, literal


def read_subpackets_by_length(
    packet: List[int],
) -> Tuple[List[int], List[int], List[int]]:
    packet, total_subpacket_length = read_value(packet, 15)
    subpackets = packet[:total_subpacket_length]
    values, versions = [], []
    while subpackets:
        subpackets, value, subversions = read_packet(subpackets)
        values.append(value)
        versions += subversions

    return packet[total_subpacket_length:], values, versions


def read_subpackets_by_count(
    packet: List[int],
) -> Tuple[List[int], List[int], List[int]]:
    packet, total_subpackets = read_value(packet, 11)
    values, versions = [], []
    for _ in range(total_subpackets):
        packet, value, subversions = read_packet(packet)
        values.append(value)
        versions += subversions

    return packet, values, versions


def read_packet(packet: List[int]):
    packet, version = read_value(packet, 3)
    packet, type_id = read_value(packet, 3)

    if type_id == 4:
        packet, literal = read_literal(packet)
        return packet, literal, [version]
    else:
        # Parse the subpackets
        packet, length_type_id = read_value(packet, 1)

        if length_type_id == 0:
            packet, subvalues, subversions = read_subpackets_by_length(packet)
            value = perform_operation(type_id, subvalues)
            return packet, value, subversions + [version]
        else:
            packet, subvalues, subversions = read_subpackets_by_count(packet)
            value = perform_operation(type_id, subvalues)
            return packet, value, subversions + [version]


packet = read_binary(data.contents())
_, output, versions = read_packet(packet)

aoc.p1(sum(versions))
aoc.p2(output)
