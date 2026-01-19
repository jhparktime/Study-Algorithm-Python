import sys

inst = sys.stdin.readline().rstrip()
stack = []
block = 0

for i in range(len(inst)) :
    if inst[i] == '(' and inst[i+1] != ')' :
        stack.append('(')

    elif inst[i] == '(' and inst[i+1] == ')' :
        block += len(stack)

    elif inst[i] == ')' and inst[i-1] == '(' :
        pass

    elif inst[i] == ')' and inst[i-1] != '(' : 
        stack.pop()
        block += 1

print(block)
    