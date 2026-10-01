def longest_unique(text):
    left = 0
    chars = set()
    max_length = 0

    for right in range(len(text)):
        while text[right] in chars:
            chars.remove(text[left])
            left += 1

        chars.add(text[right])

        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length

    return max_length