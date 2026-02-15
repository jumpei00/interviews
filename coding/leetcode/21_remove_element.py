from typing import List


def remove_element(nums: List[int], val: int) -> int:
    left = 0

    for right in range(len(nums)):
        if nums[right] != val:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    
    return left


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    print(remove_element(nums=nums, val=3))
    print(nums)

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(remove_element(nums=nums, val=2))
    print(nums)

    nums = []
    print(remove_element(nums=nums, val=0))
    print(nums)
