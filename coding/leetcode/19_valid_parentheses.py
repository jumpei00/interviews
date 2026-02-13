def is_valid(s: str) -> bool:
    stack = []
    converter = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
            continue

        if not stack:
            return False
        
        if converter[stack.pop()] != char:
            return False
    
    return not stack


if __name__ == "__main__":
    print(is_valid("()"))
    print(is_valid("()[]{}"))
    print(is_valid("(]"))
    print(is_valid("([])"))
    print(is_valid("([)]"))
