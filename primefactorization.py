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
<<<<<<< HEAD
=======
    
    #this part is a bit complicated. we're doing mod on numbers we already know are
    #factors in order to find out if they are prime ones. exception being 2 and 
    #we're using the square root of the number we're proving because this saves memory but also prevents 
    #us from having to look through all of the numbers in the range of 600 billion and stops us at one larger than
    #the square of a factor that we know isn't even due to factorize(x)... the only exception to this method being 
    #when the number we're proving is a perfect square & prime of the factor.
    #
    #example: sqrt(14)=3.74 but has a prime factor of 7 (7^2=14) which is larger than the sqrt. this however is ruled
    #out by the first chunk, just wanted to be mathematically rigorous in the comment
    #a.k.a. the sieve of eratosthenes
>>>>>>> origin/master
    print(all(i%n for n in range(3,int(sqrt(i))+1,2)))

factorize(600851475143)
