def factorial(n):
    if n<2:
        return 1
    if n<1:
        return None
    product=1
    for i in range(2,n+1):
        product=product*i
    return product
print(factorial(5))