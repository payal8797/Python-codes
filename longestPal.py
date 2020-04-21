def getmaxpalin(str):
    strlen=len(str)
    if not(strlen%2==0):
        strlen=1
    max=0
    while(strlen>1):
        result=createsubarray(str,strlen)
        while x in result:
            pp=per(x)
            while y in pp:
                if(ispalin(y)):
                    max=len(y)
                    break
            if(max>0):
                break
        if(max>0):
            return max
        else:
            strlen==2