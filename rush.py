
"""def hello():
    print('st',end="*")
def three():
    for i in range(3):
        hello()

three()
def fib(n):"""
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
print(fib(7))
