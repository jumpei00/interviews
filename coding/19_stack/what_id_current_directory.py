def current_dirname(path: str) -> str:
    parts = [part for part in path.split("/") if part != ""]
    stack = []

    for part in parts:
        if part == ".":
            continue
        if part == "..":
            stack.pop()
        else:
            stack.append(part)

    if not stack:
        return "root"

    return stack[-1]


if __name__ == "__main__":
    print(current_dirname("/home/"))  # Output: "home"
    print(current_dirname("/home"))  # Output: "home"
    print(current_dirname("/home/sakamoto"))  # Output: "sakamoto"
    print(current_dirname("/home/./sakamoto"))  # Output: "sakamoto"
    print(current_dirname("/home/../sakamoto"))  # Output: "sakamoto"
    print(current_dirname("/home/../sakamoto/."))  # Output: "sakamoto"
    print(current_dirname("/home/.."))  # Output: "root"
    print(current_dirname("/home/../sakamoto/../"))  # Output: "root"
    print(current_dirname("/"))  # Output: "root"
