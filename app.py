"""Todo App Console
demirtaserdem@gmail.com
https://github.com/demirtaserdem/todo-app-python-console
"""
"""Çalıştırılacak ana python dosyasıdır.
firststepfunc.py
secondstepfunc.py 
dosyalarındaki fonksiyonları kullanır. 
"""
from func.firststepfunc import firstStep,login,signup
from func.secondstepfunc import secondstep,getTodosFromdb,prTodos
from func.secondstepfunc import addTodoTodb,getTodoNumber,updateTodoObjText
from func.secondstepfunc import updateTodoObjStatus,deleteTodoObj,deleteUser
from func.secondstepfunc import prSecondStep
from time import sleep

def secondStepLoop(username):
    """İlk adımdan kullanıcı adı alarak çağırılan fonksiyon
    kendi içerisinde kullanıcı adını istenilen seçenekteki
    fonksiyonlara göndererek işlem yapılan döngüdür. 
    """
    # İlk olarak seçenekler yazdırılıyor
    prSecondStep()
    while True:
        # ikinci adım döngüsü
        # gelen seçeneğe göre işlem yapılıyor
        secondstepoption = secondstep(username)
        # seçenekte kullanıcıdan çıkış yapılıyor.
        if secondstepoption == "q":
            print("Kullanıcıdan Çıkış Yapılıyor")
            return
        # seçenekte kullanıcın todoları ve durumları ekrana
        # yazdırılıyor
        elif secondstepoption == "1":
            todosObjList = getTodosFromdb(username)
            if todosObjList: 
                prTodos(todosObjList)
            else: print("Kayıtlı Todo Bulunmuyor.")
        # seçenekte todo ekleme işlemi yapılıyor.
        elif secondstepoption == "2":
            addTodoTodb(username)
        # seçenekte todo durumu güncelleme işlemi yapılıyor
        elif secondstepoption == "3":
            todosObjList = getTodosFromdb(username)
            todoObj = getTodoNumber(todosObjList)
            if todoObj: updateTodoObjStatus(todoObj)
        # seçenekte yazısı güncelleme işlemi yapılıyor.
        elif secondstepoption == "4":
            todosObjList = getTodosFromdb(username)
            todoObj = getTodoNumber(todosObjList)
            if todoObj: updateTodoObjText(todoObj)
        # seçenekte todo silme işlemi yapılıyor. 
        elif secondstepoption == "5":
            todosObjList = getTodosFromdb(username)
            todoObj = getTodoNumber(todosObjList)
            if todoObj: deleteTodoObj(todoObj)
        # seçenekte mevcut kullanıcının silme işlemi yapılıyor.
        elif secondstepoption == "6":
            if deleteUser(username): return
        # seçenekte bütün seçenekler Yazdırılıyor.
        elif secondstepoption == "7": prSecondStep()

while True:
    # Main Loop
    # ilk olarak seçenek isteniyor.
    firststepoption = firstStep()
    # dönen 3 seçenekten birinin işlemi
    # yapılıyor.
    # Bu seçenekte
    # döngüden çıkıp programı kapatma işlemi yapılıyor
    if firststepoption == "q":
        print("Çıkış Yapılıyor...")
        sleep(0.5)
        break
    # seçenekte giriş yapma işlemi yapılıyor
    # ikinci adıma kullanıcı adıyla geçiliyor.    
    elif firststepoption == "1":
        sessionUsername = login()
        if sessionUsername: 
            secondStepLoop(sessionUsername)
    # seçenekte kullanıcı kaydı yapılıyor.
    # giriş yapılmış şekilde ikinci adıma kullanıcı adıyla geçiş 
    # yapılıyor.
    elif firststepoption == "2":
        signUsername = signup()
        if signUsername: 
            secondStepLoop(signUsername)