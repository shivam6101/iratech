def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
          
def sum(n):
    s = 0.0  
    for i in range(1, n + 1):
        s += 1.0 / factorial(i)
    print(s)

n=int(input("enter any value : "))
sum(n)