
arr = []
def hanoi(n,a,c,b): #원반개수, 목표, 보조
    if(n==1):
        arr.append(f"{a} {c}")  #시작 -> 목표
        return
    
    hanoi(n-1,a,b,c) # 원반개수-1,시작, 보조, 목표
    arr.append(f"{a} {c}") #시작 -> 목표
    hanoi(n-1,b,c,a) # 원반개수-1,보조, 목표, 시작

N = int(input())

hanoi(N,1,3,2)
print(len(arr))
print("\n".join(arr))