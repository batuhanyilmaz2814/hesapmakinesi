def tekrar2(fonksiyon):
    def wrapper_fonksiyon(*args, **kwargs):
        fonksiyon(*args, **kwargs)
        fonksiyon(*args, **kwargs)
    return wrapper_fonksiyon

@tekrar2
def merhaba():
    print("Merhaba")

@tekrar2
def isimlisi(isim):
    print(f"Merhaba {isim}")

isimlisi("Batuhan")
merhaba()

