import sys
import re
import math

from typing import List, Set, Tuple
from functools import cache
from collections import deque
from copy import copy

def main() -> int:
    machines = _parse_input()

    result = 0
    for machine in machines:
        indicators, buttons, _ = machine
        result += find_min_presses(indicators, buttons)

    print(f"Result: {result}")
    return 0


def find_min_presses(indicators: List[bool], buttons: List[List[int]]) -> int:
    target = tuple(indicators)
    start = tuple(False for _ in range(len(target)))

    queue = deque()
    queue.append((start, 0))
    visited = set()
    while len(queue) > 0:
        state, depth = queue.popleft()
        if state == target:
            return depth

        visited.add(state)
        for button in buttons:
            next_state = _press_button(state, button)
            if next_state not in visited:
                queue.append((next_state, depth + 1))

    raise ValueError(f"Could not reach target state {target}")


def _press_button(state: Tuple[bool, ...], button: List[int]) -> Tuple[bool, ...]:
    new_state = list(state)

    for i in button:
        new_state[i] = not state[i]

    return tuple(new_state)


def _parse_input() -> List[Tuple[List[bool], List[List[int]], List[int]]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()

        line_regex = re.compile(r"\[([#\.]+)\] ([^\{]+) \{([\d\,]+)\}\s*")
        buttons_regex = re.compile(r"\(([\d,]+)\)")
        def parse_machine(line: str) -> Tuple[List[bool], List[List[int]], List[int]]:
            line_match = line_regex.fullmatch(line)

            indicators = [ch == '#' for ch in line_match.group(1)]

            button_strs = buttons_regex.findall(line_match.group(2))
            buttons = [[int(n) for n in s.split(',')] for s in button_strs]

            joltage = [int(s) for s in line_match.group(3).split(',')]
            return (indicators, buttons, joltage)

        return [parse_machine(line) for line in data]


if __name__ == '__main__':
    sys.exit(main())
