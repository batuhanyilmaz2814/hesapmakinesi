# Batuhan Yılmaz 24011064 YODA İHA YAZILIM 2. Hafta Ödevi

from collections import Counter

metin = input("Lütfen hesaplatmak istediğiniz metni giriniz: ") #Kullanıcıdan hesaplatılacak metin alınır.

metin = metin.lower()#İşlem kolaylığı adına tüm harfler küçük harfe dünüştürülür.

metinislem = metin.split() #Daha kolay işlem yapılması adına metin listeye dönüştürülür.

kelimesayisi = metinislem.__len__() # Kelime sayısı uygun fonksiyon ile bulunur

bosluksayisi = kelimesayisi - 1 #İleride kullanmak için boşluk sayısı bulunur.

karaktersayisi = len(metin) #Karakter sayısı bulunur.

enuzunkelime = max(metinislem, key=len) #En uzun kelime bulunur.

tekrar = dict(Counter(metinislem)) #Counter modulü ile listemizdeki değerleri saydık ve takrar sayılarını belirledik, ardından çıktımızı güzelleştirmek adına bunu bir sözlüğe çevirdik

print("Yaptığımız hesaplamalar sonucunda: \n Metnin kelime sayısı: {} \n Metnin karakter sayısı: {} \n Metnin en uzun kelimesi: {} \n Tekrar sayıları: {} \n Boşluk sayısı: {} \n olarak hesaplanmıştır.".format(kelimesayisi,karaktersayisi,enuzunkelime,tekrar,bosluksayisi))

#Ve son olarak istenen çıktı kullanıcıya iletilmektedir.





   








