"""Todo App Console
demirtaserdem@gmail.com
https://github.com/demirtaserdem/todo-app-python-console
"""
"""Veritabanı işlemlerini SQLALCHEMY-ORM ile yapan dosyadır.
firststepfunc.py,
secondstepfunc.py 
dosyaları tarafından kullanılır. 
"""

import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(os.path.abspath(sys.executable))
elif __file__:
    # çalışan programın yolunu almak için 
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# veri tabanı engine oluşturmak için
engine = create_engine("sqlite+pysqlite:///{}".format(os.path.join(base_path,"sqlite.db")))
# Test Aşamasında kullanmak için
# engine = create_engine("sqlite+pysqlite:///{}".format(os.path.join(base_path,"sqlite.db")),echo = True)

# base class oluşturuluyor miras almak için. 
Base = declarative_base(bind=engine)
# session maker oluşturuluyor session objesi oluşturmak için.
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    """Tablo adı "users" dört sutunu var one to many ilişkinin one tarafı.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String,nullable = False, unique=True)
    password = Column(String,nullable = False)
    todos = relationship("Todo", backref="user",cascade="save-update, merge, delete")

class Todo(Base):
    """Tablo adı "todos" dört sutunu var one to many ilişkinin many tarafı. 
    """
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    todo = Column(String(30))
    status = Column(Boolean)
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable = False)

# Migrate fonksiyonu gibi oluşturuyor.
Base.metadata.create_all(engine,checkfirst = True)