# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 11:30:25 2016

@author: Gao
"""
import string
import urllib 
from bs4 import BeautifulSoup

url = ('http://www.yelp.com/biz/jean-georges-new-york?osq=jean+george')
ourUrl = urllib.urlopen(url)
soup = BeautifulSoup(ourUrl)   #use of BeautifulSOup
tag=soup('p')

f=open('reviews.txt','w')
n=1
for i in tag:
    if i.get('itemprop'):
        i=str(i)        #for counting
        i=i.replace('<p itemprop="description" lang="en">','')
        f.write(str(n))
        n=n+1
        f.write("."+i+'\n'+'\n')
        print i
f.close()

        
