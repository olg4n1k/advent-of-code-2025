import sys
import re
import math

from typing import List, Set, Tuple, Union
from functools import cache
from collections import deque
from copy import copy

def main() -> int:
    machines = _parse_input()

    result = 0
    for i, machine in enumerate(machines):
        buttons, joltage = machine
        presses = _find_min_presses(joltage, buttons)
        print(f"Machine {i} result: {presses}")
        result += presses

    print(f"Result: {result}")
    return 0


def _build_button_map(joltage: tuple[int, ...], buttons: tuple[set[int], ...]) -> tuple[list[int], dict[int, tuple[set[int]]]]:
    n = len(joltage)
    button_map = dict()
    for i in range(n):
        button_map[i] = tuple(b for b in buttons if i in b)

    unordered = set(range(n))
    order = []

    while unordered:
        # Heuristic: find smallest counter first by button length, then max by joltage
        min_len = min(len(button_map[i]) for i in unordered)
        i = max(filter(lambda i: len(button_map[i]) == min_len, unordered), key=lambda i: joltage[i])
        # Variant 1:
        # i = min(unordered, key=lambda i: len(button_map[i]))
        # Variant 2: same as current, but with min by joltage
        order.append(i)
        unordered.remove(i)
        for j in unordered:
            button_map[j] = tuple(b for b in button_map[j] if i not in b)

    return (order, button_map)


def _find_min_presses(joltage: tuple[int, ...], buttons: tuple[tuple[int, ...], ...]) -> int:
    order, button_map = _build_button_map(joltage, buttons)
    # print(f"Order: {order}, map: {button_map}")

    states = {joltage: 0}
    for i in order:
        new_states = dict()
        button_options = button_map[i]
        for state, presses in states.items():
            value = state[i]
            for new_state in _process_counter(i, state, button_options):
                new_presses = presses + value
                if new_state in new_states:
                    new_states[new_state] = min(new_states[new_state], new_presses)
                else:
                    new_states[new_state] = new_presses

        # print(f"After {i} counter: {len(new_states)}")
        states = new_states

    return min(states.values())

def _process_counter(i: int, state: tuple[int, ...], button_options: tuple[set[int]]) -> list[tuple[int, ...]]:
    value = state[i]
    if value == 0:
        return [state]
    
    if not button_options:
        return []

    result = []
    button = button_options[0]
    # We can press this button between 0 and value times
    next_state = list(state)
    for _ in range(value + 1):
        # Recurse to other button options
        result.extend(_process_counter(i, tuple(next_state), button_options[1:]))

        # Apply press for the next cycle (since first cycle has no presses)
        negative = False
        for j in button:
            x = next_state[j] - 1
            negative = negative or x < 0
            next_state[j] = x

        if negative:
            # All subsequent presses are also invalid
            break

    return result

def _parse_input() -> list[tuple[tuple[set[int], ...], tuple[int, ...]]]:
    # filename = "test.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()

        line_regex = re.compile(r"\[[#\.]+\] ([^\{]+) \{([\d\,]+)\}\s*")
        buttons_regex = re.compile(r"\(([\d,]+)\)")
        def parse_machine(line: str) -> tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]:
            line_match = line_regex.fullmatch(line)

            button_strs = buttons_regex.findall(line_match.group(1))
            buttons = tuple(set(int(n) for n in s.split(',')) for s in button_strs)

            joltage = tuple(int(s) for s in line_match.group(2).split(','))
            return (buttons, joltage)

        return [parse_machine(line) for line in data]


if __name__ == '__main__':
    sys.exit(main())
