#  VnfPkgInfo: VnfPkgInfo object to Query Values 
> <QuerySet [<VnfPkgInfo: VnfPkgInfo object (049c2a37-c435-49d7-bb89-3604a225c235)>]

> to

> <QuerySet [{'id': UUID('049c2a37-c435-49d7-bb89-3604a225c235'),'aaaa':'aaaa'}, '...(remaining elements truncated)...']>
```python
VnfPkgInfo.objects.all().values()
```

# <class 'django.db.models.query.QuerySet'> to <class 'list'>
```python
vnfPkgInfoList = list(VnfPkgInfo.objects.all().values())

for e in vnfPkgInfoList:
    e['id'] = str(e['id'])
    e['createdAt'] = str(e['createdAt'])
    e['vnfPkgInfoID_id'] = str(e['vnfPkgInfoID_id'])
```