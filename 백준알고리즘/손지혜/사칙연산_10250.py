import math
T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
    
    mok = math.ceil(N/H)
    
    print(f"{N-(H*(mok-1))}{str(math.ceil(N/H)).zfill(2)}")

