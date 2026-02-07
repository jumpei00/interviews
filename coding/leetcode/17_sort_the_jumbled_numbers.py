from typing import List
from functools import cmp_to_key
from collections import defaultdict


def sort_the_jumbled_numbers(mapping: List[int], nums: List[int]) -> List[int]:
    def compare(v1: int, v2: int) -> int:
        jumbled_v1 = 0
        if v1 == 0:
            jumbled_v1 = mapping[v1]

        i = 0
        while v1 > 0:
            n = v1 % 10
            jumbled_v1 += mapping[n] * 10**i
            v1 = v1 // 10
            i += 1

        jumbled_v2 = 0
        if v2 == 0:
            jumbled_v2 = mapping[v2]

        j = 0
        while v2 > 0:
            n = v2 % 10
            jumbled_v2 += mapping[n] * 10**j
            v2 = v2 // 10
            j += 1

        if jumbled_v1 == jumbled_v2:
            return 0

        if jumbled_v1 < jumbled_v2:
            return -1

        return 1

    nums.sort(key=cmp_to_key(compare))
    return nums


def sort_the_jumbled_numbers_v2(mapping: List[int], nums: List[int]) -> List[int]:
    compare_map = defaultdict(int)

    for num in nums:
        if num == 0:
            compare_map[num] = mapping[num]
            continue

        jumbled_num = 0
        temp = num
        i = 0
        while temp > 0:
            n = temp % 10
            jumbled_num += mapping[n] * 10**i
            temp = temp // 10
            i += 1

        compare_map[num] = jumbled_num

    nums.sort(key=lambda n: compare_map[n])
    return nums

def sort_the_jumbled_numbers_v3(mapping: List[int], nums: List[int]) -> List[int]:
    def compare(num: int) -> int:
        if num == 0:
            return mapping[num]
        
        jumbled_num = 0
        i = 0
        while num > 0:
            n = num % 10
            jumbled_num += mapping[n] * 10 ** i
            num = num // 10
            i += 1
        
        return jumbled_num
    
    nums.sort(key=compare)
    return nums


if __name__ == "__main__":
    print(sort_the_jumbled_numbers_v3([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]))
    print(sort_the_jumbled_numbers_v3([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123]))
    print(
        sort_the_jumbled_numbers_v3(
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )
    )
