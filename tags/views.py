from rest_framework import generics, permissions
from .models import Tag
from .serializers import TagSerializer

class TagList(generics.ListCreateAPIView):
    """
    List all tags or create a new tag if authenticated.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def perform_create(self, serializer):
        # Here, no specific user is associated with the tag creation.
        # You can customize this if needed, for example by associating tags with a user or adding other logic.
        serializer.save()


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a tag.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
