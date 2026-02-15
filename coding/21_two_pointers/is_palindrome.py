def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("level"))  # Output: True
    print(is_palindrome("interviewcat"))  # Output: False(is_palindrome())
