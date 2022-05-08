
arr=[0]*12000

def d(n):

    if(n> 10000):
        return
    val = n + sum(list(map(int,str(n)))) #자릿수 더하기
    if(arr[val]==1): #중복된 숫자는 더이상 확인하지 않음
        return
    arr[val]=1 #계산 된 결과가 있는 건에 1표시
    return d(val)

i = 1
j = 1
while(i<=10000):
    d(i)
    if arr[i]!=1:
        print(i)
    i+=1





