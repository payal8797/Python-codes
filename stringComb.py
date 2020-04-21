import math
def allPossibleCombination(array,n):
    comb=(int)(math.pow(2,n))
    array2=[]
    for i in range(0,comb):
        array1=[]
        for j in range(0,n):
            if((i & (1<<j))>0):
                print(array[j],end=" ")
                #array1.append(array[j])
                #if(sum(array1)==k):
                #    print("sum is k:",array1)
        #array2.append(array1)
        print(" ")
    print(array2)

if __name__=="__main__":
    n=int(input("Enter length of string:"))
    array=[]
    for i in range(n):
        m=int(input())
        array.append(m)
    #k=int(input("Enter req sum:"))
    allPossibleCombination(array,n)