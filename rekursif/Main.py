import os, sys
import mylibrary

def main():
 #1
    print("Penjumlahan")
    num1 = int(input("Inputkan Angka : "))
    num2 = int(input("Inputkan Angka : "))
    print(f"Hasil penjumlahan dari {num1} + {num2} = {mylibrary.add_rec(num1,num2)}")
    print("="*70)
#2
    print("Pengurangan")
    num1 = int(input("Inputkan Angka : "))
    num2 = int(input("Inputkan Angka : "))
    print(f"Hasil pengurangan dari {num1} - {num2} = {mylibrary.subs_rec(num1,num2)}")
    print("="*70)
#3
    print("Perkalian")
    num1 = int(input("Inputkan Angka : "))
    num2 = int(input("Inputkan Angka : "))
    print(f"Hasil perkalian dari {num1} x {num2} = {mylibrary.mul_rec(num1,num2)}")
    print("="*70)
#4
    print("Perpangkatan")
    num1 = int(input("Inputkan Angka : "))
    num2 = int(input("Inputkan Angka : "))
    print(f"Hasil pemangkatan dari {num1} ^ {num2} = {mylibrary.pow_rec(num1,num2)}")
    print("="*70)
#5
    print("Deret Fibonnaci")
    n = int(input("Inputkan Batas Fibonnaci : "))
    for i in range(1, n+1):
        print(mylibrary.fib(i), end=" ")
    print ()
    print("="*70)
#6
    print("Deret Ascending")
    n=int(input("Masukkan angka : "))
    print(f"Hasil dari deret {n} adalah : ")
    for i in range(mylibrary.deret(n)):
        print(i+1,end=" ")
    print()
    print("="*70)
#7
    print("Deret Descending")
    n=int(input("Inputkan angka : "))
    print(f"Hasil dari deret {n} adalah : ")
    for i in range (n,0,-1):
        print(mylibrary.deret_desc(i),end=" ")
    print()
    print("="*70)
#8
    print("Hasil penjumlahan deret ")
    n = int(input("Inputkan panjang deret : "))
    print(f"Hasil penjumlahan deret adalah {mylibrary.sum(n)} ")
    print("="*70)
#9
    print("Hasil penjumlahan deret fibonacci ")
    n=int(input("Inputkan Panjang deret fibonacci : "))
    print(f"Hasil penjumlahan deret fibonacci adalah {mylibrary.sum_fib(n)}")
    print("="*70)
#10
    num=int(input("Inputkan Angka: "))
    print(mylibrary.cetak(num))

if __name__ == '__main__':
    main()
