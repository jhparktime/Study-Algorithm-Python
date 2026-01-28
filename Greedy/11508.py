import sys

N = int(sys.stdin.readline().rstrip())
prices = []

for _ in range(N):
    prices.append(int(sys.stdin.readline().rstrip()))

prices.sort(reverse=True)

answer = 0

for i, price in enumerate(prices):
    if i % 3 != 2:
        answer += price

print(answer)