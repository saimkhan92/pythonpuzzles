# Program to implement Fibonacci series

a,b=0,1
print(a)
print(b)
for i in range(10):
    c=a+b
    print(c)
    a=b
    b=c
