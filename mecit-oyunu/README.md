# Mecit Abi – Redaksiyonun Efendisi 📝

Ofisimizin redaktörü Mecit Abi'nin bir haftasını anlatan mobil tarayıcı oyunu. Her gün ayrı bir mini oyun:

| Gün | Oyun | Ne yapıyorsun? |
|---|---|---|
| Pazartesi | Baskıya Gitmeden | Kitap matbaaya gitmeden yazım yanlışlarına dokunup düzeltiyorsun |
| Salı | Kısa Bir Şey Anlatıcam | Hikâye sürerken kaçmaya çalışanları (Berk, Ata, Hanım kız...) geri oturtuyorsun |
| Çarşamba | Ata, Bu Ne Diyor? | Berk bir şey söylüyor, Mecit Abi inanmıyor. Ata sensin, doğru mu yanlış mı söylüyorsun |
| Perşembe | Git Artık Anne! | Butona basa basa kayınvalideyi kapıya kadar götürüyorsun |
| Cuma | Niye Kapadın?! | Kepenk indiren esnafa dokunup dükkanı geri açtırıyorsun |
| Cumartesi | Acıbadem Batağı | 3 hanımefendiyle batak oynuyorsun (koz maça), arada iltifat ediyorsun 😏 |

## Nasıl oynanır?
- **En kolayı:** `mecit-abi.html` dosyasını telefona gönder (WhatsApp, AirDrop, e-posta) ve tarayıcıda aç. Tek dosya, internet gerekmez.
- `index.html` + `assets/` klasörü de aynı oyundur (GitHub Pages ile yayınlanabilir).
- Telefonda "Ana Ekrana Ekle" dersen uygulama gibi tam ekran açılır.

`index.html` değişirse tek dosyayı yeniden üretmek için: `python3 build.py`

## Mecit Abi'nin sesi
Oyundaki 72 replik `SES-METNI.md` dosyasında numaralı olarak duruyor. Kayıtlar `assets/ses/NN.mp3` olarak eklenir. Eksik olanlar sessiz kalır, oyun yine çalışır.
- Ayrı ayrı kayıtlar: `python3 ses_hazirla.py KAYIT_KLASORU` (dosya adındaki sayıya göre eşleşir)
- Tek uzun kayıt: `python3 ses_hazirla.py --bol kayit.m4a 1` (sessizliklerden böler, 01'den başlayarak numaralar)
- Ardından `python3 build.py` → sesler `mecit-abi.html` içine gömülür.
