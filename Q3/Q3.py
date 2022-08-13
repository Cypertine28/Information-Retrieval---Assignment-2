#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# ## Characters

# In[2]:


## Unigram_chars
f=open('q3d_files/chars/all_unigram_char.pickle','rb')
data1=pickle.load(f)
f.close()

## bigram_chars
f=open('./q3d_files/chars/all_bigram_char.pickle','rb')
data2=pickle.load(f)
f.close()

## trigram_chars
f=open('./q3d_files/chars/all_trigram_char.pickle','rb')
data3=pickle.load(f)
f.close()

## quadgram_chars
f=open('./q3d_files/chars/all_quadgram_char.pickle','rb')
data4=pickle.load(f)
f.close()


# In[3]:


tkn1=dict(sorted(data1.items(), key=lambda x: x[1], reverse=True)[:100])
file=open("./top 100 ngram output/Top 100 unigram Characters.txt","w",encoding="utf-8")
c=1
for i in tkn1:
    file.write(i+"\n")
    c+=1
file.close()



tkn2=dict(sorted(data2.items(), key=lambda x: x[1], reverse=True)[:100])
file=open("./top 100 ngram output/Top 100 Bigram Characters.txt","w",encoding="utf-8")
c=1
for i in tkn2:
    file.write(i+"\n")
    c+=1
file.close()



tkn3=dict(sorted(data3.items(), key=lambda x: x[1], reverse=True)[:100])
file=open("./top 100 ngram output/Top 100 trigram Characters.txt","w",encoding="utf-8")
c=1
for i in tkn3:
    file.write(i+"\n")
    c+=1
file.close()


tkn4=dict(sorted(data4.items(), key=lambda x: x[1], reverse=True)[:100])
file=open("./top 100 ngram output/Top 100 Quadgram Characters.txt","w",encoding="utf-8")
c=1
for i in tkn4:
    file.write(i+"\n")
    c+=1
file.close()


# In[ ]:





# ## Words

# In[4]:


## Unigram_word
f=open('./q3d_files/word/all_unigram_word.pickle','rb')
data1=pickle.load(f)
f.close()
tkn1=dict(sorted(data1.items(), key=lambda x: x[1], reverse=True)[:100])

## bigram_word
f=open('./q3d_files/word/all_bigram_word.pickle','rb')
data2=pickle.load(f)
f.close()

tkn2=dict(sorted(data2.items(), key=lambda x: x[1], reverse=True)[:100])

## trigram_words
f=open('./q3d_files/word/all_trigram_word.pickle','rb')
data3=pickle.load(f)
f.close()
tkn3=dict(sorted(data3.items(), key=lambda x: x[1], reverse=True)[:100])


# In[5]:


file=open("./top 100 ngram output/Top 100 unigram words.txt","w",encoding="utf-8")
c=1
for i in tkn1:
    file.write(i+"\n")
    c+=1
file.close()



file=open("./top 100 ngram output/Top 100 Bigram words.txt","w",encoding="utf-8")
c=1
for i in tkn2:
    file.write(i+"\n")
    c+=1
file.close()



file=open("./top 100 ngram output/Top 100 trigram words.txt","w",encoding="utf-8")
c=1
for i in tkn3:
    file.write(i+"\n")
    c+=1
file.close()


# ## Syllable

# In[6]:


## Unigram_syllable
f=open('./q3d_files/syllable/all_unigram_syl.pickle','rb')
data1=pickle.load(f)
f.close()
tkn1=dict(sorted(data1.items(), key=lambda x: x[1], reverse=True)[:100])

## bigram_syllable
f=open('./q3d_files/syllable/all_bigram_syl.pickle','rb')
data2=pickle.load(f)
f.close()

tkn2=dict(sorted(data2.items(), key=lambda x: x[1], reverse=True)[:100])

## trigram_syllable
f=open('./q3d_files/syllable/all_trigram_syl.pickle','rb')
data3=pickle.load(f)
f.close()
tkn3=dict(sorted(data3.items(), key=lambda x: x[1], reverse=True)[:100])


# In[7]:


file=open("./top 100 ngram output/Top 100 unigram syllable.txt","w",encoding="utf-8")
c=1
for i in tkn1:
    file.write(i+"\n")
    c+=1
file.close()



file=open("./top 100 ngram output/Top 100 Bigram syllable.txt","w",encoding="utf-8")
c=1
for i in tkn2:
    file.write(i+"\n")
    c+=1
file.close()



file=open("./top 100 ngram output/Top 100 trigram syllable.txt","w",encoding="utf-8")
c=1
for i in tkn3:
    file.write(i+"\n")
    c+=1
file.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




