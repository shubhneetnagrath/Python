def count_subarrays(numbers, k):
    left = 0
    window_sum = 0
    count = 0

    for right in range(len(numbers)):
        window_sum += numbers[right]

        while window_sum > k:
            window_sum -= numbers[left]
            left += 1

        if window_sum == k:
            count += 1

    return count
