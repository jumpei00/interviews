from typing import List


def find_gcd(nums: List[int]) -> int:
    def _find_gcd(a: int, b: int) -> int:
        r = a % b
        if r == 0:
            return b
        return _find_gcd(b, r)

    return _find_gcd(max(nums), min(nums))

if __name__ == "__main__":
    print(find_gcd(nums=[2, 5, 6, 9, 10]))
    print(find_gcd(nums=[7, 5, 6, 8, 3]))
    print(find_gcd(nums=[3, 3]))