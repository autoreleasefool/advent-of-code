# AOC

import util.aoc as aoc
import util.data.data as data

AOC = aoc.AOC
Data = data.Data

# Data

import util.data.rules as rules

Drop = rules.Drop
Numbers = rules.Numbers
Regex = rules.Regex
String = rules.String

# fmath

import util.fmath as fmath

chinese_remainder = fmath.chinese_remainder
mul_inv = fmath.mul_inv
numbers_from = fmath.numbers_from

# Computer

import util.comp as comp

Computer = comp.Computer

import util.intcode.computer as intcode

IntcodeComputer = intcode.IntcodeComputer

# Position

import util.position as position

Position = position.Position

# Direction
import util.direction as direction

Direction = direction.Direction

# Deck
import util.deck as deck

Deck = deck.Deck

# Util functions

import re


def transpose(l):
    return list(map(list, zip(*l)))


def chunk(count, l):
    return [l[i : i + count] for i in range(0, len(l), count)]


def flatten(l):
    return [item for sublist in l for item in sublist]


def find_all(s, f):
    return [m.start() for m in re.finditer(s, f)]


def sliding_window(iterable, size):
    return [iterable[i - (size - 1) : i + 1] for i in range(size - 1, len(iterable))]


def mins(iterable, count):
    return sorted(iterable)[:count]


def maxes(iterable, count):
    return sorted(iterable)[-count:]
