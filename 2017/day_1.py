def read_input(filename: str) -> list[str]:
    """Opens and reads a file."""

    with open(filename, "r", encoding="UTF-8") as f:
        data = f.readlines()
        return data[0]


def inverse_captcha(digits: int):
    total = 0
    extended_digits = digits + digits[0]

    for i in range(len(digits)):
        if extended_digits[i] == extended_digits[i + 1]:
            total += int(extended_digits[i])

    return total


def circular_list_captcha(digits: int):
    digits = [int(d) for d in digits]
    n = len(digits)
    halfway = n // 2
    total = 0

    for i in range(n):
        if digits[i] == digits[(i + halfway) % n]:
            total += digits[i]

    return total


if __name__ == "__main__":

    input_lines = read_input("day_1_input.txt")
    print(inverse_captcha(input_lines))
    print(circular_list_captcha(input_lines))
