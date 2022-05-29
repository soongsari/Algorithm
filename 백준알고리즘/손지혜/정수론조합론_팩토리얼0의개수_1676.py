import math

N = int(input())

cnt=0
for i in list(str(math.factorial(N)))[::-1]:
    if(i=='0'):
        cnt+=1
    else:
        break
print(cnt)