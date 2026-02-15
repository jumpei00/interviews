def max_score(s: str) -> int:
    n = len(s)
    cumulative_zero_nums = [0] * (n + 1)
    cumulative_one_nums = [0] * (n + 1)

    for i in range(n):
        cumulative_zero_nums[i + 1] = cumulative_zero_nums[i]
        if s[i] == "0":
            cumulative_zero_nums[i + 1] += 1

        cumulative_one_nums[i + 1] = cumulative_one_nums[i]
        if s[i] == "1":
            cumulative_one_nums[i + 1] += 1

    max_score = 0
    for i in range(n - 1):
        left_score = cumulative_zero_nums[i + 1] - cumulative_zero_nums[0]
        right_score = cumulative_one_nums[n] - cumulative_one_nums[i + 1]
        max_score = max(max_score, left_score + right_score)

    return max_score


if __name__ == "__main__":
    print(max_score("011101"))
    print(max_score("00111"))
    print(max_score("1111"))
