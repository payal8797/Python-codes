if __name__=="__main__":
    start=int(input("Start of range:"))
    end=int(input("End of range:"))
    number=int(input("Enter number whose sum is to be calculated:"))
    sum=0
    while number>0:
        remainder=number%10
        number=number//10
        sum=sum+remainder
    print("Sum of digits is:",sum)
    for i in range(start,end):
        sum1=0
        while start:
            remainder=start%10
            start=start//10
            sum1=sum1+remainder
            if sum==sum1:
                print(start)
            else:
                start=start+1  