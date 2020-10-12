#soal1
day = int(input("hari : "))
y = []
for i in range (1, day+1):
    v = 2**(i-1)
    y.append(v)
print(y)

#soal2
import re

def filter_kata_jorok(match):
    kata_jorok = ['setan', 'keparat', 'bejad', 'gembel', 'brengsek' , 'tai', 'bangsat']
    kata = match.group()
    if kata.lower() in kata_jorok:
        return '*' * len(kata)
    else:
        return kata

def main():
    text = str(input("input :"))
    text = re.sub(r'\b\w*\b', filter_kata_jorok, text, flags=re.I|re.U)
    print(text)

main()


#soal3
A = [12,3,12,34,10,11,9,10]
foo = 0
n = len(A)
for i in range(len(A)):
    foo = foo+A[i]
print(foo/n)


#soal4
# struktur program
import os #contoh library built-in python
import math #contoh library built-in python

# fungsi dalam 1 file yang sama dengan entry point
# diletakkan sebelum entry point
def TesFunc():
    return "Hai"

def TesProc():
print("Alo")

# entry point dengan prosedur main
def main():
    print("hello world!")
    print(TesFunc())
    TesProc()

# panggil entry point
if __name__ == '__main__': 
    main()




