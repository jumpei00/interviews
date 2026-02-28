# 1. windowの右端を進める
# 2. sumがtarget以上になるまで進める
# 3. windowを縮小させる
# 4. sumがtarget以上であれば評価する
# 5. sumがtargetより小さければストップする

from typing import List


def min_subarray_len(target: int, nums: List[int]) -> int:
    minimum_subarray_len = len(nums) + 1
    sum = 0
    left_index = 0

    for i in range(len(nums)):
        sum += nums[i]

        while sum >= target and left_index <= i:
            minimum_subarray_len = min(minimum_subarray_len, i - left_index + 1)

            sum -= nums[left_index]
            left_index += 1

    return minimum_subarray_len if left_index != 0 else 0


if __name__ == "__main__":
    print(min_subarray_len(target=7, nums=[2, 3, 1, 2, 4, 3]))
    print(min_subarray_len(target=4, nums=[1, 4, 4]))
    print(min_subarray_len(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
    print(min_subarray_len(target=1, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
