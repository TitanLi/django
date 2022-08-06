# query
[https://docs.djangoproject.com/en/2.1/ref/models/querysets/](https://docs.djangoproject.com/en/2.1/ref/models/querysets/)

> ORM = Table.objects.all()
> 可使用以下方法查看SQL
> ORM.query

1. objects.get
```python
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import VnfPkgInfo

@csrf_exempt
def test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            queryDataByID = VnfPkgInfo.objects.get(id='bd65600d-8669-4903-8a14-af88203add39')
            print(queryDataByID.id,queryDataByID.onboardingState)
            return JsonResponse({
                "id":queryDataByID.id
            })
        except:
            raise Http404("Question does not exist")
            pass
    else:
        return HttpResponse("Hello world")
```
2. objects.all()
```python
for e in VnfPkgInfo.objects.all():
    print(e.id,e.onboardingState)
```
3. objects.filter
ORM:
```python
dataArray = Table_1.objects.filter(key_1='bd65600d-8669-4903-8a14-af88203add38')
```
SQL:
```
select *
from Table_1
where key_1 = 'bd65600d-8669-4903-8a14-af88203add38'
```
4. INNER JOIN
ORM:
```python
dataArray = Table_1.objects.select_related('key1') 
```
SQL:
```
select *
from Table_1 inner join Table_2 ON (Table_1.key1 = Table_2.key1)
```

## serialization
[https://docs.djangoproject.com/en/2.2/topics/serialization/](https://docs.djangoproject.com/en/2.2/topics/serialization/)
1. objects to JSON
```
from django.core.serializers import serialize

serialize('json', SomeModel.objects.all(), cls=LazyEncoder)
```