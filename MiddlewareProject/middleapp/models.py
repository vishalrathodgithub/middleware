from django.db import models
from django.db.models.signals import pre_save,post_save

# Create your models here.
class Publication(models.Model):
    title=models.CharField(max_length=40)

    def __str__(self):
        return self.title
def pre_signal_check(sender,instance,**kwargs):
    print("before user create pre_signal_check")

def post_signal_check(sender,instance,**kwargs):
    print("user have created post_signal_check")


pre_save.connect(pre_signal_check,sender=Publication)
post_save.connect(post_signal_check,sender=Publication)

class Article(models.Model):
    headline=models.CharField(max_length=40)
    publications=models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
