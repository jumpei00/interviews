def longest_repeating_char_cnt(s: str, k: int) -> int:
	longest_repeat_cnt = 0
	num_of_b = 0
	left = 0

	for r in range(len(s)):
		if s[r] == "B":
			num_of_b += 1
		
		while num_of_b > k:
			if s[left] == "B":
				num_of_b -= 1
			left += 1
		
		longest_repeat_cnt = max(longest_repeat_cnt, r - left + 1)
	
	return longest_repeat_cnt