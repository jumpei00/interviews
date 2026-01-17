from typing import List


def two_sum_v1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    print(two_sum_v1([2, 7, 11, 15], 9))
    print(two_sum_v1([3, 2, 4], 6))
    print(two_sum_v1([3, 3], 6))
