def min_subarray_length(numbers, target):
    left = 0
    window_sum = 0
    min_length = float("inf")

    for right in range(len(numbers)):
        window_sum += numbers[right]

        # Shrink the window while sum is enough
        while window_sum >= target:
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length

            window_sum -= numbers[left]
            left += 1

    if min_length == float("inf"):
        return 0

    return min_length