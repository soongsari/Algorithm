N = int(input())
dic = dict.fromkeys(list(map(int,input().split())),1)  #list to dictionary. value값은 1

M = int(input())
arr = list(map(int,input().split()))

for i in range(M):
    if arr[i] in dic:  #키가 존재하냐
        print(1,end=' ')
    else:
        print(0,end=' ')
