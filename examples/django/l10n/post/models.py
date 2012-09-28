from django.db import models
from django.utils.translation import ugettext_lazy as _
import vinaigrette

class Post(models.Model):
    message = models.CharField(max_length=200,
            verbose_name='Message', help_text=_('A message'))

    def __unicode__(self):
        return self.message

vinaigrette.register(Post, ['message'])
