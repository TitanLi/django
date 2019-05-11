# view templates
## 參考資料
[view](https://docs.djangoproject.com/en/2.2/intro/tutorial03/)

[view templates](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-TEMPLATES)

## 步驟
1. 確認django setting(PROJECT/settings.py)檔案設定
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        ....
    }
]
```
2. 新增templates目錄APP-NAME/templates/APP-NAME/index.html
3. 編輯APP-NAME/templates/APP-NAME/index.html
```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question }}/">{{ question }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
4. 編輯update/views.py
方法一：
```
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('update/index.html')
    context = {
        # 傳至html資料
        'latest_question_list': ['aaaa','bbbb'],
    }
    return HttpResponse(template.render(context, request))
```
方法二：
```
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
        'latest_question_list': ['aaaa','bbbb'],
    }
    return render(request, 'update/index.html', context)
```
5. 編輯APP-NAME/urls.py
```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /update/
    path('', views.index, name='index'),
]
```