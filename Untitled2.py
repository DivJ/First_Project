
# coding: utf-8

# In[ ]:

from bs4 import BeautifulSoup
import urllib
url= urllib.urlopen('http://persmin.gov.in/dod/dopt_dod_directory_complete.asp').read()
inf = BeautifulSoup(url)
inf=str(inf)
def count_no(inf):
    result=[]
    count=0
    for ix in range(1,len(inf)):
        if (ix+10)<len(inf) and inf[ix-1].isdigit()==False and inf[ix].isdigit()==True          and inf[ix+1].isdigit()==True and inf[ix+2].isdigit()==True and inf[ix+3].isdigit()==True         and inf[ix+4].isdigit()==True and inf[ix+5].isdigit()==True and inf[ix+6].isdigit()==True         and inf[ix+7].isdigit()==True and inf[ix+8].isdigit()==False:
            result.append(inf[ix])
            result.append(inf[ix+1])
            result.append(inf[ix+2])
            result.append(inf[ix+3])
            result.append(inf[ix+4])
            result.append(inf[ix+5])
            result.append(inf[ix+6])
            result.append(inf[ix+7])
            result.append(" ")

    result = ''.join(result)
    print result
print "end"

