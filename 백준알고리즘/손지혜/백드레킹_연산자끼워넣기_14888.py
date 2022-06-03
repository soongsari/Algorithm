from ast import operator


N = int(input())
arr = list(map(int,input().split()))
opr = list(map(int,input().split()))

result = []

def bfs(index,res):
    
    if index == N:
        result.append(res)


    if index < N and opr[0] > 0:
            opr[0]-=1
            bfs(index+1, res+arr[index])
            opr[0]+=1


    if index < N and opr[1] > 0:
        opr[1]-=1
        bfs(index+1, res-arr[index])
        opr[1]+=1


    if index < N and opr[2] > 0:
        opr[2]-=1
        bfs(index+1,res*arr[index])
        opr[2]+=1


    if index < N and opr[3] > 0:
        opr[3]-=1
        bfs(index+1,int(res/arr[index]))
        opr[3]+=1

bfs(1,arr[0])
print(max(result))
print(min(result))