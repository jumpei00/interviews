def is_subsequence(s: str, t: str) -> bool:
    if s == "":
        return False

    s_index = 0

    for t_index in range(len(t)):
        if s[s_index] == t[t_index]:
            s_index += 1

        if s_index >= len(s):
            return True

    return False


def is_subsequence_v2(s: str, t: str) -> bool:
    s_index, t_index = 0, 0

    while s_index < len(s) and t_index < len(s):
        if s[s_index] == t[t_index]:
            s_index += 1
        t_index += 1

    return s_index == len(s)


if __name__ == "__main__":
    print(is_subsequence(s="abc", t="ahbgdc"))
    print(is_subsequence(s="axc", t="ahbgdc"))
    print(is_subsequence(s="", t="ahbgdc"))
    print(is_subsequence(s="b", t="c"))
