n=100
p=[]
while 1000>n:
    for i in range(99, 1000):
        prod=i*n
        if str(prod)==str(prod)[::-1]:
            print("Found a palindrome: "+str(prod))
            p.append(prod)
    n+=1
print(str(max(p)))