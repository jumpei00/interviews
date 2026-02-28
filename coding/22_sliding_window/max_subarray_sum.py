from typing import List


def get_max_sum_in_windown(nums: List[int], k: int) -> int:
    cur_sum = 0
    max_sum = 0

    for i in range(k):
        cur_sum += nums[i]

    max_sum = cur_sum

    for i in range(k, len(nums)):
        cur_sum -= nums[i - k]
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)

    return max_sum


if __name__ == "__main__":
    print(get_max_sum_in_windown(nums=[7, 1, 5, 9, 6, 4], k=3))
