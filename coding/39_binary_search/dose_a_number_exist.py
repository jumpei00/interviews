from typing import List


def binary_search(nums: List[int], x: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == x:
            return mid

        if nums[mid] < x:
            low = mid + 1

        if x < nums[mid]:
            high = mid - 1

    return -1


def binary_search_rec(nums: List[int], x: int) -> int:
    def _binary_search(low: int, high: int) -> int:
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] == x:
            return mid

        if nums[mid] < x:
            return _binary_search(mid + 1, high)

        if x < nums[mid]:
            return _binary_search(low, mid - 1)

        return -1

    return _binary_search(0, len(nums) - 1)


if __name__ == "__main__":
    print(binary_search(nums=[1, 3, 4, 19, 20, 33, 53], x=4))
    print(binary_search(nums=[1, 3, 4, 19, 20, 33, 53], x=22))
