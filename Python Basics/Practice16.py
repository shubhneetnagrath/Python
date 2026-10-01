def max_vowels(text, k):
    vowels = "aeiou"
    window_count = 0

    # First window
    for i in range(k):
        if text[i] in vowels:
            window_count += 1

    max_count = window_count

    # Slide the window
    for i in range(k, len(text)):
        if text[i - k] in vowels:
            window_count -= 1

        if text[i] in vowels:
            window_count += 1

        if window_count > max_count:
            max_count = window_count

    return max_count