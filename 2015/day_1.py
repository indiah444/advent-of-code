def read_input(filename: str) -> list[str]:
    """Opens and reads a file."""

    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def find_floor_no(direction: str) -> int:
    floor_no = 0

    for char in direction:
        if char == "(":
            floor_no += 1
        elif char == ")":
            floor_no -= 1

    return floor_no


if __name__ == "__main__":
    print(find_floor_no(")())())"))
