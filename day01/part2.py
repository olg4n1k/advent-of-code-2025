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
    
    full_rotations = clicks // 100 
    shift = clicks % 100
    
    if shift == 0:
        return (dial, full_rotations)

    dial_w_overflow = dial + s * shift
    new_dial = dial_w_overflow % 100
    
    if (new_dial != dial_w_overflow and dial != 0) or (new_dial == 0):
        return (new_dial, full_rotations + 1)

    return (new_dial, full_rotations)


def _parse_input():
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()
        matches = [re.fullmatch(r"([L|R])(\d+)\n", line) for line in data]
        return [(m.group(1), int(m.group(2))) for m in matches]


if __name__ == '__main__':
    sys.exit(main())
