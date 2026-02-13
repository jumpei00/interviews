from typing import List


def min_operations(logs: List[str]) -> int:
    stack = []

    for log in logs:
        if log == "./":
            continue
        if log == "../":
            if not stack:
                continue
            stack.pop()
        else:
            stack.append(log)

    return len(stack)


if __name__ == "__main__":
    print(min_operations(["d1/", "d2/", "../", "d21/", "./"]))
    print(min_operations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
    print(min_operations(["d1/", "../", "../", "../"]))
    print(min_operations(["./", "../", "./"]))
