import sys

start = list(map(int, sys.stdin.readline().rstrip().split(':')))
end = list(map(int, sys.stdin.readline().rstrip().split(':')))

end[0] += 24
end[1] += 60
end[2] += 60

end = [end[i] - start[i] for i in range(len(end))]

if end[0] >= 24 :
    end[0] -= 24

if end[1] >= 60 :
    end[1] -= 60
else :
    end[0] -= 1

if end[2] >= 60 :
    end[2] -= 60
else :
    end[1] -= 1

print(f"{end[0]:02d}:{end[1]:02d}:{end[2]:02d}")