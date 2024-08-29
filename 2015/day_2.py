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


if __name__ == "__main__":
    pass
