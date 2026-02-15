from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1

    return [left + 1, right + 1]


if __name__ == "__main__":
    print(two_sum(numbers=[2, 7, 11, 15], target=9))
    print(two_sum(numbers=[2, 3, 4], target=6))
    print(two_sum(numbers=[-1, 0], target=-1))
