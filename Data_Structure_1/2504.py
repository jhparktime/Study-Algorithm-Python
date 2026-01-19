import sys

string = sys.stdin.readline().rstrip()
stack = []
tmp = int(0)
out = int(0)

for i in range(len(string)) : 
    if string[i] == '(':
        stack.append('(')
    
    elif string[i] == '[' :
        stack.append('[')

    elif string[i] == ')' :
        if not stack :
            print(0)
            exit()
        
        total = 0
        while stack and isinstance(stack[-1], int) : 
            total += stack.pop()
        
        if not stack or stack[-1] != '(' :
            print(0)
            exit()
        
        stack.pop()
        if total == 0 :
            stack.append(2)
        else :
            stack.append(2 * total)

    elif string[i] == ']' :
            if not stack :
                print(0)
                exit()
            
            total = 0
            while stack and isinstance(stack[-1], int) : 
                total += stack.pop()
            
            if not stack or stack[-1] != '[' :
                print(0)
                exit()
            
            stack.pop()
            if total == 0 :
                stack.append(3)
            else :
                stack.append(3 * total)

if all(isinstance(x, int) for x in stack) :
    print(sum(stack))
else:
    print(0)