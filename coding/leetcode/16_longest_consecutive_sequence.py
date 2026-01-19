from typing import List


def longest_consecutive_sequence(nums: List[int]) -> int:
    longest_consecutive_num = 0
    nums_set = set(nums)

    for num in nums:
        if num not in nums_set:
            continue

        nums_set.remove(num)
        consecutive_num = 1

        i = 1
        while num + i in nums_set:
            nums_set.remove(num + i)

            consecutive_num += 1
            i += 1

        j = 1
        while num - j in nums_set:
            nums_set.remove(num - j)

            consecutive_num += 1
            j += 1

        longest_consecutive_num = max(longest_consecutive_num, consecutive_num)

    return longest_consecutive_num


if __name__ == "__main__":
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(longest_consecutive_sequence([1, 0, 1, 2]))
