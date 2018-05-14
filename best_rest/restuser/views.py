from restuser.models import RestUser
from restuser.serializers import RestUserSerializer
from rest_framework import generics
from rest_framework import permissions
from restuser.permissions import IsRestUserOrStaff
from django.contrib.auth.models import User

class RestUserList(generics.ListCreateAPIView):
    queryset = RestUser.objects.all() 
    serializer_class = RestUserSerializer
    #permission_classes = (permissions.IsAuthenticated, IsRestUserOrStaff)
    
    def perform_create(self, serializer):
        user = User.objects.create_user(username='__RestUser__', email=self.request.data['myemail'], password=self.request.data['mypassword'])
        serializer.save(user=user) 
        
    def get_queryset(self):
        queryset = super(RestUserList, self).get_queryset()

        if self.request.user and self.request.user.id :
            if not self.request.user.is_staff:
                queryset = queryset.filter(user=self.request.user)
            #else:    #staff can see all
        else:
            queryset = queryset.filter(pk=0)
            
        return queryset


class RestUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestUser.objects.all()
    serializer_class = RestUserSerializer    
    #permission_classes = (permissions.IsAuthenticated, IsRestUserOrStaff)