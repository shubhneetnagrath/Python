def max_subarray_length(numbers, target):
    left = 0
    window_sum = 0
    max_length = 0

    for right in range(len(numbers)):
        window_sum += numbers[right]

        while window_sum > target:
            window_sum -= numbers[left]
            left += 1

        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length

    return max_length