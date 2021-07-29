import datetime
from win10toast import ToastNotifier
import random

bilgiler = [
    "YouTube'da videolarda çok hızlı geçen bir karenin fotoğrafını çekmek istiyorsanız Space tuşuna basılı tutabilirsiniz.",
    "Div seçicinize ekleyeceğiniz overflow:auto; taşan içeriklerin belirttiğimiz boyutlarda otomotik olarak 'görünmesini' sağlar.",
    "Unix sunucularda Monit ile PHP, Mysql gibi hizmetleri 2 dakikada bir kontrol edip, çökmüşse yeniden başlatmak mümkün. Kurulum için: https://www.tecmint.com/how-to-install-and-setup-monit-linux-process-and-services-monitoring-program/",
    "Facebook'ta profil resimlerinize yenilik katmak için https://www.facebook.com/profilepicframes adresini kullanabilirsiniz.",
]
n = ToastNotifier()

kacdakika = int(input("Kaç dakikada bir ara verilsin:(varsayılan: 25)") or 25)
arasure = int(input("Tenefüs süresi kaç dakika olsun:(varsayılan: 5)") or 5)
print("Sistem başlatılıyor.\nR10.net: leaver\nInstagram: talhatugsat")

def araVer(sec):
    while True:
        timestamp = datetime.datetime.now().timestamp()
        if (sec + (60*int(arasure))) < timestamp:
            n.show_toast("Hatırlatıcı","Başlayabilirsin!", threaded=True)
            basla(timestamp)
            break

def basla(sec):
    while True:
        timestamp = datetime.datetime.now().timestamp()
        if (sec + (60*int(kacdakika))) < timestamp:
            n.show_toast("Hatırlatıcı","Ara vermelisin, yararlı bilgilerde bu tenefüs: " + random.choice(bilgiler), duration=20, threaded=True)
            araVer(timestamp)
            break

basla(datetime.datetime.now().timestamp())
