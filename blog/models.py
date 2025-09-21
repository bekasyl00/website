

from django.contrib.auth.models import User
from django.db import models
from django.utils  import timezone
from PIL import Image
from django.urls import reverse


class document(models.Model):
    d_naz=models.CharField('Файл атауы',max_length=64, blank=True, null=True,unique=True) 
    d_doc = models.FileField(upload_to='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
   


    def __str__(self):
        return self.d_naz
class statia(models.Model):
   
    title = models.CharField('aty',max_length=64, blank=True, null=True,unique=True) 
    text = models.TextField('angime',blank=True, null=True)
    time=models.DateTimeField(default=timezone.now)
    adam = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    poto=models.ImageField('фото',default='default.png',upload_to='news_images')
    views=models.IntegerField('prosmotr',default=1)
    def get_absolute_url(self):
        return reverse('news-detail',kwargs={'pk':self.pk})
    
    def __str__(self):
        return f'{self.title}'
    def save(self,*args,**kwargs):
        super().save()
        
        image=Image.open(self.poto.path)
        if image.height > 500 or image.width > 400:
            
            resize=(500,400)
            image.thumbnail(resize)
            image.save(self.poto.path)
    class Meta:
        verbose_name='новость'
        verbose_name_plural='новость'