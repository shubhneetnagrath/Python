def min_window(text, target):
    required = {}

    for char in target:
        required[char] = required.get(char, 0) + 1

    window = {}
    left = 0
    formed = 0

    min_length = float("inf")
    min_left = 0

    for right in range(len(text)):
        char = text[right]
        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            formed += 1

        while formed == len(required):
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length
                min_left = left

            left_char = text[left]
            window[left_char] -= 1

            if left_char in required and window[left_char] < required[left_char]:
                formed -= 1

            left += 1

    if min_length == float("inf"):
        return ""

    return text[min_left:min_left + min_length]