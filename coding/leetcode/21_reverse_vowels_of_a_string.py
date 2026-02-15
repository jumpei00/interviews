def reverse_vowels(s: str) -> str:
    str_list = list(s)
    left, right = 0, len(s) - 1
    vowels_set = {"a", "e", "i", "o", "u"}

    while left < right:
        while left < right and s[left].lower() not in vowels_set:
            left += 1

        while left < right and s[right].lower() not in vowels_set:
            right -= 1

        if left < right:
            str_list[left] = s[right]
            str_list[right] = s[left]

            left += 1
            right -= 1

    return "".join(str_list)


if __name__ == "__main__":
    print(reverse_vowels("IceCreAm"))
    print(reverse_vowels("leetcode"))
    print(reverse_vowels("t"))
    print(reverse_vowels("e"))
    print(reverse_vowels("te"))
    print(reverse_vowels("tey"))
    print(reverse_vowels("tye"))
    print(reverse_vowels("eyt"))
    print(reverse_vowels("a a"))
    print(reverse_vowels("etyta"))
    print(reverse_vowels("eta"))
