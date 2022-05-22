import sys
N, M = map(int,input().split())
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))

diffA = A-B
diffB = B-A

print(len(diffA)+len(diffB))