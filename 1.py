if __name__=="__main__":
    y=str(input())
    res=list(y)
    #print(res)
    j=len(res)-1
    i=0
    while(i<=j):
        #print(i, res[i], j, res[j])
        #print(i,j)
        if(((res[i]>='a' and res[i]<='z') or (res[i]>='A' and res[i]<='Z')) and ((res[j]>='a' and res[j]<='z') or (res[j]>='A' and res[j]<='Z'))):
            res[i],res[j]=res[j],res[i]
            i=i+1
            j=j-1
            #print('here')
        elif(((res[i]>='a' and res[i]<='z') or (res[i]>='A' and res[i]<='Z')) and ((res[j]<'a' or res[j]>'z') or (res[j]<'A' or res[j]>'Z'))):
            j=j-1
            #print('here1')
        elif(((res[i]<'a' or res[i]>'z') or (res[i]<'A' or res[i]>'Z')) and ((res[j]>='a' and res[j]<='z') or (res[j]>='A' and res[j]<='Z'))):
            i=i+1
            #print('here2')
        elif(((res[i]<'a' or res[i]>'z') or (res[i]<'A' or res[i]>'Z')) or ((res[j]<'a' or res[j]>'z') or (res[j]<'A' or res[j]>'Z'))):
            i=i+1
            j=j-1       
            #print('here3')     
    res=("".join(map(str,res)))    
    print(res)