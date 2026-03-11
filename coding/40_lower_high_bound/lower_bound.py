from typing import List


def lower_bound(nums: List[int], x: int) -> int:
    N = len(nums)

    if not (nums[0] <= x and x <= nums[N - 1]):
        return -1

    if nums[0] == x:
        return 0

    ok, ng = N - 1, 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if x <= nums[mid]:
            ok = mid
        else:
            ng = mid

    return ok if nums[ok] == x else -1
