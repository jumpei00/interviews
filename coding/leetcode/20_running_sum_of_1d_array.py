from typing import List

def running_sum(nums: List[int]) -> List[int]:
	cumulative_nums = [0]*(len(nums) + 1)

	for i, num in enumerate(nums):
		cumulative_nums[i+1] = cumulative_nums[i] + num
	
	return cumulative_nums[1:]

if __name__ == "__main__":
    print(running_sum([1, 2, 3, 4]))
    print(running_sum([1, 1, 1, 1, 1]))
    print(running_sum([3, 1, 2, 10, 1]))