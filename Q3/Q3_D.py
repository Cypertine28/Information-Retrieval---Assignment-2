#!/usr/bin/env python
# coding: utf-8

# In[43]:


import matplotlib.pyplot as plt
import pickle
import os


# ## For characters

# In[44]:


li=[]
for i in os.listdir("./q3d_files/chars/"):
    li.append(i)
li


# In[45]:


## Unigram_chars
f=open('./q3d_files/chars/all_unigram_char.pickle','rb')
data=pickle.load(f)
f.close()
all_unigram_chars=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_unigram_chars:
    x_axis.append(k)
    k+=1
    y_axis.append(all_unigram_chars[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="Unigram_Char")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
fig1=plt.gcf()
plt.draw()
fig1.savefig("output_graphs/Unigram_char.jpeg",dpi=100)


# In[ ]:





# In[46]:


## bigram_chars
f=open('./q3d_files/chars/all_bigram_char.pickle','rb')
data=pickle.load(f)
f.close()
all_bigram_chars=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_bigram_chars:
    x_axis.append(k)
    k+=1
    y_axis.append(all_bigram_chars[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="bigram_char")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
fig1=plt.gcf()
plt.draw()
fig1.savefig("output_graphs/Bigram_char.jpeg",dpi=100)


# In[47]:


## trigram_chars
f=open('./q3d_files/chars/all_trigram_char.pickle','rb')
data=pickle.load(f)
f.close()
all_trigram_chars=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_trigram_chars:
    x_axis.append(k)
    k+=1
    y_axis.append(all_trigram_chars[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="trigram_char")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
fig1=plt.gcf()

plt.draw()
fig1.savefig("output_graphs/Trigram_char.jpeg",dpi=100)


# In[48]:


## quadgram_chars
f=open('./q3d_files/chars/all_quadgram_char.pickle','rb')
data=pickle.load(f)
f.close()
all_quadgram_chars=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_quadgram_chars:
    x_axis.append(k)
    k+=1
    y_axis.append(all_quadgram_chars[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="quadgram_char")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()

fig1=plt.gcf()
plt.draw()
fig1.savefig("output_graphs/quadgram_char.jpeg",dpi=100)


# ## Syllable

# In[49]:


li=[]
for i in os.listdir("./q3d_files/syllable/"):
    li.append(i)
li


# In[50]:


## unigram_syllable
f=open('./q3d_files/syllable/all_unigram_syl.pickle','rb')
data=pickle.load(f)
f.close()
all_unigram_syl=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_unigram_syl:
    x_axis.append(k)
    k+=1
    y_axis.append(all_unigram_syl[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="unigram_syllable")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
fig1=plt.gcf()

plt.draw()
fig1.savefig("output_graphs/unigram_Syllable.jpeg",dpi=100)


# In[51]:


## bigram_syllable
f=open('./q3d_files/syllable/all_bigram_syl.pickle','rb')
data=pickle.load(f)
f.close()
all_bigram_syl=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_bigram_syl:
    x_axis.append(k)
    k+=1
    y_axis.append(all_bigram_syl[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="bigram_syllable")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
fig1=plt.gcf()

plt.draw()
fig1.savefig("output_graphs/Bigram_Syllable.jpeg",dpi=100)


# In[52]:


## trigram_syllable
f=open('./q3d_files/syllable/all_trigram_syl.pickle','rb')
data=pickle.load(f)
f.close()
all_trigram_syl=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_trigram_syl:
    x_axis.append(k)
    k+=1
    y_axis.append(all_trigram_syl[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="trigram_syllable")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
fig1=plt.gcf()

plt.draw()
fig1.savefig("output_graphs/trigram_Syllable.jpeg",dpi=100)


# ## Words

# In[53]:


li=[]
for i in os.listdir("./q3d_files/word/"):
    li.append(i)
li


# In[54]:


## unigram_word
f=open('./q3d_files/word/all_unigram_word.pickle','rb')
data=pickle.load(f)
f.close()
all_unigram_word=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_unigram_word:
    x_axis.append(k)
    k+=1
    y_axis.append(all_unigram_word[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="unigram_word")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
fig1=plt.gcf()

plt.draw()
fig1.savefig("output_graphs/unigram_word.jpeg",dpi=100)


# In[ ]:





# In[55]:


## bigram_word
f=open('./q3d_files/word/all_bigram_word.pickle','rb')
data=pickle.load(f)
f.close()
all_bigram_word=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_bigram_word:
    x_axis.append(k)
    k+=1
    y_axis.append(all_bigram_word[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="bigram_word")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
fig1=plt.gcf()

plt.draw()
fig1.savefig("output_graphs/bigram_word.jpeg",dpi=100)


# In[56]:


## trigram_word
f=open('./q3d_files/word/all_trigram_word.pickle','rb')
data=pickle.load(f)
f.close()
all_trigram_word=dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:100])
x_axis=[]
y_axis=[]
k=0
for i in all_trigram_word:
    x_axis.append(k)
    k+=1
    y_axis.append(all_trigram_word[i])
#ploting graph
fig=plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)
plt.plot(x_axis,y_axis,label="trigram_syllable")
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.legend()
fig1=plt.gcf()

plt.draw()
fig1.savefig("output_graphs/trigram_word.jpeg",dpi=100)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




