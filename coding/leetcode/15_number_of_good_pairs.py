from typing import List


def number_of_good_pairs(nums: List[int]) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count


if __name__ == "__main__":
    print(number_of_good_pairs([1, 2, 3, 1, 1, 3]))
    print(number_of_good_pairs([1, 1, 1, 1]))
    print(number_of_good_pairs([1, 2, 3]))
