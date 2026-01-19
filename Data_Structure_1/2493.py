import sys

N = int(sys.stdin.readline().rstrip())
heights = list(map(int, sys.stdin.readline().split()))  # 공백으로 분리 후 정수 변환

stack = []  # (인덱스, 높이) 저장
result = []

for i in range(len(heights)):
    # 스택에서 현재 높이보다 작은 것들을 제거
    while stack and stack[-1][1] < heights[i]:
        stack.pop()
    
    # 스택이 비어있으면 신호를 받을 탑이 없음 (0)
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0])  # 가장 가까운 높은 탑의 인덱스
    
    # 현재 탑을 스택에 추가
    stack.append((i+1, heights[i]))  # (인덱스, 높이) 저장

print(*result)  # 공백으로 구분하여 출력
            

