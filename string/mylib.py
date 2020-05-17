import os, sys


def lihat(list):
    print ("[ ID, Nama, Harga ]")
    for i in range(len(list)):
        print (list[i])


def cari(list):
    j = int(input("masukan ID :"))
    x = [x for x in list if j in x][0]
    print (list[list.index(x)])



def urut(list):
    list.sort (key=lambda x: (x[0],x[1]))
    print ("[ ID, Nama, Harga ]")
    for i in range(len(list)):
        print (list[i])


def hapus(list):
    list.clear()
    print ("Data telah terhapus T_T")


    




