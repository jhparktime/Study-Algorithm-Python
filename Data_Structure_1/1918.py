import sys 

string = sys.stdin.readline().rstrip()

stack = []  # 연산자 스택
result = []  # 결과 (후위 표기식)

# 연산자 우선순위
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

for i in range(len(string)):
    if string[i].isalpha(): 
        # 피연산자는 바로 결과에 추가
        result.append(string[i])
    else:
        if string[i] == '(':
            # 여는 괄호는 스택에 push
            stack.append(string[i])
        elif string[i] == ')':
            # 닫는 괄호: '('를 만날 때까지 pop
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # '(' 제거
        elif string[i] in ['*', '/']:
            # 높은 우선순위 연산자
            # 스택의 top이 같은 우선순위 이상이면 pop
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[string[i]]:
                result.append(stack.pop())
            stack.append(string[i])
        else:  # '+', '-'
            # 낮은 우선순위 연산자
            # 스택의 top이 같은 우선순위 이상이면 pop
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[string[i]]:
                result.append(stack.pop())
            stack.append(string[i])

# 스택에 남은 연산자 모두 pop
while stack:
    result.append(stack.pop())

# 결과 출력
print(''.join(result))
