from typing import List


def maximum_subarray_sum(nums: List[int], k: int) -> int:
    n = len(nums)
    cumutative_nums = [0] * (n + 1)

    for i in range(n):
        cumutative_nums[i + 1] = cumutative_nums[i] + nums[i]

    max_sum = float("-inf")
    num_index = {}

    for i in range(n):
        for target in [nums[i] - k, nums[i] + k]:
            if target in num_index:
                max_sum = max(
                    max_sum, cumutative_nums[i + 1] - cumutative_nums[num_index[target]]
                )

        if (
            nums[i] in num_index
            and cumutative_nums[i] - cumutative_nums[num_index[nums[i]]] < 0
        ):
            num_index[nums[i]] = i
        elif nums[i] not in num_index:
            num_index[nums[i]] = i

    return max_sum if max_sum != float("-inf") else 0


if __name__ == "__main__":
    print(maximum_subarray_sum(nums=[1, 2, 3, 4, 5, 6], k=1))
    print(maximum_subarray_sum(nums=[-1, 3, 2, 4, 5], k=3))
    print(maximum_subarray_sum(nums=[-1, -2, -3, -4], k=2))
