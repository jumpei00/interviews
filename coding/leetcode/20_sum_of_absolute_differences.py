from typing import List


def get_sum_absolute_differences(nums: List[int]) -> List[int]:
    n = len(nums)
    cumulative_nums = [0] * (n + 1)

    for i in range(n):
        cumulative_nums[i + 1] = cumulative_nums[i] + nums[i]

    results = []
    for i in range(n):
        left_sum = nums[i] * i - (cumulative_nums[i] - cumulative_nums[0])
        right_sum = (cumulative_nums[n] - cumulative_nums[i + 1]) - nums[i] * (
            n - i - 1
        )
        results.append(left_sum + right_sum)

    return results


if __name__ == "__main__":
    print(get_sum_absolute_differences([2, 3, 5]))
    print(get_sum_absolute_differences([1, 4, 6, 8, 10]))
