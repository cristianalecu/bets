
from rest_framework import permissions
from restuser.permissions import IsRestUserOrStaff
from django.contrib.auth.models import User
from restuser.models import RestUser
from restuser.serializers import RestUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class RestUserList(APIView):
    def get(self, request, format=None):
        objs = RestUser.objects.all()
        if self.request.user and self.request.user.id :
            if not self.request.user.is_staff:
                objs = objs.filter(user=self.request.user)
            #else:    #staff can see all
        else:
            objs = objs.filter(pk=0)       

        serializer = RestUserSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RestUserSerializer(data=request.data)
        if serializer.is_valid():
            users1 = User.objects.all().filter(username='__RestUser__')
            if users1.count() > 0:
                users1[0].delete()
            users2 = User.objects.all().filter(username=self.request.data['myemail'])
            users3 = User.objects.all().filter(email=self.request.data['myemail'])
            if users2.count() == 0 and users3.count() == 0:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                if users2.count():
                    return Response({'duplicate':'duplicate email'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'duplicate':'duplicate email'}, status=status.HTTP_400_BAD_REQUEST)
#                 send_mail(
#                     'Subject here',
#                     'Here is the message.',
#                     'from@example.com',
#                     ['to@example.com'],
#                     fail_silently=False,
#                     )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestUserDetail(APIView):
    """
    Retrieve, update or delete a restuser instance.
    """
    def get_object(self, pk):
        try:
            return RestUser.objects.get(pk=pk)
        except RestUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        
        if request.user.id and (request.user.id == obj.user.id or request.user.is_staff):
            serializer = RestUserSerializer(obj)
            return Response(serializer.data)
        return Response( status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        if request.user.id and (request.user.id == obj.user.id or request.user.is_staff):  # anybody can create only user owner or staff can update
            obj.user.email=request.data['myemail']
            obj.user.username=request.data['myemail']
            obj.user.set_password(request.data['mypassword'])
            obj.user.save()   
        serializer = RestUserSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)                 # Should not delete rest user, only the parent user 
        serializer = RestUserSerializer(obj)
#         if request.user.id and (request.user.id == obj.user.id or request.user.is_staff):
#             obj.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

