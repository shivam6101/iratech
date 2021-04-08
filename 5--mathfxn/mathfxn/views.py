from django.shortcuts import render
from django.http import JsonResponse

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
          
def sum(n):
    s = 0.0  
    for i in range(1, n + 1):
        s += 1.0 / factorial(i)
    return s

def fxn(request):
    if request.method=='POST':
        value=int(request.POST.get("value"))
        ans=sum(value)
        return render(request,'index.html',{'ans':ans})
    return render(request,'index.html')