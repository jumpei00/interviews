from typing import List


def get_averages(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    avg_nums = [-1] * n

    if 2 * k >= n:
        return avg_nums

    radius = 2 * k + 1
    cur_sum = 0

    for i in range(radius):
        cur_sum += nums[i]

    cur_sum = cur_sum
    avg_nums[k] = cur_sum // radius

    for i in range(k + 1, n - k):
        cur_sum -= nums[i - k - 1]
        cur_sum += nums[i + k]
        avg_nums[i] = cur_sum // radius

    return avg_nums


if __name__ == "__main__":
    print(get_averages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
    print(get_averages(nums=[100000], k=0))
    print(get_averages([8], k=100000))
    print(get_averages([2, 1], 1))
    print(get_averages([2, 1, 3], 1))
