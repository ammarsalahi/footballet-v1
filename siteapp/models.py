from django.db import models
from bs4 import BeautifulSoup
import requests
from utils.bs_data import *
from utils.getmixdata import *

# Create your models here.
class Site(models.Model):
    site_url=models.URLField(unique=True)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_site(self):
        return self.site_url

    def get_request(self):    
        site=requests.get(self.get_site())
        soup=BeautifulSoup(site.text,'html.parser')
        return soup
    def get_mixed(self,context):
        soup=self.get_request()
        set_mixed_data(model=self,context=context,soup=soup)

    def get_data(self):
        soup=self.get_request()
        return get_all_data(model=self,soup=soup)    

              

  
        

     