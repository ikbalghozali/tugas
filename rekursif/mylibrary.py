import os, sys
#1
def add_rec(num1,num2):
    if num1 == 0 :
        hasil = num2
    else :
        hasil = 1 + add_rec((num1-1), num2)
    return hasil
#2
def subs_rec(num1,num2):
    if num2 == 0 :
        hasil = num1
    else :
        hasil = subs_rec(num1, (num2-1)) - 1
    return hasil
#3
def mul_rec(num1,num2):
    if num1 == 0 :
        hasil = 0
    elif num2 == 0 :
        hasil = 0
    else :
        hasil =  mul_rec((num1-1),num2) + num2
    return hasil
#4
def pow_rec(num1,num2):
    if num2 == 0:
        hasil = 1
    else :
        hasil = num1*pow_rec(num1, (num2-1))
    return hasil
#5
def fib(n):
    if (n <= 2):
        hasil = 1
    else:
        hasil = (fib(n-1)+fib(n-2))
    
    return hasil
#6
def deret(n):
    if n == 1:
        hasil = 1
    else :
        hasil = deret(n-1) + 1
    return hasil
#7
def deret_desc(n):
    if n == 1 :
        hasil = 1
    else :
        hasil = deret_desc(n-1) +1
    return hasil
#8
def sum(n):
    if n == 0:
        hasil = 0
    else :
        hasil= n + sum(n-1)
    return hasil
#9
def sum_fib(n):
    if n == 0 :
        hasil = 0
    elif n == 1 :
        hasil = 1
    else :
        hasil = (sum_fib(n-1)+sum_fib(n-2))+1
    
    return hasil
#10
def cetak(num):
    hasil = 1
    while num > 1 :
        hasil = hasil*num
        num = num -1
    return hasil

    

