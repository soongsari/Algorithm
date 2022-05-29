result = list()

def bfs(index,letter):


    if(index==M):
        result.append(letter)
        return

    for i in range(1,N+1):
        
        if(v[i]!=1):
            letter += " "+str(i)
            bfs(index+1,letter)
            letter = letter[:-2]
        
N, M = list(map(int,input().split()))
v = [0]*(N+1)

for i in range(1,N+1):
    bfs(1,str(i))

for i in result:
    print(i)