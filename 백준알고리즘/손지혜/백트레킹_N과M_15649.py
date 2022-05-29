
result = list()

def bfs(index,letter):

    if(index==M):
        result.append(letter)
        return

    for i in range(1,N+1):
        
        if(v[i]!=1):
            letter += " "+str(i)
            v[i]=1

            bfs(index+1,letter)
            v[i]=0
            letter = letter[:-2]

        

N, M = list(map(int,input().split()))
v = [0]*(N+1)


for i in range(1,N+1):
    v[i]=1
    bfs(1,str(i))
    v[i]=0

for i in result:
    print(i)