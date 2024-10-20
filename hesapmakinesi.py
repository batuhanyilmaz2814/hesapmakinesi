import os
import time

def isnedir():
    if (os.name == 'nt'):
        _=os.system('cls')
    elif (os.name == 'mac'):
        _=os.system('clear')
    elif (os.name == "posix"):
        _=os.system('clear')


print("Hesap Makinesine Hoşgeldiniz")
time.sleep(2)

while(True):
    print("Lütfen yapmak istediğiniz işlemi giriniz (+ toplama, - çıkartma, * çarpma, / bölme)")
    islem = input() 
    if (False == (islem=="+" or islem == "-" or islem == "*" or islem == "/")):
        print("İŞLEMDE HATALI DEĞER GİRDİNİZ LÜTFEN TEKRAR DENEYİNİZ")
        continue
    time.sleep(3)
    isnedir()
 
    try:
        sayi1 = float(input("Lütfen birinci sayıyı giriniz: "))
        time.sleep(1)
        sayi2 = float(input("Lütfen ikinci sayıy giriniz: "))
    except ValueError:
        print("LÜTFEN DOĞRU DEĞER GİRİNİZ")
    
    if(islem == "+"):
        sonuc = sayi1 + sayi2
        print("İstediğiniz işlemin sonucu: {}".format(sonuc))
        time.sleep(10)
    elif(islem == "-"):
        sonuc == sayi1 - sayi2
        print("İstediğiniz işlemin sonucu: {}".format(sonuc))
        time.sleep(10)
    elif(islem == "*"):
        sonuc == sayi1 * sayi2
        print("İstediğiniz işlemin sonucu: {}".format(sonuc))
        time.sleep(10)
    elif((islem == "/") and (sayi2 != 0)):
        sonuc = sayi1 / sayi2
        tambolum = sayi1 // sayi2
        kalan = sayi1 % sayi2
        print("İstediğiniz işlemin sonucu: {} . Tam bölümü {}. İşlemin kalanı da {}' dır.".format(sonuc,tambolum,kalan))
        time.sleep(10)
    else:
        print("HATALI DEĞER GİRDİNİZ LÜTFEN TEKRAR DENEYİN")
        continue
    i=0
    a=10
    while(i != 10):
        print("Ekran {} saniye sonra temizlenecek".format(a))
        time.sleep(1)
        a=a-1
        i=i+1
    isnedir()
    k = input("Başka bir işlem yapmak istiyor musunuz? (y=evet, n=hayır)")
    if (k=="y"):
        continue
    elif(k=="n"):
        print("Bizi terci ettiğiniz için teşekkür ederiz.")
        break
    else:
        print("HATALI GİRİŞ EN BAŞA YÖNLENDİRİLİYORSUNUZ")
        continue

    
    

        
