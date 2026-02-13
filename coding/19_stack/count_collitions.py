def count_collisions(directions: str) -> int:
    stack = []
    collision = 0

    for d in directions:
        if not stack:
            stack.append(d)
            continue

        if d == "R":
            stack.append(d)
            continue

        if d == "L" and stack[-1] == "R":
            collision += 2
            stack.pop()
            d = "S"
        elif d == "L" and stack[-1] == "S":
            collision += 1
            stack.pop()
            d = "S"

        while stack and stack[-1] == "R" and d == "S":
            collision += 1
            stack.pop()

        stack.append(d)

    return collision


if __name__ == "__main__":
    print(count_collisions("RLRS"))  # Output: 3
    print(count_collisions("LLRR"))  # Output: 0
