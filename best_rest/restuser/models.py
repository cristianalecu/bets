from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class RestUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    validation_code = models.CharField(max_length=10, default='')
    expire_validation = models.DateTimeField(default=timezone.now)
    
    myemail = models.EmailField(blank=True)
    mypassword = models.CharField(blank=True,max_length=128)
    
    def save(self, *args, **kwargs):
        if( not self.id):
            self.user = User.objects.create(password=self.mypassword, username=self.myemail, email=self.myemail)
            
        self.mypassword = ''
        self.myemail = ''
        super(RestUser, self).save(*args, **kwargs)
        
    @receiver(post_save, sender=User)
    def create_user_restuser(self, instance, created, **kwargs):
        if created:
            RestUser.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_restuser(self, instance, **kwargs):
        instance.restuser.save()