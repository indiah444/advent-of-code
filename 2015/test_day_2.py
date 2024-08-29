from day_2 import find_box_surface_area, find_smallest_side_area


def test_find_box_surface_area_basic_input():
    """Tests that find_box_surface_area works with valid input."""
    l, w, h = 2, 3, 4

    assert find_box_surface_area(l, w, h) == 52


def test_find_smallest_side_area_basic_input():
    """Tests that find_smallest_side_area works with valid input."""
    l, w, h = 2, 3, 4

    assert find_smallest_side_area(l, w, h) == 6
