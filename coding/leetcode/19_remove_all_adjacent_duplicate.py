def remove_duplicates(s: str) -> str:
    stack = []

    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
            continue

        while stack and stack[-1] == c:
            stack.pop()

    return "".join(stack)


if __name__ == "__main__":
    print(remove_duplicates("abbaca"))
    print(remove_duplicates("azxxzy"))
