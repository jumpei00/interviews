from typing import List


def quick_sort(nums: List[int]):
    def _quick_sort(nums: List[int], left: int, right: int):
        if left >= right:
            return

        partition_index = partition(nums, left, right)
        _quick_sort(nums, left, partition_index - 1)
        _quick_sort(nums, partition_index + 1, right)

    _quick_sort(nums, 0, len(nums) - 1)


def partition(nums: List[int], left: int, right: int) -> int:
    pivot_index = right
    pivot_value = nums[pivot_index]

    i = left
    for j in range(left, right):
        if nums[j] < pivot_value:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
    return pivot_index


if __name__ == "__main__":
    nums = [5, 2, 1, 4, 3]
    quick_sort(nums)
    print(nums)
