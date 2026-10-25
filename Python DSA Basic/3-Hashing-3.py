def two_sum(numbers, target):
    seen = set()

    for x in numbers:
        needed = target - x

        if needed in seen:
            return [needed, x]

        seen.add(x)

    return []