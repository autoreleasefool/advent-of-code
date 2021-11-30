# AOC

import util.aoc as aoc

AOC = aoc.AOC

# fmath

import util.fmath as fmath

chinese_remainder = fmath.chinese_remainder
mul_inv = fmath.mul_inv

# Computer

import util.comp as comp

Computer = comp.Computer

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


def flatten(l):
    return [item for sublist in l for item in sublist]


def find_all(s, f):
    return [m.start() for m in re.finditer(s, f)]
