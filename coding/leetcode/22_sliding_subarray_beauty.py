from typing import List
from collections import defaultdict


def get_subarray_beauty(nums: List[int], k: int, x: int) -> List[int]:
    counter = defaultdict(int)

    def find_beauty():
        count = 0
        for num in range(-50, 0):
            count += counter[num]
            if count >= x:
                return num
        return 0

    subarray = []

    for i in range(k):
        counter[nums[i]] += 1

    subarray.append(find_beauty())

    for i in range(k, len(nums)):
        counter[nums[i - k]] -= 1
        counter[nums[i]] += 1
        subarray.append(find_beauty())

    return subarray


if __name__ == "__main__":
    print(get_subarray_beauty(nums=[1, -1, -3, -2, 3], k=3, x=2))
    print(get_subarray_beauty(nums=[-1, -2, -3, -4, -5], k=2, x=2))
    print(get_subarray_beauty(nums=[-3, 1, 2, -3, 0, -3], k=2, x=1))
    print(get_subarray_beauty(nums=[-2, -2, -2, -1, -1, -2], k=5, x=3))
