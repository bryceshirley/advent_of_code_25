"""Unit tests for Fortran-compiled day1 module functions."""
import subprocess
import time
import os

import numpy as np
import pytest

import day1_fortran.dial_utils_fortran as duf
# import day1_fortran.part2_main_fortran as p2f
# import day1_fortran.part1_main_fortran as p1f


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
    pos = np.array(current_position)
    duf.dial_utils.turn_dial(pos, turn_amount, 'R')
    assert pos == expected_position

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
    Test turn_dial function to turn left using Fortran module.
    """
    pos = np.array(current_position)
    duf.dial_utils.turn_dial(pos, turn_amount, 'L')
    assert pos == expected_position

def test_read_input():
    """
    Test read_input function to ensure it reads lines correctly from a file.
    """
    test_lines = ["R10", "L20", "R30"]
    test_file = "test_input.txt"
    with open(test_file, "w") as f:
        f.write("\n".join(test_lines))

    max_lines = 20000
    turn_list = duf.dial_utils.read_input(test_file, max_lines)

    # Convert Fortran array of bytes to Python list of strings
    arr, val = turn_list
    py_list = [x.decode().strip() for x in arr if x.strip()]

    # delete the test file after reading
    os.remove(test_file)

    assert py_list == test_lines


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
    assert duf.dial_utils.turn_dial(current_position, turn_amount,
                     direction) == expected_lands

def test_integration_part1():
    """
    Integration test calling the compiled Fortran executable for Part 1.
    """
    command = "./day1_fortran/dial_sim_part1 day1/test.txt"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    assert result.stdout.strip() == "3"


def test_integration_part2():
    """
    Integration test calling the compiled Fortran executable for Part 2.
    """
    command = "./day1_fortran/dial_sim_part2 day1/test.txt"  # assuming you compiled Fortran program
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    assert result.stdout.strip() == "6"

def test_part1():
    """
    Integration test calling the compiled Fortran executable for Part 1.
    """
    command = "./day1_fortran/dial_sim_part1 day1/problem.txt"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    assert result.stdout.strip() == "1152"

def test_part2():
    """
    Test the main function of part2.py directly.
    """
    # time the execution
    start_time = time.time()
    command = "./day1_fortran/dial_sim_part2 day1/problem.txt"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    end_time = time.time()
    print(f"Execution time for part2 in fortran: {end_time - start_time} seconds")
    assert result.stdout.strip() == "6671"