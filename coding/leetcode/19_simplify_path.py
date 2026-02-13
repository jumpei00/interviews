def simplify_path(path: str) -> str:
    dir_list = [dir_name for dir_name in path.split("/") if dir_name != ""]
    stack = []

    for dir_name in dir_list:
        if dir_name == ".":
            continue
        if dir_name == "..":
            if stack:
                stack.pop()
            continue
        else:
            stack.append(dir_name)

    return "/" + "/".join(stack)


if __name__ == "__main__":
    print(simplify_path("/home/"))
    print(simplify_path("/home//foo/"))
    print(simplify_path("/home/user/Documents/../Pictures"))
    print(simplify_path("/../"))
    print(simplify_path("/.../a/../b/c/../d/./"))
    print(simplify_path("/"))
