import sys
K = int(input())

Xmaxlen=0
Ymaxlen=0
diff=0

arr = []
for i in range(6):
    D, L = map(int,input().split())
    arr.append((D,L))

    if D in (4,3) and Ymaxlen < L:
        Ymaxlen = L
    elif D in (1,2) and Xmaxlen < L:
        Xmaxlen = L

for i in range(6):
    if arr[i-1][0] == arr[(i+1)%6][0] and arr[i][0] == arr[(i+2)%6][0]:      
        diff = arr[i][1] * arr[(i+1)%6][1]
        break

print((Xmaxlen*Ymaxlen-diff)*K)