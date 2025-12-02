"""Unit tests for day1 module functions."""
import os
import subprocess
import time

import pytest

from day1.utils import (count_zero_lands_part1, count_zero_lands_part2,
                        read_input, turn_dial)


@pytest.mark.parametrize(
    "current_position, turn_amount, expected_position",
    [
        (11, 8, 19),
        (99, 1, 0),
        (95, 5, 0),
    ],
)
def test_turn_right(current_position, turn_amount, expected_position):
    """
    Test turn_right function with various cases.
    """
    assert turn_dial(current_position, turn_amount, 'R')[
        0] == expected_position


@pytest.mark.parametrize(
    "current_position, turn_amount, expected_position",
    [
        (19, 19, 0),
        (0, 1, 99),
        (5, 10, 95),
    ],
)
def test_turn_left(current_position, turn_amount, expected_position):
    """
    Test turn_left function with various cases.
    """
    assert turn_dial(current_position, turn_amount, 'L')[
        0] == expected_position


def test_read_input():
    """
    Test read_input function to ensure it reads lines correctly from a file.
    """
    test_lines = ["R10", "L20", "R30"]
    test_file = "test_input.txt"
    with open(test_file, "w") as f:
        f.write("\n".join(test_lines))

    turn_list = read_input(test_file)

    # delete the test file after reading
    os.remove(test_file)

    assert turn_list == test_lines


@pytest.mark.parametrize(
    "current_position, turn_amount, direction, expected_lands",
    [
        (50, 68, 'L', 1),
        (50, 25, 'R', 0),
        (50, 1000, 'R', 10),
        (50, 1000, 'L', 10),
        (50, 150, 'R', 2),
        (50, 150, 'L', 2),
        (0, 23, 'L', 0),
        (23, 23, 'L', 1),
        (95, 5, 'R', 1),
    ],
)
def test_turn_dial(current_position, turn_amount, direction, expected_lands):
    """
    Test turn_dial function for both directions and various turn amounts.
    """
    assert turn_dial(current_position, turn_amount,
                     direction)[1] == expected_lands


def test_count_zero_lands_part1():
    """
    Test to simulate a sequence of turns and verify final position.
    """
    lines = ['L68', 'L30', 'R48', 'L5', 'R60',
             'L55', 'L1', 'L99', 'R14', 'L82']

    password = count_zero_lands_part1(lines, verbose=False)

    assert password == 3

    lines = ['L50']

    assert count_zero_lands_part1(lines, verbose=False) == 1

    lines = ['R50']

    assert count_zero_lands_part1(lines, verbose=False) == 1

    lines = ['R25', 'L25', 'R25', 'L25']

    assert count_zero_lands_part1(lines, verbose=False) == 0


def test_integration_part1():
    """
    Integration test using command-line execution simulation.
    """
    base_command = "python day1/part1.py day1/test.txt"
    subprocess_command = f"{base_command}"
    result = subprocess.run(
        subprocess_command,
        shell=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout == "3\n"

    subprocess_command = f"{base_command} -v"
    result = subprocess.run(
        subprocess_command,
        shell=True,
        capture_output=True,
        text=True,
    )

    # Adjust expected output based on the test input
    assert result.stdout == "The dial landed on 0 a total of 3 times during this process.\n"
    assert result.stdout != ""

    subprocess_command = f"{base_command} -vv"
    result = subprocess.run(
        subprocess_command,
        shell=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout == """The dial starts by pointing at 50.
The dial is rotated L68 to point at 82.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32.
The dial landed on 0 a total of 3 times during this process.\n"""
    assert result.stdout != ""


def test_count_zero_lands_part2():
    """
    Test to simulate a sequence of turns and verify final position for part 2.
    """
    lines = ['L68', 'L30', 'R48', 'L5', 'R60',
             'L55', 'L1', 'L99', 'R14', 'L82']

    password = count_zero_lands_part2(lines, verbose=False)

    assert password == 6  # Updated expected value for part 2

    lines = ['L50']

    assert count_zero_lands_part2(lines, verbose=False) == 1

    lines = ['R50']

    assert count_zero_lands_part2(lines, verbose=False) == 1

    lines = ['R25', 'L25', 'R25', 'L25']

    assert count_zero_lands_part2(lines, verbose=False) == 0


def test_integration_part2():
    """
    Integration test using command-line execution simulation.
    """
    base_command = "python day1/part2.py day1/test.txt"
    subprocess_command = f"{base_command}"
    result = subprocess.run(
        subprocess_command,
        shell=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout == "6\n"

    subprocess_command = f"{base_command} -v"
    result = subprocess.run(
        subprocess_command,
        shell=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout == """The dial landed on 0 a total of 6 times during this process.\n"""  # Adjust expected output based on the test input
    assert result.stdout != ""

    subprocess_command = f"{base_command} -vv"
    result = subprocess.run(
        subprocess_command,
        shell=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout == """The dial starts by pointing at 50.
The dial is rotated L68 to point at 82; during this rotation, the number of times it points at 0 is 1.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55; during this rotation, the number of times it points at 0 is 1.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32; during this rotation, the number of times it points at 0 is 1.
The dial landed on 0 a total of 6 times during this process.\n"""
    assert result.stdout != ""


def test_part1():
    """
    Test the main function of part1.py directly.
    """
    subprocess_command = "python day1/part1.py day1/problem.txt"
    result = subprocess.run(
        subprocess_command,
        shell=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout == "1152\n"


def test_part2():
    """
    Test the main function of part2.py directly.
    """
    subprocess_command = "python day1/part2.py day1/problem.txt"
    start_time = time.time()
    result = subprocess.run(
        subprocess_command,
        shell=True,
        capture_output=True,
        text=True,
    )
    end_time = time.time()
    print(f"Execution time for part2 in python: {end_time - start_time} seconds")
    assert result.stdout == "6671\n"
