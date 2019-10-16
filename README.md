# Sale Web API

Django RESTFUL Framework
App Name: Sale

```
INSTALLED_APPS += [
    'rest_framework',
    'myapp.apps.MyappConfig',
    'drf_autodocs',
]
```

## Model
- Product
- Customer
- Cart
  - buyer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  - sku = models.ForeignKey(Product, on_delete=models.CASCADE)
  - quantity = models.IntegerField())
  
## Serializer
- ModelViewSerializer
```
class Meta:
    model = xxx
    fields = ('id', '...',)
```
- Foreign Key (only show ID for reference)
```
xxx = XxxSerializer(many=False, read_only=True)
xxx_id = serializers.IntegerField(read_only=False)
```

## View
- APIView
- ModelViewSet: 
  - actions (provide .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy())
    - extra: 
```
@action(
    detail=False, 
    methods=['get'], 
    serializer_class=CartSerializer,
    url_path='xxx/(?P<xxx_id>[^/.]+)', 
    name='...')
def action_name(self, request, xxx_id, pk=None):
    xxx = Xxx.objects.all()[(int)(customer_id)-1]
    listitems = MyModel.objects.all().filter(xxx=xxx)
    serializer = self.get_serializer(listitems, many=True)
    return Response(serializer.data)
```
- queryset
    - Xxx.objects.all()
    - filter
- Permission
  - custom permission in 'permissions.py'
```
# sample code from toturial
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
```

## Documentation
### Interactive API documentation
- pip install coreapi
- add url in project setting
```
url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
```
- import url
```
from django.conf.urls import url
```
- add autosheme in project setting
```
REST_FRAMEWORK = {
   ...
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}
```

# TODO
- customized User
