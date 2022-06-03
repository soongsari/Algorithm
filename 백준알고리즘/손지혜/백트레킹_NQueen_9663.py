
N = int(input())

cnt=0
arr = list()


def check(row,col):
    for i in range(len(arr)):
        if col==arr[i] or abs(col-arr[i])== abs(i-row):
            return False
    return True

def bfs(row):
    global cnt

    if row==N:
        cnt+=1
        return

    for col in range(N):
        if(check(row,col)):
            arr.append(col)
            bfs(row+1)
            arr.pop()

bfs(0)
print(cnt)