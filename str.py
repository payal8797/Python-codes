def main(arr,length):

    i=0
    while(i<length-1):
        arr[i],arr[i+1]=arr[i+1],arr[i]
        i=i+2
    print(arr)
    arr.reverse()
    y=("".join(arr))
    print(y)
if __name__=="__main__":
    n=input()
    arr=list(n)
    length=len(arr)
    main(arr,length)