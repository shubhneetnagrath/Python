def max_sum(numbers, k):
    window_sum = 0

    for i in range(k):
        window_sum += numbers[i]

    max_sum = window_sum

    for i in range(k, len(numbers)):
        window_sum = window_sum - numbers[i - k] + numbers[i]

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum 