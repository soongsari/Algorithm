def pibonachi(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return pibonachi(n-1) + pibonachi(n-2)

N = int(input())

print(pibonachi(N))