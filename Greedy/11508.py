import sys

N = int(sys.stdin.readline().rstrip())
prices = []

for _ in range(N):
    prices.append(int(sys.stdin.readline().rstrip()))

# 가장 비싼 것부터 정렬
prices.sort(reverse=True)

answer = 0

for i, price in enumerate(prices):
    # 0,1,3,4,6,7,... 번째는 더하고
    # 2,5,8,... 번째(매 3번째)는 공짜
    if i % 3 != 2:
        answer += price

print(answer)