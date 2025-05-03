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
def get_primes(n):
    primes=[]
    if(n>1):
        for v in range(2,n-1):
            y=v
            x=0
            z=0
            while (z==0):
                y=y-1
                if(y>1):
                    if(x==0 and v%y!=0):
                        x=0
                    else:
                        x=1
                        z=1
                else:
                    z=1
            if(x==0):
                primes.append(v)
    return primes
                
def print_primes(n):
    primes=get_primes(n)
    for v in primes:
        print(v, end=' ')
