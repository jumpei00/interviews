from copy import deepcopy


def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    ans = []

    subset = []

    def rec(i):
        if i == n:
            ans.append(deepcopy(subset))
            return

        subset.append(nums[i])
        rec(i + 1)

        subset.pop()
        rec(i + 1)

        return

    rec(0)
    return ans


if __name__ == "__main__":
    print(subsets(nums=[1, 2, 3]))
