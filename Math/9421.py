import sys

N = int(sys.stdin.readline().rstrip())

# 1. 소수 구하기 (에라토스테네스의 체)
is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, N + 1):
    if is_prime[i] == False:
        continue
    for j in range(i * 2, N + 1, i):
        is_prime[j] = False

# 2. 상근수인지 확인하는 함수
# 자리 숫자 제곱의 합을 반복해서 1이 되면 상근수, 같은 수가 다시 나오면 아님
def is_sangen(num):
    seen = []
    cur = num

    while cur != 1:
        # 이전에 나왔던 수면 사이클 -> 상근수 아님
        if cur in seen:
            return False
        seen.append(cur)

        # 자리 숫자 제곱의 합 구하기
        next_val = 0
        s = str(cur)
        for i in range(len(s)):
            digit = int(s[i])
            next_val += digit * digit
        cur = next_val

    return True

# 3. 소수이면서 상근수인 수 출력
for p in range(2, N + 1):
    if is_prime[p] == True:
        if is_sangen(p) == True:
            print(p)
