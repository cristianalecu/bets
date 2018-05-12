from restuser.models import RestUser
from restuser.serializers import RestUserSerializer
from rest_framework import generics
from rest_framework import permissions
from restuser.permissions import IsRestUserOrStaff

class RestUserList(generics.ListCreateAPIView):
    queryset = RestUser.objects.all() 
    serializer_class = RestUserSerializer
    permission_classes = (permissions.IsAuthenticated, IsRestUserOrStaff)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        queryset = super(RestUserList, self).get_queryset()

        if self.request.user and not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
            
        return queryset


class RestUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestUser.objects.all()
    serializer_class = RestUserSerializer    
    permission_classes = (permissions.IsAuthenticated, IsRestUserOrStaff)