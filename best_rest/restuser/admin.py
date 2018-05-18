from django.contrib import admin

from .models import RestUser

class RestUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.id and request.user.id and (request.user.id == obj.user.id or request.user.is_staff):  # anybody can create only user owner or staff can update
            obj.user.email=self.myemail
            obj.user.username=self.myemail
            obj.user.set_password(self.mypassword)
            obj.user.save() 
            obj.save()
            
admin.site.register(RestUser, RestUserAdmin) 
