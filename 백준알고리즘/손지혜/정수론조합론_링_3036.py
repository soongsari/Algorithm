import math

# def GCD(A,B):
#     Big = max(A,B)
#     Small = min(A,B)

#     while(Big%Small!=0):
#         Big,Small = Small,Big%Small

#     return Small


N = int(input())

arr = []
arr = list(map(int,input().split()))

first = arr[0]

for i in range(1,len(arr)):
    #gcd = GCD(arr[i],first)
    gcd = math.gcd(arr[i],first)
    print(f"{first//gcd}/{arr[i]//gcd}")