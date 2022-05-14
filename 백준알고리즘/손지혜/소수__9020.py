import math

def issosu(num):
    if num == 1:
        return False

    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

# 범위가 작으니, 소수인것 먼저 표시(아니면 시간초과 남)
array= [0]*10001
for i in range(2,10001):
    if issosu(i):
        array[i]=1

T = int(input())

for i in range(T):
    N = int(input())
    A = 0
    B = 0
    for j in range(2,int(N/2)+1):
        if array[j]==1:
            if array[N-j]==1:
                A = j
                B = N-j
    print(A,B)
