from collections import defaultdict


def length_of_longest_substring(s: str) -> int:
    counter = defaultdict(int)
    longest_substring_count = 0
    left_index = 0

    for i in range(len(s)):
        counter[s[i]] += 1

        while counter[s[i]] >= 2:
            counter[s[left_index]] -= 1
            left_index += 1

        longest_substring_count = max(longest_substring_count, i - left_index + 1)

    return longest_substring_count


if __name__ == "__main__":
    print(length_of_longest_substring(s="abcabcbb"))
    print(length_of_longest_substring(s="bbbbb"))
    print(length_of_longest_substring(s="pwwkew"))
    print(length_of_longest_substring(s=""))
    print(length_of_longest_substring(s="abbca"))
    print(length_of_longest_substring(s="tmmzuxt"))
