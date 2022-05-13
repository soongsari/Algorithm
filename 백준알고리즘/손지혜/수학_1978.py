N = int(input())

def issosu(num):
    if num == 1:
        return 0

    for i in range(2,int(num/2)+1):
        if num%i==0:
            return 0
    return 1

result=0

arr = map(int,input().split())

for i in arr:
    result += issosu(i)

print(result)