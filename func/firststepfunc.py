"""Todo App Console
demirtaserdem@gmail.com
https://github.com/demirtaserdem/todo-app-python-console
"""
"""app.py dosyası tarafından çağırılan fonksiyonları
içeren dosyadır.
models.py 
dosyalasındaki fonksiyonları kullanır. 
"""

from func.models import Todo,User,session
#Şifre girişinin gizli tutan 
from getpass import getpass
from passlib.hash import sha256_crypt

"""Login Blok Begin
"""
def firstStep():
    """Seçenek istenilen Fonksiyon 
    1,2,"q" girdilerini kabul ediyor.
    seçileni strig olarak döndürüyor.
    """
    while True:
        prFirstStep()
        option =  input('Seçenegi Giriniz ["1","2","q"]: ')
        option = option.lower().strip()
        if option in ["1","2","q"]:
            return option
        else:
            print("Seçeneği Yanlış girdiniz... Tekrar Deneyin... \n")

def prFirstStep():
    """ İlk Ekranın seçeneklerinin gösterilmesi 
    fonksiyonu.
    """
    print("""
    ******************************
    Python Todo Console Uygulaması

    1. Kullanıcı Giriş Yapınız.

    2. Yeni Kullanıcı Oluşturun.

    Çıkış için 'q' tuşuna basınız.
    ******************************

    """)

def login():
    """ Giriş işlemin ana döngüsünü barındıran fonksiyon
    kullanıcı adını ister, kullanıcı şifresini ister
    şifrelenmiş şifreyi kontrol eder doğruysa kullanıcı adını döner
    """
    while True:
        username = loginUsername()
        if username == None: return
        password = loginPasword()
        if password == None: return
        if loginCheck(username,password): return username

def loginUsername():
    """Kullanıcı girişi için kullanıcı adının istendiği fonksiyondur.
    kullanıcı adının veritabanında kayıtlı olup olmadığını kontrol eder.
    varsa K.A. döndürür. "q" seçeneği girilirse None döndürür. 
    """
    while True:
        username = input("Kullanıcı adınızı giriniz: ").strip() 
        if username in ["q","Q"]: return 
        userQuery = session.query(User).filter(User.username == username).first()
        if userQuery: return username
        else: print("Böyle bir kullanıcı bulunmamaktadır.")

def loginPasword():
    """K.A. Girişi için şifre istendiği fonksiyondur. Şifreyi görünmez
    olarak ister. 'q' olursa None döner. Boşluk kabul etmez uygun giri 
    yapılırsa şifreyi döner.
    """
    while True:
        password = getpass("Şifreyi Giriniz: ").strip()
        if password:
            if password in ["q","Q"]: return
            return password

def loginCheck(username,loginPasword):
    """ Kullanıcı adı ve şifreyi veritabanından kontrol eder. 
    uyuşuyorsa True Uyuşmuyorsa False Döndürür
    """  
    user = session.query(User).filter(User.username == username).first()
    if (username == user.username and 
        sha256_crypt.verify(loginPasword,user.password)):
        print("Giriş Başarılı.")
        return True
    else: 
        print("Kullanıcı Adı ve Şifre Uyuşmuyor...")
        return

"""Login Blok End
"""

"""Sign up Blok Begin 
"""
def signup():
    """Kayıt ol ana fonksiyonudur. Koşulları yazdırır 
    Kullanıcı adı ister, şifre ister, veritabanına 
    kayot eder. kullanıcı adını döndürür.
    """ 
    prSignuptext()
    while True:
        username = signupUsername()
        if username == None: return
        password = signupPasword()
        if password == None: return
        if password == False: continue
        signupCommit(username,password)
        return username

def prSignuptext():
    """Kullanıcı kaydı için metin.
    """
    print("""
    ******************************
    Kullanıcı Kaydı

    Şifre ve kullanıcı kaydının başında ve sonunda boşluk olamaz.

    Geri dönmek için 'q' tuşuna basınız.
    ******************************
    """)

def signupUsername():
    """Yeni kullanıcı adının istendiği ve veritabanından kontrol 
    edildiği fonksiyon "q" ile çıkış yapılabilir.
    """
    while True:
        username = input("Yeni kullanıcı adı giriniz: ").strip()
        if username: 
            if username in ["q","Q"]: return 
            if (session.query(User).filter(User.username == username)
                .first()):
                print("Kullanıcı adı daha önce alınmış")
            else: return username

def signupPasword():
    """ Kullanıcı kaydı için şifre istenilen fonksiyon 
    2 defa şifre istenin aynı olup olmadığı kontrol edilir.
    uygun koşullar sağlanırsa şifre döndürülür.
    """
    while True:
        password = getpass("Şifreyi Giriniz: ").strip()
        if password:
            if password in ["q","Q"]: return
            password2 = getpass("Şifreyi Tekrar Giriniz: ").strip()
            if password2 in ["q","Q"]: return
            if password == password2: return password
            else: 
                print("Parolalar Uyuşmuyor...")
                return False

def signupCommit(username,password):
    """Şifre ve kullanıcı adının veritabanına kayıt edildiği 
    fonksiyondur. Şifre veri tabanına şifrelenmiş olarak kaydedilir.
    """
    try:
        newUser = User()
        newUser.username = username
        newUser.password = sha256_crypt.encrypt(password)
        session.add(newUser)
        session.commit()
        print("Kullanıcı başarıyla kaydedildi.")
    except:
        print("Kullanıcıyı kaydederken hata oluştu.")

"""Sign up Blok End
"""

