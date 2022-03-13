import math

n = 0;


def recurringPrimeFactors(n):
    N = n
    factors = list()
    while n % 2 == 0:
        n = n / 2  
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            if i in factors:
                print('{0} is a recurring prime factor of {1}'.format(str(i), str(N)))
                # r
            factors.append(i)
            n = n / i
    if n > 2:
        # if n in factors:
            # r
        factors.append(n)



while(n < 100):
    x = pow(10, n) + 1
    if recurringPrimeFactors(x):
        n = 101
    else:
        print('{0} does not have any recurring prime factors.'.format(str(x)))
    n = n + 1
        
