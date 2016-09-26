def fib(n, x, y):
    #instantiate an array to store even fib#s
    even=[]
    #so long as the sum of the two numbers is less than our limit, continue
    while (x+y)<n:
            #store the sum
            z=x+y
            #print it for us dumb humans so we know it's happening
            print(z)
            #look for complete modularity
            if z%2==0:
                print("Even fibonacci number found.")
                #add the even numbers to the array
                even.append(z)
            #add come fibonnaci logic
            x=y
            y=z
    #get that sum
    sums = sum(even)
    print("Sum:"+str(sums))
    #ta-daa!
    print("Finished")
    
#call our algorithm with the assignment and old school fib values
fib(4000000,0,1)
