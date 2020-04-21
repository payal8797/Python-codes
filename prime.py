def fun(array,n):
    array1=[]
    array2=[]
    for i in range(n):
        if(array[i]==1):
            print("num is neither prime nor composite")
        elif(array[i]==2):
            array2.append(array[i])
        else:
            for j in range(2,array[i]):
                if(array[i]%j)==0:
                    array1.append(array[i])
                    #print("num is not prime")
                    break
                else:
                    #print(array[i])
                    array2.append(array[i])
                    break
                    
    print(array1)
    print(array2)



if __name__=="__main__":
    n=int(input())
    array=[]
    for i in range(n):
        array.append(int(input()))
    fun(array,n)