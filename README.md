# Todo App Python Console  

Python SqlAlchemy - ORM kullanılarak, Çok kullanıcılı şifreli 
todoapp uygulamasıdır. 

### Yöntem
One to Many veritabanı yöntemiyle işlem yapılmıştir.
Bir kullanıcının birden fazla todo kaydı olabilir. 
Bir todunun bir kullanucusu olabilir.

One tarafında "user" tablosu, Many tarafında todo tablosu kaydedilmiştir.

Başlangıç ekranı ve kullanıcı ekranı olmak üzere, iki adımdan oluşturulmuştur
Kullanıcı şifreleri veritabanına şifrelenerek kaydedilmiştir.

Her girdide "q" girişi geri dönme veya programı sonlandırma 
görevinde kullanılmıştır.

Sqlite3 kullanılmış SqlAlchemy - ORM kullanılarak yapılmıştır.
func/models.py dosyasında veritabanı işlem sınıfları yazılmıştır. 

### Uygulamadan Fotoğraflar

![Imgur1](https://i.imgur.com/Qv77vuY.png?1)

![Imgur2](https://i.imgur.com/sqhhZhA.png?1)

![Imgur3](https://i.imgur.com/nkZmuno.png?1)

![Imgur4](https://i.imgur.com/ywOnav3.png?1)

### Çalışma Ağacı - Kısa Açıklamalarla

```bash
.
└── todo-app-python-console
    ├── func                    -->> Fonksiyonların bulunduğu klasör
    │   ├── firststepfunc.py    -->> İlk ekranda kullanılan fonksiyonların bulunduğu dosya.
    │   ├── models.py           -->> Database Tablo Sınıflarının ORM işlemlerinin balkangıç dosyası
    │   └── secondstepfunc.py   -->> Kullanıcı ekranında kullanılan fonksiyonların bulunduğu dosya.
    ├── app.py                  -->> Çalıştırılacak dosya.
    ├── icon.ico                -->> Derlemede kullanınan icon resmi.Ks
    ├── README.md               -->> Github README dosyası
    ├── requirements.txt        -->> pip install -r requirements.tx ile yüklenecek modül listesi.
    └── todouml.odg             -->> todo uml diagramı

```

## Çalıştırma
Dosyaları indirmek için komutu çalıştırılır.

```
git clone https://github.com/demirtaserdem/todo-app-python-console.git
```
Yüklemeleri yapmak için komutu çalıştırılır
```
pip install requirements.txt
```
çalıştırmak için app.py ile aynı klasörün içinde komutu çalıştırılır
```
python app.py
```

## Geliştirme - Değiştirme
Veritabanı dosyasında todolar için tarih eklenebilir.

Todolar için filtreleme özelliği eklenebilir. 

### Çalışan uygulama
Aşağıdaki adrestedir
https://github.com/demirtaserdem/todo-app-python-console/releases

derleme işlemi w10-x64 ortamında pyinstaller'la yapılmıştır.
pyinstaller yüklemek için
```
pip install pyinstaller
```
derlemek için
```
pyinstaller.exe --onefile --icon=icon.ico app.py
```

## Kaynak
[1] : https://docs.sqlalchemy.org/en/latest/

[2] : https://belgeler.yazbel.com/python-istihza/

