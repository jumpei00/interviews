from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_map = defaultdict(int)
    t_map = defaultdict(int)

    for i in range(len(s)):
        s_map[s[i]] += 1

    for j in range(len(t)):
        t_map[t[j]] += 1

    for key in s_map:
        if s_map[key] != t_map[key]:
            return False

    return True


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat", "car"))
