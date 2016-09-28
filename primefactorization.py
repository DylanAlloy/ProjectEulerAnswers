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
    #so this part is a bit complicated. we're doing mod range(i)/n on numbers we already know are
    #factors in order to find out if they are prime ones. exception being 2 (duh) and 
    #we're using the square root of the number we're proving because this saves memory but also prevents 
    #us from having to look through all of the numbers in the range of 600 billion and stops us at one larger than
    #the square... the only exception being that the product of a number if it is a perfect square & prime
    #example: sqrt(14) 3.74 but has a prime factor of 7 (7^2=14)
    #a.k.a. the sieve of eratosthenes
    print(all(i%n for n in range(3,int(sqrt(i))+1,2)))

factorize(600851475143)
