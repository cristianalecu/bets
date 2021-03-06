from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework import permissions
from restuser.permissions import IsOwnerOrStaff

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all() 
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrStaff)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        queryset = super(SnippetList, self).get_queryset()

        if self.request.user and not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)
            
        return queryset


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer    
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrStaff)