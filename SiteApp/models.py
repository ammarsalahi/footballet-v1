
from django.db import models
from bs4 import BeautifulSoup
import requests

from utils.bs_data import *

# Create your models here.
class Site(models.Model):
    site_url=models.URLField(
        verbose_name='آدرس',
        unique=True
    )
    name=models.CharField(
        max_length=100,
        verbose_name='نام سایت'
    )
    logo=models.ImageField(
        verbose_name='لوگو',
        upload_to='logos/',
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name
    def get_site(self):
        return self.site_url

    def get_request(self):    
        site=requests.get(self.get_site())
        soup=BeautifulSoup(site.text,'html.parser')
        return soup

    def get_mixed_data(self,context):
        soup=self.get_request()
        if self.name== 'ورزش سه':
            set_v3(soup=soup,context=context,lim=4)
        elif self.name== 'فوتبالی':
            set_ft(soup=soup,context=context,lim=4)
        elif self.name== 'فارس':
            set_fn(soup=soup,context=context,lim=4)
        elif self.name== 'خبرورزشی':
            set_kv(soup=soup,context=context,lim=4)
        elif self.name== 'تسنیم':
            set_ts(soup=soup,context=context,lim=4)
        elif self.name== 'مهر':
            set_mh(soup=soup,context=context,lim=4)
        elif self.name== 'ایسنا':
            set_is(soup=soup,context=context,lim=4)
        elif self.name== 'خبرآنلاین':
            set_ko(soup=soup,context=context,lim=4)    
        elif self.name== 'ایرنا':
            set_ir(soup=soup,context=context,lim=4) 
        elif self.name== 'ایمنا':
            set_im(soup=soup,context=context,lim=4)   
        elif self.name== 'ایلنا':
            set_il(soup=soup,context=context,lim=4)                            
    def get_data(self):
        soup=self.get_request()
        context=[]
        if self.name=='ورزش سه':
            set_v3(soup=soup,context=context,lim=15)
        elif self.name== 'فوتبالی':
            set_ft(soup=soup,context=context,lim=15)
        elif self.name== 'فارس':
            set_fn(soup=soup,context=context,lim=9)
        elif self.name== 'خبرورزشی':
                set_kv(soup=soup,context=context,lim=15)
        elif self.name== 'تسنیم':
            set_ts(soup=soup,context=context,lim=15)
        elif self.name== 'مهر':
            set_mh(soup=soup,context=context,lim=15)
        elif self.name== 'ایسنا':
            set_is(soup=soup,context=context,lim=15)
        elif self.name== 'خبرآنلاین':
            set_ko(soup=soup,context=context,lim=9)    
        elif self.name== 'ایرنا':
            set_ir(soup=soup,context=context,lim=15) 
        elif self.name== 'ایمنا':
            set_im(soup=soup,context=context,lim=9)   
        elif self.name== 'ایلنا':
            set_il(soup=soup,context=context,lim=9)       
        return context            

  
        

     