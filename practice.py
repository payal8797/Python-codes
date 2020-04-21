# given a number n, from 1 to n, convert each number to its binary equivalent,append and convert to decimal...[n=3..1,10,11..11011..27] 

def binaryToDecimal(x1):
    arr=[]
    res=list(map(int,str(x1)))
    n=len(res)-1
    for i in res:
        y=i*(2**n)
        n=n-1
        arr.append(y)
    output=sum(arr)
    print(output)

def decimalToBinary(n):
    arr1=[]
    array1=[] 
    for i in range(1,n+1):
        array=[]
        while(i>=1):       
            #print("value of i:",i)
            y=i%2
            i=i//2
            array.append(y)
            #print(array)
        array.reverse()
        #print("here:",array)
        array1.append(array)
    #print(array1)
    for x in array1:
        #print(x)
        for y in x:
            arr1.append(y)
        #print(arr1)
    x1=("".join(map(str,arr1)))
    #print(x1)
    binaryToDecimal(x1)

if __name__=="__main__":
    n=int(input("Enter number:"))
    decimalToBinary(n)