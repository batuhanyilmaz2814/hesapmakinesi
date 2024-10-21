sayilar = [1,23,4,32,21,3,5,6,7,1000,12,3,3,3,3]
harfler = ["h","k","j","u","b"]

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)

print(sonuc)

# Bu komutlar listelerdeki en büyük (alfabetik en sonda) veya en küçük (alfabetik en başta) elemanı bulmamızı sağlar.

sayilar.append(2) #dizinin sonuna ekler
#harfler.append("a")
harfler.insert(0,"a") #istediğimiz yere ekleme yapmayı sağlar

#Bu komutlar listelerde eleman ekleme işlemlerini sağlar

sayilar.pop() #en sondaki elemanı siler
sayilar.remove(12) #belirli indexteki elemanı siler

#Bu komutlar listelerden eleman çıkartmayı sağlar.

harfler.sort() #Bu komut listeyi küçükten büyüğe(alfabetik) sıralar
sayilar.reverse() #Bu komut ters sıralar
 
#Bu komutlar sıralama işlemlerini gerçekleştirir

print(sayilar.count(3)) # sayilar kümesinde int cinsinden 3 elemanı ne kadar geçer bulunur.

print(harfler.index("b")) #harfler kümesinin "b" elamanının indexi bulunur



