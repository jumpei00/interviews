def score_of_parentheses(s: str) -> int:
    stack = []

    for i in range(len(s)):
        if s[i] == "(":
            stack.append("x")
        else:
            if len(stack) >= 1 and type(stack[-1]) is int:
                v = stack.pop()
                stack.pop()
                stack.append(v * 2)
            else:
                stack.pop()
                stack.append(1)

            if len(stack) >= 2 and type(stack[-1]) is int and type(stack[-2]) is int:
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)

    return stack.pop()


if __name__ == "__main__":
    print(score_of_parentheses("()"))
    print(score_of_parentheses("(())"))
    print(score_of_parentheses("()()"))
