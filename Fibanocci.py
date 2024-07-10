def fib(n):
    if n<3:
        return 1
    if n<1:
        return 0
    sum=0
    ele_1=ele_2=1
    for i in range (3,n+1):
        sum =ele_1+ele_2
        ele_1,ele_2=ele_2,sum
    return sum
for n in range (1,31):
    print(n,"------>",fib(n))