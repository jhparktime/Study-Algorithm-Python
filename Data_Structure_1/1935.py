import sys

N = int(sys.stdin.readline().rstrip())
expr = sys.stdin.readline().rstrip()
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

stack = []

for char in expr:
    if 'A' <= char <= 'Z':  # 알파벳이면
        stack.append(arr[ord(char) - ord('A')])
    elif char in ['+', '-', '*', '/']:  # 연산자면
        b = stack.pop()
        a = stack.pop()
        
        if char == '+':
            stack.append(a + b)
        elif char == '-':
            stack.append(a - b)
        elif char == '*':
            stack.append(a * b)
        elif char == '/':
            stack.append(a / b)

print(f"{stack[0]:.2f}")