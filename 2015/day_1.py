"""Solution for Advent of Code 2015 Day 1."""


def read_input(filename: str) -> list[str]:
    """Opens and reads a file."""

    with open(filename, "r", encoding="UTF-8") as f:
        data = f.readlines()
        return data[0]


def find_floor_no(direction: str) -> int:
    """Returns the floor number based on a set of 
    directions given as a string consisting of 
    parentheses."""

    floor_no = 0

    for char in direction:
        if char == "(":
            floor_no += 1
        elif char == ")":
            floor_no -= 1

    return floor_no


def find_basement_position(direction: str) -> int:

    floor_no = 0
    index = 0

    for char in direction:
        index += 1
        if char == "(":
            floor_no += 1
        if char == ")":
            floor_no -= 1
        if floor_no == -1:
            return index


if __name__ == "__main__":
    instructions = read_input("day_1_input.txt")
    correct_floor = find_floor_no(instructions)
    basement_position = find_basement_position(instructions)

    print(f"The floor Santa needs to go to is {correct_floor}")
    print(f"The position of the character that causes Santa to first enter the basement is {
          basement_position}")
