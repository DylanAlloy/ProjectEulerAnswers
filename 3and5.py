def mult(x):
    sum_xhat=[]
    for i in range(x):
        if i%3==0:
            sum_xhat.append(i)
        elif i%5==0:
            sum_xhat.append(i)
    print(str(sum(sum_xhat)))
mult(1000)