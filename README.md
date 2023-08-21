# Developer Case

Bu proje, yazılmış scriptlerin koleksiyonunu içerir.

## Kurulum ve Ayarlar

Bu bölümde, projeyi başarılı bir şekilde çalıştırmak için gerekli kurulum ve ayar adımlarını bulabilirsiniz.

### 1. Ön Koşullar

- Python 3.10+ yüklü olmalıdır. Python'ı [resmi web sitesi](https://www.python.org/downloads/) üzerinden indirebilirsiniz.
- Pip (Python Paket Yöneticisi) yüklenmelidir. Python'ı resmi sitesinden indirirseniz genellikle Pip de yüklenmiş olacaktır.

### 2. Sanal Ortamın Oluşturulması (Opsiyonel)

Bu adım opsiyoneldir, ancak scriptleri bir sanal ortamda çalıştırmak, bağımlılıkların ana Python yüklemenizle çakışmasını önler. Sanal bir ortam oluşturmak için:

```bash
cd <scripts_klasörünün_yolu>
python -m venv venv
```

Sanal ortamı aktive etmek için `scripts` klasörünün içerisindeyken:
```bash
. venv\Scripts\activate
```

### 3. Bağımlılıkların Kurulması

`requirements.txt` dosyasında listelenen bağımlılıkları kurmak için:

```bash
pip install -r requirements.txt
```

### 4. Scriptleri Çalıştırma

Scriptleri çalıştırmadan önce aşağıdaki "Script Açıklamaları" bölümündeki talimatları takip edin.

## Dizin Yapısı

```
scrips/
├── requirements.txt
├── script1/
│   ├── script1.exe
│   └── script1.py
├── script2/
│   ├── DejaVuSans.ttf
│   ├── kelimeler.txt
│   └── script2.py
├── script3/
│   ├── fetch_data.py
│   ├── hava.py
│   ├── save_to_db.py
│   └── weather_data.db
└── venv/
```


## Script Açıklamaları

### script1 (`script1.py`)

Bu script, "Netstat -ano", "Whoami", "Systeminfo" ve "ver" gibi bir dizi komutu çalıştırır. Bu komutların çıktılarını yakalar ve bu bilgileri bir Excel dosyasına (`script1-çıktı.xlsx`) yazar. Excel dosyası komut adı, komut çıktısı ve ek biçimlendirme ile düzenlenmiştir.

`exe` dosyasını oluşturmak için pyinstaller kullanılmıştır.

**Bağımlılıklar**:
- `openpyxl`

### script2 (`script2.py`)

Bu script, bir metin dosyasından (`kelimeler.txt`) kelimeleri okur ve bunları alfabetik sıraya göre bir PDF dosyasına (`script2-çıktı.pdf`) yazar. Script, PDF için belirli bir yazı tipini (`DejaVuSans.ttf`) kullanır.

**Bağımlılıklar**:
- `reportlab`

### script3 (`hava.py`)

Bu script, bir SQLite veritabanıyla (`weather_data.db`) etkileşimde bulunarak hava durumu verilerini gösterir. Kullanıcılar birden çok yolla hava durumu verilerini görebilir:
1. Tüm veriyi tarihe göre sıralayarak listele.
2. Belirli bir tarihe göre sıcaklık sorgula.
3. Belirli bir sıcaklıkta olan tüm tarihleri listele.

**Kullanım**:

- Tüm veriyi tarihe göre sıralayarak listele: `python hava.py -d`
- Belirli bir tarihe göre sıcaklık sorgula: `python hava.py -t <TARİH>`
- Belirli bir sıcaklıkta olan tüm tarihleri listele: `python hava.py -s <SICAKLIK>`

**Tarih Formatı**: GG/AA/YYYY

**Bağımlılıklar**:
- `sqlite3`
- `argparse`

**Verilerin Baştan Oluştulması**

Öncelikle `fetch_data.py` çalıştırılarak verilerin `temperatures` isimli bir klasöre indirilmesi sağlanır.
Daha sonra `save_to_db.py` scripti ile bu verilerden yeni bir veritabanı oluşturulur.