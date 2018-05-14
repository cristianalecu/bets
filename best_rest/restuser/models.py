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
        if self.id:  # anybody can create only user owner or staff can update
            self.user.email=self.myemail
            self.user.username=self.myemail
            self.user.set_password(self.mypassword)
            self.user.save()
        self.mypassword = ''
        self.myemail = ''
        super(RestUser, self).save(*args, **kwargs)
        
    def __str__(self):
        return '%s' % (self.user.username)
        
    @receiver(post_save, sender=User)
    def create_user_restuser(instance, created, **kwargs):
        if created:
            if instance.username == '__RestUser__':
                instance.username = instance.email
                instance.save()
            else:
                RestUser.objects.create(user=instance)

    