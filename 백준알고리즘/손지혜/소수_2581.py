def issosu(num):
    if num == 1:
        return False

    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    return True

M = int(input())
N = int(input())

array= []
for i in range(M,N+1):
    if issosu(i):
        array.append(i)

if len(array)==0:
    print(-1)
else:
    print(sum(array))
    print(min(array))
