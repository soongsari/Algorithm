def dfs(index):
    if len(s) == m:
        print(" ".join(map(str, s)))
    else:
        for i in range(1, n+1):
            if len(s)==0 or i >=s[-1]:
                s.append(i)
                dfs(index+1)
                s.pop()


n, m = map(int, input().split())
s = []

dfs(1)