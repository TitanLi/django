# django
[https://docs.djangoproject.com/en/2.2/intro/tutorial01/](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

[HttpRequest](https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpRequest)

[Database](https://docs.djangoproject.com/en/2.2/intro/tutorial02/)

## 環境準備
```
$ brew install python3
$ pip3 install virtualenv
$ virtualenv env
$ . env/bin/activate
$ pip3 install django
$ python3 -m django --version
```

## create project
```
$ django-admin startproject PROJECT-NAME
```

## create app
```
$ cd PROJECT-NAME
$ python manage.py startapp APP-NAME
```

## write view
```
$ vim APP-NAME/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")
```
## create URLconf file(urls.py)
```
$ vim APP-NAME/URLconf_name.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
## set my app to project/urls
> import django.urls.include
```
$ vim ProjectName/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('SET-URL/', include('APP-NAME.URLconf_name')),
    path('admin/', admin.site.urls),
]
```
## run server
```
$ python manage.py runserver
```

## connect mySQL
```
$ vim mysite/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
> mac OS

> brew install mysql-client

> #### mysql-client is not on the `PATH` by default

> export PATH="/usr/local/opt/mysql-client/bin:$PATH"

> #### openssl is not on the link path by default

> export LIBRARY_PATH="$LIBRARY_PATH:/usr/local/opt/openssl/lib/"

> pip3 install mysqlclient

### 初始化
> 須先建立database(mydatabase)
```
$ python manage.py migrate
```

### Creating models
```
$ vim APP-NAME/models.py

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
### Activating models

> APP-NAME => polls

> polls.apps.PollsConfig

> PollsConfig在polls/apps.py檔案中可找到
```
$ mysite/settings.py

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 透過makemigrations告訴Django您已對模型進行了一些更改
# 完成後會產生polls/migrations/0001_initial.py
$ python manage.py makemigrations polls
```

## 檢查遷移用的SQL
```
$ python manage.py sqlmigrate polls 0001
```