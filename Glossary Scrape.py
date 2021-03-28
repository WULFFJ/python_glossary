#Unstructured glossary page from https://docs.python.org/3/glossary.html


from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import xlsxwriter
pd.set_option('display.max_colwidth', 800)
df=pd.DataFrame(columns={'Term','Definition'})
url=r'https://docs.python.org/3/glossary.html'
response=requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
divs = soup.find_all(re.compile(r'(dt|dd)'))
list={'Term':[],'Definition':[]}
df=pd.DataFrame(columns={'Term','Definition'})

count=0.0
count=float(count)

for div in divs:
    num=(count/2.0)
    if count==0:
        list={'Term':[],'Definition':[]}
    elif float(num).is_integer():
        list={'Term':[],'Definition':[]}
    elif not float(num).is_integer():
        pass
    temp={'temp':[]}
    tests=div.text
    tests.split("\n\n")
    tests.replace("]","],")
    temp['temp'].append(tests)
    
    if count==0:
        list['Term'].append(temp)
    elif float(num).is_integer():
        list['Term'].append(temp)
    elif not float(num).is_integer():
        list['Definition'].append(temp)
        df=df.append(list,ignore_index=True)
    
    count=count+1
      
df.head(500)


# In[2]:


df=df.replace(r"[{'temp': '","")
df=df.replace(r"[{'temp': '","")
df=df.replace("]","")
df['Term']=(df['Term']).apply(pd.Series)
df['Definition']=(df['Definition']).apply(pd.Series)                                       
df.head()


# In[3]:



df['Definition']=pd.json_normalize(df['Definition'])
df['Term']=pd.json_normalize(df['Term'])
df['Term']=(df['Term']).apply(pd.Series)

df['Definition']=(df['Definition']).apply(pd.Series)                                       


# In[4]:


df.head()


# In[ ]:




