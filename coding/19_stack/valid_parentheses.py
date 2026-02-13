def is_valid_parentheses(s: str) -> bool:
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)
        elif not stack:
            return False
        else:
            stack.pop()
    
    return len(stack) == 0

if __name__ == "__main__":
    print(is_valid_parentheses("()")) # Output: True
    print(is_valid_parentheses("(())")) # Output: True
    print(is_valid_parentheses("(())()")) # Output: True
    print(is_valid_parentheses("(())(")) # Output: False
    print(is_valid_parentheses("(()")) # Output: False
    print(is_valid_parentheses("())")) # Output: False
