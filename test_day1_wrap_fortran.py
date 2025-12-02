"""Unit tests for Fortran-compiled day1 module functions."""
from dbm import gnu
import os
import subprocess

import pytest
import numpy as np

import day1_fortran.dial_utils_fortran as duf


@pytest.mark.parametrize(
    "current_position, turn_amount, expected_position",
    [
        (11, 8, 19),
        (99, 1, 0),
        (95, 5, 0),
    ],
)
def test_turn_right(current_position, turn_amount, expected_position):
    pos = np.array([current_position], dtype=np.int32)
    lands = duf.dial_utils.turn_dial(pos, turn_amount, b'R')
    assert pos[0] == expected_position

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
    pos = np.array([current_position], dtype=np.int32)
    lands = duf.dial_utils.turn_dial(pos, turn_amount, b'L')
    assert pos[0] == expected_position

def test_integration_part1(tmp_path):
    """
    Integration test calling the compiled Fortran executable for Part 1.
    """
    test_file = tmp_path / "test_input.txt"
    test_lines = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    test_file.write_text("\n".join(test_lines))

    exe_name = "./day1_fortran/dial_sim_part1"  # assuming you compiled Fortran program
    result = subprocess.run(f"{exe_name} {test_file}", shell=True, capture_output=True, text=True)
    assert result.stdout.strip() == "3"


def test_integration_part2(tmp_path):
    """
    Integration test calling the compiled Fortran executable for Part 2.
    """
    test_file = tmp_path / "test_input.txt"
    test_lines = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    test_file.write_text("\n".join(test_lines))

    exe_name = "./day1_fortran/dial_sim_part2"  # assuming you compiled Fortran program
    result = subprocess.run(f"{exe_name} {test_file}", shell=True, capture_output=True, text=True)
    assert result.stdout.strip() == "6"


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

def test_part1():
    """
    Integration test calling the compiled Fortran executable for Part 2.
    """
    test_file = "day1/problem.txt"
    exe_name = "./day1_fortran/dial_sim_part1"  # assuming you compiled Fortran program
    result = subprocess.run(f"{exe_name} {test_file}", shell=True, capture_output=True, text=True)
    assert result.stdout.strip() == "1152"

def test_part2():
    """
    Test the main function of part2.py directly.
    """
    test_file = "day1/problem.txt"

    exe_name = "./day1_fortran/dial_sim_part2"  # assuming you compiled Fortran program
    result = subprocess.run(f"{exe_name} {test_file}", shell=True, capture_output=True, text=True)
    assert result.stdout.strip() == "6671"