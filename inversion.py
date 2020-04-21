def inversion(array,n):
    array2=[]
    for i in range(n-1):
        array1=[]
        for j in range(i,n):
            if(array[i]>array[j]):
                array1.append(array[j])
                #print(array[i],array[j])
        array2.append(array1) 
    print(array2)
                

        

if __name__=="__main__":
    n=int(input("Enter number of elements in array:"))
    array=[]
    #k=int(input("Enter size of inversion:"))
    for i in range(n):
        y=int(input())
        array.append(y)
    inversion(array,n)