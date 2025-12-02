"""Utility functions for dial turning simulation."""

def turn_one_position(pos, direction):
    """
    Turn the dial to the right by a specified amount.

    Args:
        current_position (int): The current position on the dial (0-99).
        turn_amount (int): The amount to turn the dial to the right.

    Returns:
        int: The new position on the dial after turning right.
    """
    if direction == 'L':
        return (pos - 1) % 100
    if direction == 'R':
        return (pos + 1) % 100
    else:
        raise ValueError("Direction must be 'R' or 'L'.")


def turn_dial(pos, turn_amount, direction):
    """
    Turn the dial to the left by a specified amount.

    Args:
        pos (int): The current position on the dial (0-99).
        turn_amount (int): The amount to turn the dial to the left.

    Returns:
        int: The new position on the dial after turning left.
    """
    lands = 0
    for i in range(turn_amount):
        pos = turn_one_position(pos, direction)
        if pos == 0:
            lands += 1
    return pos, lands


def read_input(file_path):
    """
    Read input from a file and return a list of lines.

    Args:
        file_path (str): The path to the input file.
    Returns:
        list: A list of lines from the file.
    """
    with open(file_path) as file:
        lines = [line.strip() for line in file]
    return lines


def count_zero_lands_part1(lines, verbose=False):
    """
    Count how many times the dial lands on position 0.
    Args:
        lines (list): A list of turn instructions.
    """
    # Initialize starting position and counter
    position = 50
    count = 0
    if verbose:
        print(f"The dial starts by pointing at {position}.")
    for line in lines:
        direction = line[0]
        amount = int(line[1:])

        position, lands = turn_dial(position, amount, direction)

        if verbose:
            print(f"The dial is rotated {line} to point at {position}.")

        # Count how many times we land on position 0
        if position == 0:
            count += 1
    return count


def count_zero_lands_part2(lines, verbose=False):
    """
    Count how many times the dial lands on position 0, including during turns.
    Args:
        lines (list): A list of turn instructions.
    """
    # Initialize starting position and counter
    position = 50
    count = 0
    if verbose:
        print(f"The dial starts by pointing at {position}.")

    for line in lines:
        direction = line[0]
        amount = int(line[1:])

        position, lands = turn_dial(position, amount, direction)
        if verbose:
            stdout = f"The dial is rotated {line} to point at {position}"
            if lands > 0 and position != 0:
                stdout += f"; during this rotation, the number of times it points at 0 is {lands}"
            print(stdout+".")
            # print(tmp_position, position, lands)

        count += lands
    return count
