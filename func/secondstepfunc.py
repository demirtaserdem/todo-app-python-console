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
import sqlalchemy.orm

def secondstep(username):
    """Seçenek istenilen Fonksiyon 
    1,2,3,4,5,6,7,"q" girdilerini kabul ediyor.
    seçileni string olarak döndürüyor.
    """
    while True:
        option =  input('Seçenegi Giriniz ["1","2","3","4","5","6","7","q"]: ')
        option = option.lower().strip()
        if option in ["1","2","3","4","5","6","7","q"]:
            return option
        else:
            print("Seçeneği Yanlış girdiniz... Tekrar Deneyin... \n")

def prSecondStep():
    """İkinci Ekranın seçeneklerinin gösterilmesi. 
    """
    print("""
    ******************************
    Todo Bölümü

    1. Tüm Todoları Görüntüleyin

    2. Todo Ekleyin.

    3. Todo Durumunu Değiştirin

    4. Todo Metnini Güncelleyin

    5. Todo Silin
    
    6. Kullanıcıyı Siliniz
    
    7. Seçenekleri Görün

    Geri dönmek için 'q' tuşuna basınız.
    ******************************
    """)

def getTodosFromdb(username):
    """K.A.'ya göre todoları veritabanından alıp
    obje listesi olarak döndüren fonksiyon.
    """ 
    try:
        user = (session.query(User).filter(User.username == username)
            .first())
        # todosObjList = user.todos
        todosObjList = (session.query(Todo)
            .filter(Todo.user_id == user.id).all())
        return todosObjList
    except:
        print("Todoloarı alırken hata oluştu")

def prTodos(todosObjList):
    """gelen todo obje listesini ekrana yazdıran fonksiyon.
    id numarasına 1 ekleyerek tablo numarası oluşturur.
    """
    print("   ","No | Todo")
    print("   ","***|***********")
    for todoObj in todosObjList:
        print("  ",todosObjList.index(todoObj)+1,"|",todoObj.todo,todoObj.status,sep = "  ")

def addTodoTodb(username):
    """ K.A. ya göre yeni todoları alan foksiyon. 
    veritabanına ekleme fonksiyonunu çağırır.
    """
    while True:
        todo = input("Todoyu Giriniz: ")
        todo = todo.strip()
        if todo in["q","Q"]: return
        elif todo: 
            commitAddTodo(username,todo)
        else:
            print("Tekrar Giriniz.")

def commitAddTodo(username,todo):
    """ Kullanıcı Adına göre todoyu todo tablosuna ekler.
    """ 
    try:
        user = (session.query(User)
            .filter(User.username == username).first())
        newTodo = Todo()
        newTodo.status = False
        newTodo.todo = todo
        newTodo.user_id = user.id
        print(newTodo.status,newTodo.todo,newTodo.user_id)
        session.add(newTodo)
        session.commit()
        print("Todo başarıyla kaydedildi.")
    except:
        print("Todo kaydederken hata oluştu.")

def getTodoNumber(todosObjList):
    """İşlem yapılacak todo numarasını ister obje listesinin 
    içerisinde mi kontolünü yapar. Uygunsa ilgili todo objesini döner.
    """
    while True:
        inp = input("İşlem Yapılacak Todo Numarasını Giriniz: ")
        inp = inp.strip()
        try:
            if inp in ["q","Q"]: return
            if int(inp) in range(1,len(todosObjList)+1):
                return todosObjList[int(inp) - 1]
            else:
                print("Listede Bulunmamaktadır...")
        except: pass

def updateTodoObjStatus(todoObj):
    """todo Objesinin durumunu değiştirir veritabanından günceller.
    """
    todoObj.status = not todoObj.status
    session.add(todoObj)
    session.commit()
    print("Todo durumu {} oldu".format(todoObj.status))

def updateTodoObjText(todoObj):
    """Todo objesinin metnini değiştirir ve veritabanından günceller.
    """
    print(todoObj.todo)
    while True:
        inp = input("Değiştirilmiş Yazıyı Giriniz: ")
        inp = inp.strip()
        if inp in ["q","Q"]: return
        elif inp:    
            todoObj.todo = inp
            session.add(todoObj)
            session.commit()
            print("Başarıyla GÜncellendi...")
            return
            
def deleteTodoObj(todoObj):
    """Todo Objesinin silinme kontrolünü yapıp siler.
    """
    while True:
        inp = input(" Todo Silinecek Emin misiniz (y/n):  ")
        inp = inp.strip().lower()
        if inp == "q": return
        elif inp in ["y","yes"]:
            try:
                session.delete(todoObj)
                session.commit()
                print("Todo Başarıyla silindi")
                return
            except:
                print("Hata Oluştu...")
        elif inp in ["n","no"]:
            print("Todo Silimedi...")
            return

def deleteUser(username):
    """Kullanıcı Sİlme fonksiyonu Kullanıcı şifresini kontrol eder.
    emin misin işlemini yapar.
    K.A.'ya göre kullanıcı objesini alır veritabanından siler. 
    """
    if deleteUserGetPass(username):
        while True:
            inp = input("Emin misiniz (y/n):  ")
            inp = inp.strip().lower()
            if inp == "q": return
            elif inp in ["y","yes"]:
                try:
                    userObj = (session.query(User).
                        filter(User.username == username).first())
                    session.delete(userObj)
                    session.commit()
                    print("Kullanıcı ve Todoları Başarıyla silindi...")
                    return True
                except:
                    print("Hata Oluştu...")
            elif inp in ["n","no"]:
                print("Kullanıcı Silimedi...")
                return
    return

def deleteUserGetPass(username):
    """Kullanıcı silme işlemi için şifre ister ve kontrolünü yapar.
    doğrulanırsa true doğrulanmazsa None döner.
    """
    userObj = (session.query(User).
                    filter(User.username == username).first())
    while True:
        print("{} kullanıcısı silinecek çıkmak için 'q' giriniz.".format(username))
        print("Devam etmek için ")
        password = getpass("Kullanıcı şifresini giriniz: ").strip()
        if password in ["q","Q"]: return
        if (sha256_crypt.verify(password,userObj.password)): return True
        else: 
            print("Kullanıcı Adı ve Şifre Uyuşmuyor...")
            print("Geri dönmek için 'q' giriniz... ")


