#manage.py
__author__ = 'derek'

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from Perfect_bbs import create_app
from exts import db

from apps.cms import models as cms_models

CMSUser = cms_models.CMSUser
app = create_app()

manager = Manager(app)

Migrate(app,db) #绑定app跟db
manager.add_command('db',MigrateCommand)

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_cms_user(username,password,email):
    user = CMSUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功')
    
if __name__== '__main__':
    manager.run()