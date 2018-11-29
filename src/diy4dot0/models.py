from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete

class DigitalItemModel(models.Model):
    DBTag = models.CharField(max_length=10,blank = True,editable=False,null=True)
    HumanTag = models.CharField(max_length=10)
    Bit0 = models.CharField(max_length=50)
    Bit1 = models.CharField(max_length=50)
    Bit2 = models.CharField(max_length=50)
    Bit3 = models.CharField(max_length=50)
    Bit4 = models.CharField(max_length=50)
    Bit5 = models.CharField(max_length=50)
    Bit6 = models.CharField(max_length=50)
    Bit7 = models.CharField(max_length=50)
    
    def clean(self):
        self.DBTag=self.HumanTag.replace(' ','_')
                        
    def __str__(self):
        return self.FormatTag
        
class AnalogItemModel(models.Model):
    DATATYPE_CHOICES=(
        ('INTEGER','Integer'),
        ('FLOAT','Float')
    )
    DBTag = models.CharField(max_length=10,blank = True,editable=False,null=True)
    HumanTag = models.CharField(max_length=10)
    DataType= models.CharField(max_length=10,choices=DATATYPE_CHOICES)
    Units = models.CharField(max_length=10)
    
    def clean(self):
        self.DBTag=self.HumanTag.replace(' ','_')
                        
    def __str__(self):
        return self.FormatTag
        
