def find_max(nums):
    """
    Return the maximum value in a non-empty list of integers.
    """
    current_max = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > current_max:
            current_max = nums[i]

    return current_max


if __name__ == "__main__":
    nums = [3, 5, 2, 9, 1]
    print(find_max(nums))  # Expected output: 9

