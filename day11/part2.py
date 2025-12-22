import sys
import re
import math


from collections import deque

def main() -> int:
    devices = _parse_input()
    rev_devices = _reverse_graph(devices)

    reachable_from_svr = _get_reachable_nodes(devices, "svr")
    print(f"{len(reachable_from_svr)} reachable from 'svr'")

    reachable_from_fft = _get_reachable_nodes(devices, "fft")
    reach_fft = _get_reachable_nodes(rev_devices, "fft")

    reachable_from_dac = _get_reachable_nodes(devices, "dac")
    reach_dac = _get_reachable_nodes(rev_devices, "dac")

    print(f"Is 'dac' reachable from 'fft': {'dac' in reachable_from_fft}")

    reach_out = _get_reachable_nodes(rev_devices, "out")

    first = reachable_from_svr.intersection(reach_fft)
    second = reachable_from_fft.intersection(reach_dac)
    third = reachable_from_dac.intersection(reach_out)

    print(f"Sections: 'svr' -> {len(first)} -> 'fft' -> {len(second)} -> 'dac' -> {len(third)} -> 'out'")

    # reachable_from_you = _get_reachable_nodes(devices, "you")
    # print(f"First part was {len(reachable_from_you.intersection(reach_out))}")

    first_paths = _calc_paths_dfs(devices, "svr", "fft", first)
    second_paths = _calc_paths_dfs(devices, "fft", "dac", second)
    third_paths = _calc_paths_dfs(devices, "dac", "out", third)

    result = first_paths * second_paths * third_paths
    print(f"Result: {result}")
    return 0


def _reverse_graph(devices: dict[str, set[str]]) -> dict[str, set[str]]:
    rev_devices = {}

    for node, children in devices.items():
        for child in children:
            if child not in rev_devices:
                rev_devices[child] = {node}
            else:
                rev_devices[child].add(node)

    return rev_devices


def _get_reachable_nodes(devices: dict[str, set[str]], start: str) -> set[str]:
    queue = deque()
    queue.append(start)
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)

            if node in devices:
                queue.extend(devices[node])

    return visited


def _calc_paths_dfs(devices: dict[str, set[str]], current: str, end: str, subset: set[str]) -> int:

    if current == end:
        return 1

    if current not in subset:
        return 0

    return sum(_calc_paths_dfs(devices, output, end, subset) for output in devices[current])


def _parse_input() -> dict[str, set[str]]:
    # filename = "test2.txt"
    filename = "input.txt"
    with open(filename, encoding="utf-8") as file:
        data = file.readlines()

        line_regex = re.compile(r"(\w+)\:((?: \w+)+)\s*")
        def parse_line(line: str) -> tuple[str, set[str]]:
            line_match = line_regex.fullmatch(line)

            device = line_match.group(1)
            outputs_str = line_match.group(2).strip()
            outputs = set(s for s in outputs_str.split(' '))

            return (device, outputs)

        return {k:v for (k, v) in (parse_line(line) for line in data)}


if __name__ == '__main__':
    sys.exit(main())
