def getMass():
    x=input()
    res=[list(map(int,list(x)))]
    for _ in range(len(x)-1):
        res.append(list(map(int,list(input()))))
def getMaxInMatrix(m):
    maxN=0
    for i in m:
#        print(i)
        r=max(i)
        if r>maxN: maxN=r
    return maxN
def findItem(m,i):
    y=0
    for s in m:
        if i in s: return y,s.index(i)
        y+=1
def findNeightBors(pos):
    neib=[]
    neib.append([pos[0]+1, pos[1]])
    neib.append([pos[0]-1, pos[1]])
    neib.append([pos[0], pos[1]+1])
    neib.append([pos[0], pos[1]-1])
    return neib

def deleteMin0Max3(n):
    x=n
    for a in x[:]:
        for b in a[:]:
            if b < 0 or b > 2:
                x.remove(a)
    return x


def findMaxFromNeightbors(mas,pos):
    neib=findNeightBors(pos)
    neib=deleteMin0Max3(neib)
    maxPos=[0,0]
    maxZN=0
    for i in neib:
        if mas[i[0]][i[1]]>maxZN:
            maxZN=mas[i[0]][i[1]]
            maxPos=i[:]
    setZero(maxPos)
    return maxZN,maxPos
def setZero(pos):
    global res
    res[pos[0]][pos[1]]=0
res=[[4, 5, 6],[7, 2, 3],[1, 8, 9]]
#print(*res,sep="\n",end="\n\n\n")
#findMaxFromNeightbors(res,[1,1])
#print(*res,sep="\n")

print(*res,sep="\n",end="\n\n\n")
print(findItem(res,9))
posit=findItem(res,getMaxInMatrix(res))
setZero(posit)
print(*res,sep="\n",end="\n\n\n")
rr="9"
while res!=[[0,0,0],[0,0,0],[0,0,0]]:
    mt=findMaxFromNeightbors(res,posit)
    rr+=str(mt[0])
    print(res)
    posit=mt[1]
p