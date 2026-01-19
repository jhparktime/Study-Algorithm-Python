import sys
string = sys.stdin.readline().rstrip()
stack = []
pairs = []
out = []

for i in range(len(string)) :
    if string[i] == '(' :
        stack.append(i)
    elif string[i] == ')' :
        pairs.append((stack.pop(), i))

for j in range(1, 2**(len(pairs))) :
    mask = format(j, f'0{len(pairs)}b')
    tmp = []
    for k in range(len(mask)) :  # range() 사용, 변수명 k로 변경
        if mask[k] == '1' :
            tmp.append(pairs[k][0])  # k는 이미 인덱스
            tmp.append(pairs[k][1])
    out.append(tmp)

# 결과 문자열들을 저장할 리스트
results = []

for i in range(len(out)):
    result = ''  # 각 경우의 결과 문자열
    for j in range(len(string)):
        if j not in out[i]:  # j가 제거할 인덱스에 없으면
            result += string[j]  # 문자 추가
    results.append(result)

# 중복 제거 및 사전순 정렬
results = sorted(set(results))

# 출력
for res in results:
    print(res) 