"""Advent Of Code 2021 - Day 1"""


def read_input(filename: str) -> list[str]:
    """To read data from a file."""

    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def is_increase(nums: list[int]) -> int:
    larger_count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            larger_count += 1

    return larger_count


# print(is_increase([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))

day_1_input = read_input("day_1_input.txt")

print(is_increase(day_1_input))
