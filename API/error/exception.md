# http exception
參考網址：[https://docs.djangoproject.com/en/2.2/topics/http/views/#django.http.Http404](https://docs.djangoproject.com/en/2.2/topics/http/views/#django.http.Http404)

編輯APP_NAME/views.py
方法一：
```
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```
方法二：
```
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```