# Batuhan Yılmaz 24011064 YODA İHA YAZILIM 2. Hafta Ödevi

class BankaHesap:
    def __init__(self,ad,soyad,hesapno,sifre,bakiye,isDonuk=False):
        self.ad = ad
        self.soyad = soyad
        self.hesapno = hesapno
        self.bakiye = bakiye
        self.sifre = sifre
        self.isDonuk = isDonuk



    
hesap0 = BankaHesap("Eraslan","Uzunali",12024,"123456",10000.0)
hesap1 = BankaHesap("Batuhan", "Yılmaz",22024,"654321",1000.0)

liste = [hesap0, hesap1]

def bakiyesor():
    print(liste[a].bakiye)
def paracek():
    while(True):
        try:
            cekmiktar = float(input("Kaç lira çekmek istiyorsunuz: "))
            break
        except ValueError:
            print("Lütfen sayı giriniz")
    if(liste[a].bakiye - cekmiktar >= 0):
        liste[a].bakiye = liste[a].bakiye - cekmiktar
        print("Islem basarili. Hesap miktari: {}".format(liste[a].bakiye))
    else:
        print("Islem basarisiz hesabınızda yeteli bakiye yok")
    return cekmiktar

def parayatir():
    while(True):
        try:
            yatirmiktar = float(input("Kaç lira yatırmak istiyorsunuz: "))
            break
        except ValueError:
            print("Lütfen sayı giriniz")
    liste[a].bakiye = liste[a].bakiye + yatirmiktar
    print("Islem basarili. Hesap miktari: {}".format(liste[a].bakiye))
    return yatirmiktar

    
    


while True:
    try:
        deneNo = int(input("Lütfen hesap numaranizi giriniz: "))
    except ValueError:
        print("Hesap numaranız nümerik olmalidir.")
        continue
    a=0
    bulundu = False
    for hesapbul in liste:
        a += 1
        if hesapbul.hesapno == deneNo and a <= len(liste):
            print(f"Hosgeldiniz {liste[a-1].ad, liste[a-1].soyad} lütfen sifrenizi giriniz.")
            bulundu = True
            a = a-1
            break
    if (not bulundu):
        print("Bu numaraya ait bir hesap yok tekrar deneyiniz.")
        continue
    deneSifre = input("Lütfen sifrenizi giriniz: ")
    if(deneSifre == liste[a].sifre):
        islem = input("Giriş başarılı, hosgeldiniz sayın {} {}, Hesap no: {} \n Lütfen yapmak istediğiniz işlemi seciniz: \n Bakiye görüntüleme: b \n Para cekme: pc \n Para yatirma: py \n cikis: e \n hesap dondurma: hd \n islem: ".format(hesapbul.ad, hesapbul.soyad, hesapbul.sifre))
    else:
        print("Yanlış şifre lütfen tekrar deneyiniz.")
        continue
    if islem == "b" and not liste[a].isDonuk:
        bakiyesor()
    if islem == "pc" and not liste[a].isDonuk:
        paracek()
    if islem == "py" and not liste[a].isDonuk:
        parayatir()
    if islem == "e" and not liste[a].isDonuk:
        break
    if islem == "hd":
        if liste[a].isDonuk:
            liste[a].isDonuk = False
        else:
            liste[a].isDonuk = True
    if liste[a].isDonuk:
        print("Hesabiniz dondurulusmustur islem yapamazsiniz.")
        continue
    if (not(islem == ("b" or "pc" or "py" or "e" or "hd"))):
        print("Hatalı giris")
        continue
    
        


        




    
    
        

    

        

    


            

             
    




        