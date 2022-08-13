#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import time
import pickle
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


# In[7]:


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

def preprocess(word):
    #preprocessing given word like adding necessory '्'(halant) char after consonant
    res=[]
    #iterating over all chars of word
    for i in range(len(word)):
        try:
            #Ignore '्'(halant) char that is extra added.
            if word[i]=='्':
                continue
            #if given char is consonant and next char is in alphabets then add '्'(halant) and append 'अ'
            if word[i] in consonant  and word[i+1] in alphabets:
                res.append(word[i]+'्')
                res.append('अ')
            else:
                #if given char is consonant the add '्'(halant)  only
                if word[i] in consonant:
                    res.append(word[i]+'्')
                else:
                    #if char is not in consonat the simply add current char.
                    res.append(word[i])
        except:
            res.append(word[i])
            if word[i]in consonant:
                res[-1]+='्'
                res.append('अ')
    return res


# In[10]:


def correcting(s):
    #function that help to correct bi_gram,tri_gram,quad_gram word which is formed
    t=''
    i=0
    while i<len(s):
        #if current char is '्' (halant) and next char is matra then ignore current '्'(halant)
        if i!=len(s)-1 and s[i]=='्' and s[i+1] in matra:
            i+=1
            continue
        #if current word is vowel or matra then simply add
        if s[i] in vowels or s[i] in matra:
            t+=(s[i])
        #if current char is in consonat then check for further condition
        if s[i] in consonant:
            try:
                #if next char is '्' (halant)  then add according to i+2'th char
                if s[i+1]=='्':
                    if s[i+2] in consonant:
                        t+=s[i]+s[i+1]+s[i+2]
                        i+=2
                    elif s[i+2]=='अ':
                        t+=s[i]
                        i+=2
                    else:
                        t+=s[i]
                        t+=s[i+2]
                        i+=2
            except:
                #if out of index error occure then simply add current char
                t+=s[i]
        i=i+1
    return t


# In[8]:


def find_n_gram(wordli,n):
    ngrams = []
    #iterating len(word)-n+1 time to get n_gram
    for i in range(len(wordli)-(n-1)):
        s=''
        for j in wordli[i:i+n]:
            s+=j
        ngrams.append(s)
    return ngrams


# In[6]:


preprocess("अंतरराष्ट्रीय")


# In[8]:


#defining global uni_gram, bi_gram,tri_gram,quad_gram dictionary
unigram_dict={}
bigram_dict={}
trigram_dict={}
quadgram_dict={}
for file in os.listdir("../data/"):
    print(file)
    start1=time.time()
    f= open("../data/"+file,encoding='utf-8')
    end1=time.time()
    print(end1-start1)
    start2=time.time()
    count=0
    #iterating over each line of given file
    for word in f:
        #clean current line and split it into words
        temp1=cleaning_text(word)
        temp2=temp1.split()
        pro_li=[]
        for i in temp2:
            #tokenize each word which gives corresponding char's from given word
            pro_li=preprocess(i)
            #updating char's in Uni_gram dictinary
            for i in pro_li:
                if i in unigram_dict:
                    unigram_dict[i]+=1
                else:
                    unigram_dict[i]=1
            #finding Bigram using list contain all char's for given word
            bi_gram=find_n_gram(pro_li,2)
            #updating bigram in bi_gram dictinary
            for t1 in bi_gram:
                if t1 in bigram_dict:
                    bigram_dict[t1]+=1
                else:
                    bigram_dict[t1]=1
            #finding trigram using list contain all char's for given word
            tri_gram=find_n_gram(pro_li,3)
            #updating trigram in tri_gram dictinary
            for t2 in tri_gram:
                if t2 in trigram_dict:
                    trigram_dict[t2]+=1
                else:
                    trigram_dict[t2]=1
            #finding quadgram using list contain all char's for given word
            quad_gram=find_n_gram(pro_li,4)
            #updating quadgram in quad_gram dictinary
            for t3 in quad_gram:
                if t3 in quadgram_dict:
                    quadgram_dict[t3]+=1
                else:
                    quadgram_dict[t3]=1
    end2=time.time()
    print(end2-start2)
    


# In[54]:


## Unigram_chars
f=open('./q3d_files/chars/all_unigram_char.pickle','rb')
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


# In[55]:


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


# In[38]:


# d1={}
# d2={}
# d3={}
# d4={}
# for i in data1:
#     s=correcting(i)
#     d1[s]=data1[i]
# for i in data2:
#     s=correcting(i)
#     try:
#         if s[0] in consonant and s[1]=='्':
#             continue
#         else:
#             d2[s]=data2[i]
#     except:
#         d2[s]=data2[i]
# for i in data3:
#     s=correcting(i)
#     d3[s]=data3[i]
# for i in data4:
#     s=correcting(i)
#     d4[s]=data4[i]


# # In[51]:


# tkn1=dict(sorted(d1.items(), key=lambda x: x[1], reverse=True)[:100])
# file=open("./top 100 ngram output/Top 100 unigram Characters.txt","w",encoding="utf-8")
# c=1
# for i in tkn1:
#     file.write(i+"\n")
#     c+=1
# file.close()



# tkn2=dict(sorted(d2.items(), key=lambda x: x[1], reverse=True)[:100])
# file=open("./top 100 ngram output/Top 100 Bigram Characters.txt","w",encoding="utf-8")
# c=1
# for i in tkn2:
#     file.write(i+"\n")
#     c+=1
# file.close()



# tkn3=dict(sorted(d3.items(), key=lambda x: x[1], reverse=True)[:100])
# file=open("./top 100 ngram output/Top 100 trigram Characters.txt","w",encoding="utf-8")
# c=1
# for i in tkn3:
#     file.write(i+"\n")
#     c+=1
# file.close()


# tkn4=dict(sorted(d4.items(), key=lambda x: x[1], reverse=True)[:100])
# file=open("./top 100 ngram output/Top 100 Quadgram Characters.txt","w",encoding="utf-8")
# c=1
# for i in tkn4:
#     file.write(i+"\n")
#     c+=1
# file.close()


# In[46]:





# In[48]:





# In[50]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




