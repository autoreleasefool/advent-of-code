from aoc import AOC
import re


aoc = AOC(year=2015, day=23)
data = aoc.load()

## Part 1

register_a = 0
register_b = 0
commands = []

# For each line in the input
for line in data.lines():
    # Add the line to the list of commands
    commands.append(line.strip())

# Start at command 0 and continue until an impossible command is invoked
current_command = 0
while current_command < len(commands):
    # Get the command and the register/values associated with it
    command = re.match(
        r"^(hlf|tpl|inc|jmp|jie|jio) ([ab]|[+-]?\d+)(, ([+-]?\d+))?$",
        commands[current_command],
    )

    if command.group(1) == "hlf":
        # Divide the specified register in half and continue to the next command
        current_command += 1
        if command.group(2) == "a":
            register_a = int(register_a / 2)
        elif command.group(2) == "b":
            register_b = int(register_b / 2)
    elif command.group(1) == "tpl":
        # Multiply the specified register by 3 and continue to the next command
        current_command += 1
        if command.group(2) == "a":
            register_a *= 3
        elif command.group(2) == "b":
            register_b *= 3
    elif command.group(1) == "inc":
        # Increment the specified register by 1 and continue to the next command
        current_command += 1
        if command.group(2) == "a":
            register_a += 1
        elif command.group(2) == "b":
            register_b += 1
    elif command.group(1) == "jmp":
        # Jump to the command relative to the current one, by offset
        current_command += int(command.group(2))
    elif command.group(1) == "jie":
        # Jump to the command relative to the current one, by offset, if the specified register is even
        # Otherwise, go to the next command
        if (command.group(2) == "a" and register_a % 2 == 0) or (
            command.group(2) == "b" and register_b % 2 == 0
        ):
            current_command += int(command.group(4))
        else:
            current_command += 1
    elif command.group(1) == "jio":
        # Jump to the command relative to the current one, by offset, if the specified register is one
        # Otherwise, go to the next command
        if (command.group(2) == "a" and register_a == 1) or (
            command.group(2) == "b" and register_b == 1
        ):
            current_command += int(command.group(4))
        else:
            current_command += 1

aoc.p1(register_b)

## Part 2

register_a = 1
register_b = 0
commands = []

# For each line in the input
for line in data.lines():
    # Add the line to the list of commands
    commands.append(line.strip())

# Start at command 0 and continue until an impossible command is invoked
current_command = 0
while current_command < len(commands):
    # Get the command and the register/values associated with it
    command = re.match(
        r"^(hlf|tpl|inc|jmp|jie|jio) ([ab]|[+-]?\d+)(, ([+-]?\d+))?$",
        commands[current_command],
    )

    if command.group(1) == "hlf":
        # Divide the specified register in half and continue to the next command
        current_command += 1
        if command.group(2) == "a":
            register_a = int(register_a / 2)
        elif command.group(2) == "b":
            register_b = int(register_b / 2)
    elif command.group(1) == "tpl":
        # Multiply the specified register by 3 and continue to the next command
        current_command += 1
        if command.group(2) == "a":
            register_a *= 3
        elif command.group(2) == "b":
            register_b *= 3
    elif command.group(1) == "inc":
        # Increment the specified register by 1 and continue to the next command
        current_command += 1
        if command.group(2) == "a":
            register_a += 1
        elif command.group(2) == "b":
            register_b += 1
    elif command.group(1) == "jmp":
        # Jump to the command relative to the current one, by offset
        current_command += int(command.group(2))
    elif command.group(1) == "jie":
        # Jump to the command relative to the current one, by offset, if the specified register is even
        # Otherwise, go to the next command
        if (command.group(2) == "a" and register_a % 2 == 0) or (
            command.group(2) == "b" and register_b % 2 == 0
        ):
            current_command += int(command.group(4))
        else:
            current_command += 1
    elif command.group(1) == "jio":
        # Jump to the command relative to the current one, by offset, if the specified register is one
        # Otherwise, go to the next command
        if (command.group(2) == "a" and register_a == 1) or (
            command.group(2) == "b" and register_b == 1
        ):
            current_command += int(command.group(4))
        else:
            current_command += 1

aoc.p2(register_b)
