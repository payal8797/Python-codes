def fun(a):
    cnt=[]
    c=[]
    d=[]
    
    for i in range(0,len(a)):
        b=[]
        for j in range(i,len(a)):
            b.append(a[j])
            if(len(b)%2==0):
                c=b[:len(b)//2]
                d=b[len(b)//2:]
                if(sorted(c)==sorted(d)):
                    cnt.append(len(b))  
                    #print(cnt) 
    #cnt.sort()
    print("aa:",cnt)

    if(cnt==[]):
        return 0
    else:
        return max(cnt)




if __name__=="__main__":
    y=input()
    a=list(y)
    print(fun(a))
