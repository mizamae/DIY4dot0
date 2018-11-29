from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.RELEASES_ROOT)

    
class ReleaseModelManager(models.Manager):
    def create_Release(self, Date,Name,ChangeList,DjangoImage,RaspImage):
        Rel = self.create(Date=Date,Name=Name,ChangeList=ChangeList,DjangoImage=DjangoImage,RaspImage=RaspImage)
        Rel.save()

class ReleaseModel(models.Model):
    
    Date= models.DateField(unique=True)
    Name = models.CharField(max_length=20,unique=True,error_messages={'unique':_("Invalid release name - This name already exists in the DB.")})
    ChangeList = models.CharField(max_length=200)
    DjangoImage = models.FileField(storage=fs)
    RaspImage = models.FileField(storage=fs)
    
    objects = ReleaseModelManager()
        
    def __str__(self):
        return self.Name

@receiver(post_save, sender=ReleaseModel, dispatch_uid="update_ReleaseModel")
def update_ReleaseModel(sender, instance, update_fields,**kwargs):
    if kwargs['created']:   # new instance is created
        print('Se ha registrado la version ' + str(instance))
