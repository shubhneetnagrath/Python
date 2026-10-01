def min_sum(numbers, k):
    window_sum = 0

    # First window
    for i in range(k):
        window_sum += numbers[i]

    min_sum = window_sum

    # Slide the window
    for i in range(k, len(numbers)):
        window_sum = window_sum - numbers[i - k] + numbers[i]

        if window_sum < min_sum:
            min_sum = window_sum

    return min_sum