# django-rest-framework
[Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
## Serialization
1. 安裝virtualenv，創建一個新的虛擬環境
```
$ virtualenv env
$ source env/bin/activate
```
> 可使用deactivate退出狀態
1. 安裝
```
$ pip install django
$ pip install djangorestframework
$ pip install pygments # We'll be using this for the code highlighting
```
2. 建立專案
> PROJECT-NAME => tutorial

> APP-NAME => snippets
```
$ django-admin.py startproject PROJECT-NAME
$ cd PROJECT-NAME/
$ django-admin.py startapp APP-NAME
```
3. 建立models.py
> snippets/models.py

> PROJECT-NAME => tutorial

> APP-NAME => snippets
```
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
```
4. 透過makemigrations告訴Django您已對模型進行了一些更改
> PROJECT-NAME => tutorial

> APP-NAME => snippets
```
$ python manage.py makemigrations snippets
```
5. 在Database建立模型
```
$ python manage.py migrate
```
6. 建立Serializer class
> 在APP內建立serializers.py

> snippets/serializers.py
```
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
```
## 使用Serializers
Django shell
```
$ python manage.py shell
> from snippets.models import Snippet
> from snippets.serializers import SnippetSerializer
> from rest_framework.renderers import JSONRenderer
> from rest_framework.parsers import JSONParser

# 新增資料
> snippet = Snippet(code='foo = "bar"\n')
> snippet.save()

# 資料顯示
> snippet = Snippet(code='foo = "bar"\n')
> serializer = SnippetSerializer(snippet)
> serializer.data

# At this point we've translated the model instance into Python native datatypes. To finalize the serialization process we render the data into json
> content = JSONRenderer().render(serializer.data)
> content

> import io

> stream = io.BytesIO(content)
> data = JSONParser().parse(stream)

> serializer = SnippetSerializer(data=data)
> serializer.is_valid()
> serializer.validated_data

> serializer.save()

# 查詢多值
> serializer = SnippetSerializer(Snippet.objects.all(), many=True)
> serializer.data
```