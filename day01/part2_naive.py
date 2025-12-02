import sys
import re


def main() -> int:
    rotations = _parse_input()
    
    dial = 50
    total_zeros = 0
    for (direction, clicks) in rotations:
        (dial, zeros) = _rotate(direction, clicks, dial)
        # print(f"Rotation: dial {dial}, zeros {zeros}")
        total_zeros += zeros

    print(f"Result: {total_zeros}")
    return 0


def _rotate(direction, clicks, dial):
    match direction:
        case 'R':
            s = 1
        case 'L':
            s = -1
        case _:
            raise ValueError("Invalid rotation direction")
   
    zeros = 0
    for _ in range(clicks):
        dial = (dial + s) % 100
        if dial == 0:
            zeros += 1

    return (dial, zeros)


def _parse_input():
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()
        matches = [re.fullmatch(r"([L|R])(\d+)\n", line) for line in data]
        return [(m.group(1), int(m.group(2))) for m in matches]


if __name__ == '__main__':
    sys.exit(main())
