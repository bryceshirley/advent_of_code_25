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
    command = "./day1_fortran/dial_sim_part2 day1/problem.txt"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    assert result.stdout.strip() == "6671"