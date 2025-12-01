from utils import count_zero_lands_part2, read_input 
import subprocess
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Dial Turning Simulation")
    parser.add_argument("input_file", help="Path to the input file containing turn instructions")
    parser.add_argument("-v", action="store_true", default=False, help="Enable verbose output level 1")
    parser.add_argument("-vv", action="store_true", default=False, help="Enable verbose output level 2")
    args = parser.parse_args()

    lines = read_input(args.input_file)

    # Count how many times we land on position 0
    # If verbose level 2 is set, provide detailed output
    zero_lands = count_zero_lands_part2(lines, verbose=args.vv)

    if args.v or args.vv:
        print(f"The dial landed on 0 a total of {zero_lands} times during this process.")
    else:
        print(zero_lands)
    
    return 0

if __name__ == "__main__":
    main()