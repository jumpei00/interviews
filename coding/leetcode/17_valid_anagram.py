def valid_anagram(s: str, t: str) -> bool:
    return "".join(sorted(s)) == "".join(sorted(t))


if __name__ == "__main__":
    print(valid_anagram("anagram", "nagaram"))
    print(valid_anagram("rat", "car"))
    print(valid_anagram("a", "ab"))
