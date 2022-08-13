#!/usr/bin/env python
# coding: utf-8

# In[55]:


f=open("hi_train.conll",'r',encoding='utf-8')
f1=f.read()
li=f1.split("# id")
res_sen=[]
res_label=[]
for i in li:
    temp=i.split("\n")
    li_sen=[]
    li_label=[]
    for j in range(len(temp)):
        if temp[j]=='':
            continue
        if j==0:
            continue
        s=temp[j].split(" ")
        li_sen.append(s[0])
        li_label.append(s[-1])
    if len(li_sen)==0 or len(li_label)==0:
        continue
    res_sen.append(li_sen)
    res_label.append(li_label)
    
    
df={"sentence":[],"Labels":[]}
row1=[]
row2=[]
for i in range(len(res_label)):
    li1=res_label[i]
    li2=res_sen[i]
#     print(li1)
    s1=''
    s2=''
    for j in range(len(li1)):
        s1+=li1[j]+" "
        s2+=li2[j]+" "
    row1.append(s1.rstrip())
    row2.append(s2.rstrip())

for i in range(len(row1)):
    df["sentence"].append(row2[i])
    df['Labels'].append(row1[i])
    
    
import pandas as pd

new = pd.DataFrame.from_dict(df)

new.to_csv("ner_csv_train.csv",index=None)


# In[ ]:





# In[56]:


f=open("hi_dev.conll",'r',encoding='utf-8')
f1=f.read()
li=f1.split("# id")
res_sen=[]
res_label=[]
for i in li:
    temp=i.split("\n")
    li_sen=[]
    li_label=[]
    for j in range(len(temp)):
        if temp[j]=='':
            continue
        if j==0:
            continue
        s=temp[j].split(" ")
        li_sen.append(s[0])
        li_label.append(s[-1])
    if len(li_sen)==0 or len(li_label)==0:
        continue
    res_sen.append(li_sen)
    res_label.append(li_label)
    
    
df={"sentence":[],"Labels":[]}
row1=[]
row2=[]
for i in range(len(res_label)):
    li1=res_label[i]
    li2=res_sen[i]
#     print(li1)
    s1=''
    s2=''
    for j in range(len(li1)):
        s1+=li1[j]+" "
        s2+=li2[j]+" "
    row1.append(s1.rstrip())
    row2.append(s2.rstrip())

for i in range(len(row1)):
    df["sentence"].append(row2[i])
    df['Labels'].append(row1[i])
    
    
import pandas as pd

new = pd.DataFrame.from_dict(df)

new.to_csv("ner_csv_test.csv",index=None)


# In[51]:





# In[52]:





# In[53]:





# In[54]:




