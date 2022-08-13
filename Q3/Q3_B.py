#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import time
import pickle


# In[7]:


#storing all alphabets
alphabets=['ऄ','अ','आ','इ','ई','उ','ऊ','ऋ','ऌ','ऍ','ऎ','ए','ऐ','ऑ','ऒ','ओ','औ','क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट',
'ठ','ड','ढ','ण','त','थ','द','ध','न','ऩ','प','फ','ब','भ','म','य','र','ऱ','ल','ळ','ऴ','व','श','ष','स','ह']
#storing all vowels
vowels=['ऄ','अ','आ','इ','ई','उ','ऊ','ऋ','ऌ','ऍ','ऎ','ए','ऐ','ऑ','ऒ','ओ','औ','अ:']
#storing all consonets
consonant=['क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट',
'ठ','ड','ढ','ण','त','थ','द','ध','न','ऩ','प','फ','ब','भ','म','य','र','ऱ','ल','ळ','ऴ','व','श','ष','स','ह']
#storing all matra
matra=['ऀ','ँ','ं','ः','ऺ','ऻ','़','ा','ि','ी','ु','ू','ृ','ॄ','ॅ','ॆ','े','ै','ॉ','ॊ','ो','ौ','्','ॎ','ॏ','ॕ','ॖ','ॗ']
all_chars=vowels+consonant+matra


# In[3]:


def cleaning_text(data):
    #cleaning each line by removing all uncessory char's
    s=''
    for i in data:
        if i not in all_chars:
            s+=' '
        else:
            # if i (char) in all_char simply add that char else add space " "
            s+=i
    return s

def find_n_gram(wordli,n):
    ngrams = []
    #iterating len(word)-n+1 time to get n_gram
    for i in range(len(wordli)-(n-1)):
        s=''
        for j in wordli[i:i+n]:
            s+=j+" "
        #remove last extra space 
        s=s.rstrip()
        ngrams.append(s)
    return ngrams


# In[4]:


#for example.
f="""आवेदन करने की आखिरी तारीख 31 जनवरी, 2020 है।\n"""
cleaning_text(f).split()
find_n_gram(cleaning_text(f).split(),4)


# In[ ]:





# In[9]:


unigram_dict_word={}
bigram_dict_word={}
trigram_dict_word={}
for file in os.listdir("./data/"):
    print(file)
    start1=time.time()
    f= open("./data/"+file,encoding='utf-8')
    end1=time.time()
    print(end1-start1)
    start2=time.time()
    count=0
    #iterating over each line of given file
    for word in f:
        #clean current line and split it into words
        temp1=cleaning_text(word)
        temp2=temp1.split()
        pro_li=temp2
        #updating word's in unigram_dict_word dictinary
        for i in pro_li:
            if i in unigram_dict_word:
                unigram_dict_word[i]+=1
            else:
                unigram_dict_word[i]=1
        #finding bigrams using pro_li
        bi_gram=find_n_gram(pro_li,2)
        #updating word's in bigram_dict_word dictinary
        for t1 in bi_gram:
            if t1 in bigram_dict_word:
                bigram_dict_word[t1]+=1
            else:
                bigram_dict_word[t1]=1
        #finding trigrams using pro_li
        tri_gram=find_n_gram(pro_li,3)
        #updating word's in trigram_dict_word dictinary        
        for t2 in tri_gram:
            if t2 in trigram_dict_word:
                trigram_dict_word[t2]+=1
            else:
                trigram_dict_word[t2]=1
    end2=time.time()
    print(end2-start2)
    break


# In[17]:


#sorting each dictinary
tkn1=dict(sorted(unigram_dict_word.items(), key=lambda x: x[1], reverse=True))
tkn2=dict(sorted(bigram_dict_word.items(), key=lambda x: x[1], reverse=True))
tkn3=dict(sorted(trigram_dict_word.items(), key=lambda x: x[1], reverse=True))


# In[ ]:





# In[5]:


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


# In[ ]:





# In[10]:


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


# In[ ]:





# In[ ]:




