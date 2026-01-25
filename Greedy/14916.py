import sys

reward = int(sys.stdin.readline().rstrip())

i = 1
a, b = 0, 0

if reward == 2 : 
    print(1)
elif reward == 4 : 
    print(2)
elif reward >= 5 : 
    while (5 * i <= reward):
        if ((reward - (5*i)) % 2 == 0) :
            a = i   
        i += 1
    
    b = (reward - (5 * a)) // 2
    print(a+b)
else :
    print(-1)
