def build_prefix(numbers):
    prefix = [0]

    for x in numbers:
        prefix.append(prefix[-1] + x)

    return prefix
