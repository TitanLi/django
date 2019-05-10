# 建立管理員用戶
## 建立使用者
```
$ python manage.py createsuperuser

Username (leave blank to use 'liwensheng'): admin
Email address: admin@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```
## 啟動服務
```
$ python manage.py runserver
```
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
## 讓Dashboard可以對Database進行修改
```
$ vim APP-NAME/admin.py

from django.contrib import admin

from .models import MODEL_NAME

admin.site.register(MODEL_NAME)
```