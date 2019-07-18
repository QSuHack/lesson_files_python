def quick_exponentation(base: int, exponent: int) -> int:
    result = 1
    while exponent != 0:
        if exponent % 2 == 1:
            result *= base
        base **= 2
        exponent //= 2
    return result


print(quick_exponentation(int(input()), int(input())))
