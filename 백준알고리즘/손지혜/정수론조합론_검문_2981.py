N = int(input())

list = []
for i in range(N):
    list.append(int(input()))


Big = list[1]
Small = list[0]

while(Big%Small!=0):
    Big, Small= Small, Big%Small

#print(Small) #최대공약수

val=Small
cnt=0
idx=1

if(val==1):
    val = 2
    while(val<=list[1]):
        cnt=0
        nam=list[0]%val
        for i in list:
            if(i%val == nam):
                cnt+=1
            else:
                break
        if(cnt==N):
            print(val,end=' ')
        val +=1
else:
    while(val<=list[1]):
        cnt=0
        nam=list[0]%val
        for i in list:
            if(i%val == nam):
                cnt+=1
            else:
                break
        if(cnt==N):
            print(val,end=' ')
        idx+=1
        val = Small * idx
    