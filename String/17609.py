import sys

def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def check_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1):
                return 1
            else:
                return 2
    
    return 0

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    string = sys.stdin.readline().rstrip()
    print(check_palindrome(string))