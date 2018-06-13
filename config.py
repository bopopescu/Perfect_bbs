#config.py
__author__ = 'derek'
import os
SECRET_KEY = os.urandom(24)

CMS_USER_ID = 'abcdefg' #随便写一值，这样session更加安全
DEBUG = True

DB_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/bbs?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False