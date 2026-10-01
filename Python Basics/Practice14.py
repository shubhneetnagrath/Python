def longest_two_distinct(numbers):
    left = 0
    freq = {}
    max_length = 0

    for right in range(len(numbers)):
        # Add current element
        freq[numbers[right]] = freq.get(numbers[right], 0) + 1

        # Too many distinct values → shrink
        while len(freq) > 2:
            freq[numbers[left]] -= 1

            if freq[numbers[left]] == 0:
                del freq[numbers[left]]

            left += 1

        # Update maximum length
        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length

    return max_length