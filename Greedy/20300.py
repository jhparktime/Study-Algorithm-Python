import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()  

answer = 0

if N % 2 == 1 :  
    answer = arr[-1]          
    arr = arr[:-1]           

for i in range(len(arr) // 2) :
    s = arr[i] + arr[-1 - i]  
    if s > answer :
        answer = s

print(answer)