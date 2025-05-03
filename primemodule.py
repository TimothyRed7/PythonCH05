def is_prime(n):
    if(n>1):
        t=0
        for v in range(2,n-1):
            if(t==0 and n%v!=0):
                t=0
            elif(t!=0 or n%v==0):
                t=1
                return False
    else:
        t=1
        return False
    if(t==0):
        return True
print(is_prime(10))
print(is_prime(11))