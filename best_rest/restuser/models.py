from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class RestUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    validation_code = models.CharField(_('validation code'), max_length=10, default='')
    expire_validation = models.DateTimeField(_('expire validation'), default=timezone.now)
    
    @receiver(post_save, sender=User)
    def create_user_restuser(self, instance, created, **kwargs):
        if created:
            RestUser.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_restuser(self, instance, **kwargs):
        instance.restuser.save()