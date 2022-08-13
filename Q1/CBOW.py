#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from numpy.linalg import norm
from gensim.models import Word2Vec
import pickle


# In[2]:


def cosine_similarity(v1,v2):
    v1=np.array(v1)
    v2=np.array(v2)
    dot_prod=v1.dot(v2)
    pro_norm=norm(v1)*norm(v2)
    return dot_prod/pro_norm


# In[3]:


def accuracy(y_pred,y_true):
    t=0
    n=len(y_pred)
    for i in range(n):
        if y_pred[i]==y_true[i]:
            t+=1
        else:
            t+=0
    return t/n

def thresholding(sim,threshold):
    s=[]
    for i in sim:
        if i>threshold:
            s.append(1)
        else:
            s.append(0)
    return np.array(s)


# In[4]:


sim_text=open("Word similarity/hindi.txt","r",encoding='utf-8')
sim_text=sim_text.read()
sim_li=[]
gro_th=[]
li_final=[]
for i in sim_text.split("\n"):
    if(len(i)<=1):
        break
    s=i.split(",")
    li_temp=[]
    li_temp.append(s[0])
    li_temp.append(s[1])
    li_final.append(s[0])
    li_final.append(s[1])
    sim_li.append(li_temp)
    gro_th.append(float(s[2]))


# In[5]:


gro_th=np.array(gro_th)
th_li=[4,5,6,7,8]
gro_th
dict1={}
for i in th_li:
    li=[]
    for j in gro_th:
        if j>=i:
            li.append(1)
        else:
            li.append(0)
    dict1[i]=li


# ## 50

# In[6]:


cbow50 = Word2Vec.load("hi/50/cbow/hi-d50-m2-cbow.model")
simCbow50_dict={}
for i in sim_li:
    s1=i[0]
    s2=i[1]
    simCbow50_dict[s1]=cbow50.wv[s1]
    simCbow50_dict[s2]=cbow50.wv[s2]


# In[8]:


k=0
cbow50_pair={4:[],5:[],6:[],7:[],8:[]}
for j in th_li:
    li1=[]
    k=0
    cosim50=[]
    for i in sim_li:
        s1=i[0]
        s2=i[1]
        li=[]
        t=cosine_similarity(simCbow50_dict[s1],simCbow50_dict[s2])*10
        cosim50.append(t)
        li.append(s1)
        li.append(s2)
        li.append(t)
        li.append(gro_th[k])
        k+=1
        if t>=j:
            li.append(1)
        else:
            li.append(0)
        li1.append(li)
    cbow50_pair[j]=li1


acc_li50_cbow={}
for i in th_li:
    temp=thresholding(cosim50,i)
    acc_li50_cbow[i]=(accuracy(temp,dict1[i]))
    
for i in th_li:
    temp=thresholding(cosim50,i)
    acc_li50_cbow[i]=t=(accuracy(temp,dict1[i]))
    df={"Word1":[],"Word2":[],"Similarity Score":[],"Ground Truth Similarity Score":[],"Label":[]}
    for j in cbow50_pair[i]:
        df["Word1"].append(j[0])
        df["Word2"].append(j[1])
        df["Similarity Score"].append(j[2])
        df["Ground Truth Similarity Score"].append(j[3])
        df["Label"].append(int(j[4]))
    s="./output/"+"Q1_CBOW"+str(50)+"_similarity_"+str(i)
    df["Word1"].append("_")
    df["Word2"].append("Accuracy")
    df["Similarity Score"].append(t*100)
    df["Ground Truth Similarity Score"].append("")
    df["Label"].append("")
    df2=pd.DataFrame(df)
    df2.to_csv(s,index=None)


# In[ ]:





# ## 100

# In[9]:


cbow100 = Word2Vec.load("hi/100/cbow/hi-d100-m2-cbow.model")
simCbow100=[]
simCbow100_dict={}
for i in sim_li:
    s1=i[0]
    s2=i[1]
    simCbow100_dict[s1]=cbow100.wv[s1]
    simCbow100_dict[s2]=cbow100.wv[s2]


cbow100_pair={4:[],5:[],6:[],7:[],8:[]}
for j in th_li:
    li1=[]
    k=0
    cosim100=[]
    for i in sim_li:
        s1=i[0]
        s2=i[1]
        li=[]
        t=cosine_similarity(simCbow100_dict[s1],simCbow100_dict[s2])*10
        cosim100.append(t)
        li.append(s1)
        li.append(s2)
        li.append(t)
        li.append(gro_th[k])
        k+=1
        if t>=j:
            li.append(1)
        else:
            li.append(0)
        li1.append(li)
    cbow100_pair[j]=li1
    
acc_li100_cbow={}
for i in th_li:
    temp=thresholding(cosim100,i)
    acc_li100_cbow[i]=(accuracy(temp,dict1[i]))

for i in th_li:
    temp=thresholding(cosim100,i)
    acc_li100_cbow[i]=t=(accuracy(temp,dict1[i]))
    df={"Word1":[],"Word2":[],"Similarity Score":[],"Ground Truth Similarity Score":[],"Label":[]}
    for j in cbow100_pair[i]:
        df["Word1"].append(j[0])
        df["Word2"].append(j[1])
        df["Similarity Score"].append(j[2])
        df["Ground Truth Similarity Score"].append(j[3])
        df["Label"].append(j[4])
    s="./output/"+"Q1_CBOW"+str(100)+"_similarity_"+str(i)
    df["Word1"].append("_")
    df["Word2"].append("Accuracy")
    df["Similarity Score"].append(t*100)
    df["Ground Truth Similarity Score"].append("")
    df["Label"].append("")
    df2=pd.DataFrame(df)
    df2.to_csv(s,index=None)
acc_li100_cbow


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




