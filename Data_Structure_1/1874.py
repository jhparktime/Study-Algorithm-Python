import sys

N = int(sys.stdin.readline().rstrip())

seq = []  # 목표 수열
for _ in range(N):
    seq.append(int(sys.stdin.readline().rstrip()))

stack = []  # 스택
result = []  # 출력할 연산들
current = 1  # 다음에 push할 숫자
idx = 0  # 목표 수열의 현재 인덱스

while idx < N:
    target = seq[idx]  # 목표 숫자
    
    # 목표 숫자까지 push
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1
    
    # 스택의 top이 목표 숫자와 같으면 pop
    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
        idx += 1
    else:
        # 불가능한 경우
        print('NO')
        exit()

# 가능한 경우 결과 출력
for op in result:
    print(op)

