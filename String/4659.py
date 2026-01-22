import sys

while True :
    string = sys.stdin.readline().rstrip()

    if string == 'end' :
        break

    check = 0 

    sub = 'aeiou'

    # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    if any(ch in sub for ch in string) :
        check += 1
    
    # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    if len(string) < 3 or not any(all(ch in sub for ch in string[i:i+3]) or all(ch not in sub for ch in string[i:i+3]) 
        for i in range(len(string) - 2)):
        check += 1


    # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    if len(string) < 2 or not any(string[i] == string[i+1] and string[i] not in 'eo' 
                                   for i in range(len(string) - 1)):
        check += 1

    if check == 3 :
        print(f"<{string}> is acceptable.")
    else :
        print(f"<{string}> is not acceptable.")