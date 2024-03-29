# AOC

import util.aoc_wrapper as aoc_wrapper
import util.data.data as data

AOC = aoc_wrapper.AOC
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
prod = fmath.prod

# Computer

import util.comp as comp

Computer = comp.Computer

import util.intcode.computer as intcode

IntcodeComputer = intcode.IntcodeComputer

# Position

from util.position import *

# Direction
import util.direction as direction

Direction = direction.Direction

# Deck
import util.deck as deck

Deck = deck.Deck

# Util functions

from util.functions import *

# Strings function

from util.strings import *

# Regex

from util.data.regex import parse_number_line

# Ranges

from util.ranges import *

# Strings

from util.strings import *
