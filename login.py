## LOGIN EKRANI


exit = 0

while exit == 0:
    kontrol = bool
    buyukharfkontrol = bool
    simgekontrol = bool

    kullanici_adi = input("Kullanici adınızı olusturunuz. Türkçe karakter kullanmayınız. : ")
    if kullanici_adi == "q":
        print("Sistemden Çıkılıyor....")
        exit = 1
        break

    ozelkarakter = "*?-_+/‘^!#$%&,:.;<>|İÖöÜüşŞçÇğĞ "

    kontrol = True

    for harf in ozelkarakter:
        if harf in kullanici_adi:
            print("Yasaklı karakter veya Türkçe karakter kullandınız.")
            kontrol = False
            break
        elif len(kullanici_adi) > 20:
            print("Karakter sayısını aştınız . En fazla 20 karakter kullanabilirsiniz.")
            kontrol = False
            break

    if not kontrol == False:
        sifre = input("Şifrenizi Oluşturunuz . Güçlü bir şifre seçiniz. : ")
        if sifre == "":
            print("Şifre boş bırakılamaz.")
            sifre = input("Şifrenizi Oluşturunuz . Güçlü bir şifre seçiniz. : ")
        elif sifre == "q":
            print("Sistemden Çıkılıyor....")
            exit = 1
            break

        buyukharf = "AWERTYUIOPASDFGHJKLZXCVBNM"
        simgeler = "é)(=}{*?-_+/‘^!#$%&,:.;<>| "
        buyukharfkontrol = False
        simgekontrol = False

        for guclusifre in buyukharf:
            if guclusifre in sifre:
                buyukharfkontrol = True
                break

        for simge in simgeler:
            if simge in sifre:
                simgekontrol = True
                break

        if buyukharfkontrol == True and simgekontrol == True:
            print("Güçlü bir parola oluşturdunuz.")
        elif buyukharfkontrol == True and simgekontrol == False:
            print("Orta seviyede bir parola oluşturdunuz.")
        elif buyukharfkontrol == False and simgekontrol == False:
            print("Güçsüz bir parola oluşturdunuz.")









