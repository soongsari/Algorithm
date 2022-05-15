
def star(n):

    if n==1:
        return

    for it in range(0,N//n):
        for jt in range(0,N//n):
            for i in range(n//3,2*n//3):
                for j in range(n//3,2*n//3):
                    arr[i+(it*n)][j+(jt*n)]=' '

    star(n//3)



N = int(input())

#2차원 배열 선언
arr = [["*"] * N for _ in range(N)]

star(N)

for i in range(N):
    for j in range(N):
        print(arr[i][j],end='')
    print()