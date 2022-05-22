import sys
N, M = map(int,input().split())

pocket = {}
for i in range(1,N+1):
    pocket[sys.stdin.readline().rstrip()]=i

reverse_pocket= dict(map(reversed,pocket.items())) # value, key 바꾸기

for i in range(M):
    val = sys.stdin.readline().rstrip()
    if val.isalpha(): #알파벳이면(스페이스바 없는 문자열이어야함)
        print(pocket[val])
    else:
        print(reverse_pocket[int(val)])