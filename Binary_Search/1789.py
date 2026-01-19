import sys

N = int(sys.stdin.readline().rstrip())

i = 1

while (i * (i + 1)) // 2 <= N:
    i += 1

print(i - 1)