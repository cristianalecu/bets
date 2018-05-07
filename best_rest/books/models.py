from django.db import models

LEVEL = (
    (0, 'Supreem'),
    (1, 'Major'),
    (2, 'Current'),
  )
STATUS = (
    (0, 'Updated'),
    (1, 'Only local'),
    (2, 'Changed'),
    (3, 'Deleted'),
  )

class Author(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    importance = models.SmallIntegerField(choices=LEVEL, default=2)
    priority = models.SmallIntegerField(default=0)
    until = models.DateTimeField(auto_now_add=True)
    picture = models.TextField(blank=True, default='')
    why = models.TextField(blank=True, default='')
    to_be = models.TextField(blank=True, default='')
    to_know = models.TextField(blank=True, default='')
    to_do  = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super(Author, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)