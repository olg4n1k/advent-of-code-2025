import sys
import re


def main() -> int:
    rotations = _parse_input()
    
    dial = 50
    zeros = 0
    for (direction, clicks) in rotations:
        dial = _rotate(direction, clicks, dial)
        if dial == 0:
            zeros = zeros + 1

    print(f"Result: {zeros}")
    return 0


def _rotate(direction, clicks, dial):
    match direction:
        case 'R':
            c = 1
        case 'L':
            c = -1
        case _:
            raise ValueError("Invalid rotation direction")

    return (dial + c * clicks) % 100 


def _parse_input():
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()
        matches = [re.fullmatch(r"([L|R])(\d+)\n", line) for line in data]
        return [(m.group(1), int(m.group(2))) for m in matches]


if __name__ == '__main__':
    sys.exit(main())
