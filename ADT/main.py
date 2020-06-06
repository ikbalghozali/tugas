class Kalkulator (object):
    def __init__(self,bil1,bil2):
        self.bil = bil1
        self.bil2 = bil2
        
    def jumlah(self):
        print("Hasil dari {} + {} = ".format(self.bil,self.bil2),self.bil + self.bil2)
        
    def kurang(self):
        print("Hasil dari {} - {} = ".format(self.bil,self.bil2),self.bil - self.bil2)
        
    def kali(self):
        print("Hasil dari {} * {} = ".format(self.bil,self.bil2),self.bil * self.bil2)

    def pangkat(self):
        print("Hasil dari {} ^ {} = ".format(self.bil,self.bil2),self.bil ** self.bil2)
        
    
a = int(input('Masukan Bilangan 1 :'))
b = int(input('Masukan Bilangan 2 :'))
op = Kalkulator(a,b)
op.jumlah()
op.kurang()
op.kali()
op.pangkat()