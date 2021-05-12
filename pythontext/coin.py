

def findFalseCoin(coins,start,n):       #在coins列表中下标为start开始的n个硬币中找假币
    if n==1:
        return start                    #查找范围中只剩下一个硬币，返回其下标
    nHalf = (n//2)                #nHalf为硬币数量的一半，下取整
    wL=sum(coins[start:start+nHalf])
    wR=sum(coins[start+nHalf:start+nHalf+nHalf])
    if wL<wR:
        return findFalseCoin(coins,start,nHalf)
    elif wR<wL:
        return findFalseCoin(coins,start+nHalf,nHalf)
    elif nHalf*2<n:
        return start+n-1
    else:
        return None
    
    
coins=[]
n=map(int,input().split(","))
for i in n:
    coins.append(i)
r=findFalseCoin(coins,0,len(coins))
print(("Fake coin:%d"%r) if r else "Fake coin is not found")
