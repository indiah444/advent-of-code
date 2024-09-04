def read_input(filename: str) -> list[str]:
    """Opens and reads a file."""

    with open(filename, "r", encoding="UTF-8") as f:
        return f.readlines()


def find_box_surface_area(l: int, w: int, h: int) -> int:
    """Returns the surface area of a given present."""

    return 2*l*w + 2*w*h + 2*h*l


def find_smallest_side_area(l: int, w: int, h: int) -> int:
    """Returns the area of the smallest side of a given present."""

    area_1 = l * w
    area_2 = l * h
    area_3 = w * h

    smallest_area = min(area_1, area_2, area_3)

    return smallest_area


def calculate_total_paper_needed(input_lines: list[str]) -> int:
    """Calculates total wrapping paper needed for all presents."""

    total_paper = 0
    for line in input_lines:
        l, w, h = map(int, line.strip().split("x"))
        surface_area = find_box_surface_area(l, w, h)
        smallest_side_area = find_smallest_side_area(l, w, h)
        total_paper += surface_area + smallest_side_area

    return total_paper


if __name__ == "__main__":
    input_lines = read_input("day_2_input.txt")
    total_paper = calculate_total_paper_needed(input_lines)

    print(f"Total wrapping paper needed: {total_paper}")
