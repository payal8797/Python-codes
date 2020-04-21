def completionTime(pid,arr,burst):
    comp=[]
    completionTime[1]=burst[1]
    for i in range(0,n-1):
        completionTime[i]=burst[i]+burst[i-1]
        comp.append(completionTime)
    print(comp)


if __name__=="__main__":
    n=int(input("Enter number of processes:"))
    pid=[]
    arr=[]
    burst=[]
    for i in range(n):
        p=input("Process id:")
        pid.append(p)
    for i in range(n):
        a=int(input("Arrival Time:"))
        arr.append(a)
    for i in range(n): 
        b=int(input("Burst Time:"))
        burst.append(b)
    print("Process id:",pid)
    print("Arrival time:",arr)
    print("Burst time:",burst)

    completionTime(pid,arr,burst)