def factorize(x):
    i=2
    while (x/2)+1>i:
        if (x%i)==0:
            print(str(i)+" is a factor!")
            is_prime(i)
        i+=1
    print("Finished!")
    
from math import sqrt

def is_prime(i):
    if i == 2:
        return True
    if (i < 2) or (i % 2 == 0):
        return False
    print(all(i%n for n in range(3,int(sqrt(i))+1,2)))

factorize(600851475143)