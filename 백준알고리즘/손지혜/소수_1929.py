import math

def issosu(num):
    if num == 1:
        return False

    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

M,N = map(int,input().split())

for i in range(M,N+1):
    if issosu(i):
        print(i)
