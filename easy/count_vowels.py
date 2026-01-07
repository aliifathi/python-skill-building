def count_vowels(s):
    """
    Count vowels (a, e, i, o, u) in a string, case-insensitive.
    """
    vowels = "aeiou"
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1

    return count


if __name__ == "__main__":
    s = "Interview"
    print(count_vowels(s))  # Expected output: 4

