def longest_ones(numbers, k):
    left = 0
    zeros = 0
    max_length = 0

    for right in range(len(numbers)):
        if numbers[right] == 0:
            zeros += 1

        while zeros > k:
            if numbers[left] == 0:
                zeros -= 1
            left += 1

        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length

    return max_length