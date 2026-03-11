from typing import List


def upper_bound(nums: List[int], x: int) -> int:
    N = len(nums)

    if not (nums[0] <= x and x <= nums[N - 1]):
        return -1

    if nums[N - 1] == x:
        return N - 1

    ok, ng = 0, N - 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if nums[mid] <= x:
            ok = mid
        else:
            ng = mid

    return ok if nums[ok] == x else -1
