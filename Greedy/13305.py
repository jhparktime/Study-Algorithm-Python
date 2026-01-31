import sys

N = int(sys.stdin.readline().rstrip())
dist = list(map(int, sys.stdin.readline().rstrip().split()))
fuel = list(map(int, sys.stdin.readline().rstrip().split()))

# 접근: 왼쪽→오른쪽으로 가면서 "지금까지 본 가장 싼 가격"으로만 기름 구매
min_price = fuel[0]
total = 0

for i in range(N - 1):
    if fuel[i] < min_price:
        min_price = fuel[i]
    total += min_price * dist[i]

print(total)
