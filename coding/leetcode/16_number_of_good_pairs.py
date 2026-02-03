from typing import List
from collections import defaultdict

def number_of_good_pairs(nums: List[int]) -> int:
	counter_map = defaultdict(int)

	for num in nums:
		counter_map[num] += 1
	
	count = 0
	for counter in counter_map.values():		
		count += counter * (counter - 1) // 2
	
	return count

if __name__ == '__main__':
	print(number_of_good_pairs([1, 2, 3, 1, 1, 3]))
	print(number_of_good_pairs([1, 1, 1, 1]))
	print(number_of_good_pairs([1, 2, 3]))