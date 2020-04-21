if __name__=="__main__":
    y=[1,2,3,5,6]
    x1=y[0]
    x2=1
    for i in range(len(y)):
        x1=x1^y[i]
    for i in range(len(y)):
        x2=x2^i
    print(x1^x2)