#SoalNomer1
#M.IkbalGhozali-12060
def soal1(detik):
    h = detik // 3600
    m = detik % 3600 // 60
    s = detik % 3600 % 60
    print ('{:02d} jam {:02d} menit {:02d} detik'.format(h, m, s))

    if (h >= 1):
        print ("Perjalanan Anda jauh, siapkan perbekalan yang memadai")
    else:
        print ("Perjalanan Anda dekat, siapkan perbekalan yang secukupnya")

soal1(detik = int(input('detik :')))


#SoalNomer2
#M.IkbalGhozali-12060
def soal2():
    angka = int(input("Masukan angka :"))
    for i in range(angka, 1, -1):
        if angka % i == 0:
            print(i, end=" ")

        if angka != 1:
            print(end=" ")
        i -= 1

soal2()



#SoalNomer3
#M.IkbalGhozali-12060
def soal3(nilai):
    if (nilai <= 60):
        remidi = "Test ulang"
    elif (nilai < 70):
        remidi = "Penugasan"      
    else :
        remidi = "Tidak ada"
    print(remidi)

soal3(nilai = int(input('nilai :')))


#SoalNomer4
#M.IkbalGhozali-12060
def soal4():
    list = [] 
    while True:
        print("Silahkan pilih film: \n s untuk Susi Susanti \n m untuk Maleficent 3D")
        n = input("masukan pilihan :")

        if (n == "s"):
            print("Silahkan pilih bioskop: \n 1 untuk Citra XXI \n 2 untuk E plaza \n 3 untuk Cinemaxx")
            b = int(input())
            if (b == 1):
                jml = int(input("Masukan jumlah tiket :"))
                list.append(40000*jml)
                a = str(input("ingin beli lagi? y/n :"))
                if (sum(list) >= 200000):
                    disc = sum(list)*0.1
                elif (100000 <= sum(list) <= 199999):
                    disc = sum(list)*0.05
                else:
                    disc = 0
                total = (sum(list)) - disc
                if (a == "n"):
                    print(f"harga yang harus dibayarkan : Rp.{total}")
                    byr =  int(input("Masukan uang yang dibayarkan : Rp."))
                    print (f"kembalian : Rp.{byr - total}")
                    break
                elif (a == "y"):
                    print("ok")

            elif (b == 2):
                jml = int(input("Masukan jumlah tiket :"))
                list.append(25000*jml)
                a = str(input("ingin beli lagi? y/n :"))
                if (sum(list) >= 200000):
                    disc = sum(list)*0.1
                elif (100000 <= sum(list) <= 199999):
                    disc = sum(list)*0.05
                else:
                    disc = 0
                total = (sum(list)) - disc
                if (a == "n"):
                    print(f"harga yang harus dibayarkan : Rp.{total}")
                    byr =  int(input("Masukan uang yang dibayarkan : Rp."))
                    print (f"kembalian : Rp.{byr - total}")
                    break
                elif (a == "y"):
                    print("ok")

            elif (b == 3):
                jml = int(input("Masukan jumlah tiket :"))
                list.append(35000*jml)
                a = str(input("ingin beli lagi? y/n :"))
                if (sum(list) >= 200000):
                    disc = sum(list)*0.1
                elif (100000 <= sum(list) <= 199999):
                    disc = sum(list)*0.05
                else:
                    disc = 0
                total = (sum(list)) - disc
                if (a == "n"):
                    print(f"harga yang harus dibayarkan : Rp.{total}")
                    byr =  int(input("Masukan uang yang dibayarkan : Rp."))
                    print (f"kembalian : Rp.{byr - total}")
                    break
                elif (a == "y"):
                    print("ok")
            else:
                print("inputan salah")
                
        elif (n == "m"):
            print("Silahkan pilih bioskop: \n1 untuk Citra XXI \n 2 untuk E plaza \n 3 untuk Cinemaxx")
            b = int(input())
            if b == 1:
                jml = int(input("Masukan jumlah tiket :"))
                list.append(50000*jml)
                a = str(input("ingin beli lagi? y/n :"))
                if (sum(list) >= 200000):
                    disc = sum(list)*0.1
                elif (100000 <= sum(list) <= 199999):
                    disc = sum(list)*0.05
                else:
                    disc = 0
                total = (sum(list)) - disc
                if (a == "n"):
                    print(f"harga yang harus dibayarkan : Rp.{total}")
                    byr =  int(input("Masukan uang yang dibayarkan : Rp."))
                    print (f"kembalian : Rp.{byr - total}")
                    break

                elif (a == "y"):
                    print("ok")

            elif b == 2:
                jml = int(input("Masukan jumlah tiket :"))
                list.append(35000*jml)
                a = str(input("ingin beli lagi? y/n :"))
                if (sum(list) >= 200000):
                    disc = sum(list)*0.1
                elif (100000 <= sum(list) <= 199999):
                    disc = sum(list)*0.05
                else:
                    disc = 0
                total = (sum(list)) - disc
                
                if (a == "n"):
                    print(f"harga yang harus dibayarkan : Rp.{total}")
                    byr =  int(input("Masukan uang yang dibayarkan : Rp."))
                    print (f"kembalian : Rp.{byr - total}")
                    break

                elif (a == "y"):
                    print("ok")

            elif b == 3:
                jml = int(input("Masukan jumlah tiket :"))
                list.append(45000*jml)
                a = str(input("ingin beli lagi? y/n :"))
                if (sum(list) >= 200000):
                    disc = sum(list)*0.1
                elif (100000 <= sum(list) <= 199999):
                    disc = sum(list)*0.05
                else:
                    disc = 0
                total = (sum(list)) - disc
                
                if (a == "n"):
                    print(f"harga yang harus dibayarkan : Rp.{total}")
                    byr =  int(input("Masukan uang yang dibayarkan : Rp."))
                    print (f"kembalian : Rp.{byr - total}")
                    break
                elif (a == "y"):
                    print("ok")
            else:
                print ("inputan salah ")
                break
        else:
            print ("inputan salah")
            break

soal4()
    




    

