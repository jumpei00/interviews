from typing import List


def find_maximum_average_subarray(nums: List[int], k: int) -> float:
    cur_sum = 0
    max_sum = 0

    for i in range(k):
        cur_sum += nums[i] / k

    max_sum = cur_sum

    for i in range(k, len(nums)):
        cur_sum -= nums[i - k] / k
        cur_sum += nums[i] / k
        max_sum = max(max_sum, cur_sum)

    return max_sum


if __name__ == "__main__":
    print(find_maximum_average_subarray(nums=[1, 12, -5, -6, 50, 3], k=4))
    print(find_maximum_average_subarray(nums=[5], k=1))
