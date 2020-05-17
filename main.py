import os, sys
import mylib
'''
Maaf pak kalo codingnya kurang sempurna
A11.2019.12060
'''

def main():
    list = []
    while True:
        print('Pilih Menu : \n 1. input Data \n 2. lihat data \n 3. cari data \n 4. lihat data terurut \n 5. hapus data \n 0. untuk selesai')
        n = int(input())
        
        if n == 0:
            print('program selesai')
            break
       
        elif n == 1:
            batas = int(input('Masukan Kapasitas Barang:'))
            for _ in range(batas):
                list.append([int(input('Masukan ID :')), str(input('Masukan Nama :')), int(input('Masukan Harga :'))])
            
        elif n == 2:
            mylib.lihat(list)

        elif n == 3:
            mylib.cari(list)

        elif n == 4:
            mylib.urut(list)

        elif n == 5:
            mylib.hapus(list)



if __name__ == '__main__':
    main()