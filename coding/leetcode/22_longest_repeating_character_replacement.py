# ABCCDBC, k=2
# 1. Aに変えられるか？を検証
# 2. Aじゃないものをカウント
# ABABBBB, k=2


def character_replacement(s: str, k: int) -> int:
    all_char = set(s)
    longest_rep_cnt = 0

    for char in all_char:
        left_index = 0
        rep_cnt = 0

        for i in range(len(s)):
            if s[i] != char:
                rep_cnt += 1

            while rep_cnt > k:
                if s[left_index] != char:
                    rep_cnt -= 1

                left_index += 1

            longest_rep_cnt = max(longest_rep_cnt, i - left_index + 1)

    return longest_rep_cnt


if __name__ == "__main__":
    print(character_replacement(s="ABAB", k=2))
    print(character_replacement(s="AABABBA", k=1))
