import math

def issosu(num):
    if num == 1:
        return False

    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

arr = [0]*(123456*2+1)
sosusum = 0
for i in range(2,123456*2+1):
 if issosu(i):
    sosusum+=1
    arr[i]=sosusum
 else:
    arr[i]=sosusum


while(True):
    result=0
    n = int(input())
    if n==0:
        break
    
    print(arr[2*n]-arr[n])