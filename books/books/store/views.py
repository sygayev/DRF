from rest_framework.viewsets import ModelViewSet 
from store.models import BookModel
from store.serializers import BookSerializer
 
 
class BookViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


