def fun(x,y):   
    if(x==0 and y==0):
        return -1
    elif(x!=0 and y==0):
        return 1
    elif(y<0):
        return float((1/x)*fun(x,y+1))
    else:
        return x*fun(x,y-1)


if __name__=="__main__":
    x=int(input())
    y=int(input())
    print(fun(x,y))
