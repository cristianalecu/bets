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
        if not self.id and not self.user_id:
            self.user = User.objects.create_user(username='__RestUser__', email= self.myemail, password=self.mypassword)
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

    