import sys 

N, M = map(int, sys.stdin.readline().rstrip().split())

dictionary = {}

for i in range(N) : 
    tmp = sys.stdin.readline().rstrip()
    if len(tmp) >= M :
        if tmp in dictionary.keys() :
            dictionary[tmp] += 1
        else : 
            dictionary[tmp] = 1
    else :
        continue

sorted_words = sorted(dictionary.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)


