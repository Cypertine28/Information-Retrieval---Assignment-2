#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import time
import pickle


# In[2]:


alphabets=['ऄ','अ','आ','इ','ई','उ','ऊ','ऋ','ऌ','ऍ','ऎ','ए','ऐ','ऑ','ऒ','ओ','औ','क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट',
'ठ','ड','ढ','ण','त','थ','द','ध','न','ऩ','प','फ','ब','भ','म','य','र','ऱ','ल','ळ','ऴ','व','श','ष','स','ह']
vowels=['ऄ','अ','आ','इ','ई','उ','ऊ','ऋ','ऌ','ऍ','ऎ','ए','ऐ','ऑ','ऒ','ओ','औ','अ:']
consonant=['क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट',
'ठ','ड','ढ','ण','त','थ','द','ध','न','ऩ','प','फ','ब','भ','म','य','र','ऱ','ल','ळ','ऴ','व','श','ष','स','ह']
matra=['ऀ','ँ','ं','ः','ऺ','ऻ','़','ा','ि','ी','ु','ू','ृ','ॄ','ॅ','ॆ','े','ै','ॉ','ॊ','ो','ौ','्','ॎ','ॏ','ॕ','ॖ','ॗ']
all_chars=vowels+consonant+matra


# In[3]:


def cleaning_text(data):
    #cleaning each line by removing all uncessory char's
    s=''
    for i in data:
        # if i (char) in all_char simply add that char else add space " "
        if i not in all_chars:
            s+=' '
        else:
            s+=i
    return s



def find_n_gram(wordli,n):
    ngrams = []
    #iterating len(word)-n+1 time to get n_gram
    for i in range(len(wordli)-(n-1)):
        s=''
        for j in wordli[i:i+n]:
            s+=j
        ngrams.append(s)
    return ngrams

def preprocessing_word(word):
    li=[]
    for i in word:
        li.append(i)
    res=[]
    for i in range(len(li)):
        if li[i] not in matra:
            res.append(li[i])
        else:
            try:
                res[-1]=res[-1]+li[i]
            except:
                pass
    return res

def check_case2(li,i,s,flag,j):
    #checking given syllable is with '्'
    if li[i]==li[i][0]+'्':
        #j>=1 help to handle if more one incomplete char is there.
        if j>=1:
            s+=li[i+1]
        else:
            s+=li[i]+li[i+1]

        i+=1
        j+=1
    else:
        #update flag=false to break a loop
        flag=False
        i=i+1
    return s,i,flag,j

def check_case1(li,i):
    flag=True
    s=''
    j=0
    # check untill we didnt get char with next charecter is '्'
    while flag:
        try:
            s,i,flag,j=check_case2(li,i,s,flag,j)
        except:
            flag=False
            pass
    return s,i


# In[4]:


def tokenization(word):
    #doing preprocessing on each word so we can seperate each syllable from given word.
    li=preprocessing_word(word)
    i=0
    #list to store final results
    final=[]
    while i< len(li):
        #if pointer all last index of word then simply add it into result
        if i==len(li)-1:
            final.append(li[i])
            i+=1
            continue
        if li[i]==li[i][0]+'्': 
            #checking given syllable is with '्' if present then combine chars which gives single syllable
            s,i=check_case1(li,i)
            #add result in final list
            final.append(s)
        else:
            #if above condition is not satisfy then simply add into final list
            final.append(li[i])
            i+=1
    return final
    
#for example to token
tokenization('षड्यंत्र')


# In[ ]:


unigram_dict_syl={}
bigram_dict_syl={}
trigram_dict_syl={}
quadgram_dict_syl={}
for file in os.listdir("../data/"):
    start1=time.time()
    f= open("../data/"+file,encoding='utf-8')
    end1=time.time()
    print(end1-start1)
    start2=time.time()
    count=0
    for word in f:
        #remove extra spaces and unccessory characters from give line
        temp1=cleaning_text(word)
        #spliting each line so we get each word in list
        temp2=temp1.split()
        pro_li=[]
        #iterating over each word to find syllable
        for i in temp2:
            #Tokenizing each for in proper formate
            pro_li=tokenization(i)
            #getting list contain all syllable for given word
            #updating syllable in Uni_gram dictinary
            for i in pro_li:
                if i in unigram_dict_syl:
                    unigram_dict_syl[i]+=1
                else:
                    unigram_dict_syl[i]=1
            #finding Bigram using list contain all syllables of given word
            bi_gram=find_n_gram(pro_li,2)
            #updating bigram in bi_gram dictinary
            for t1 in bi_gram:
                if t1 in bigram_dict_syl:
                    bigram_dict_syl[t1]+=1
                else:
                    bigram_dict_syl[t1]=1
            #finding trigram using list contain all syllables of given word
            tri_gram=find_n_gram(pro_li,3)
            #updating trigram in tri_gram dictinary
            for t2 in tri_gram:
                if t2 in trigram_dict_syl:
                    trigram_dict_syl[t2]+=1
                else:
                    trigram_dict_syl[t2]=1
            #finding quadgram using list contain all syllables of given word
            quad_gram=find_n_gram(pro_li,4)
            #updating quadgram in quad_gram dictinary
            for t3 in quad_gram:
                if t3 in quadgram_dict_syl:
                    quadgram_dict_syl[t3]+=1
                else:
                    quadgram_dict_syl[t3]=1
    end2=time.time()
    print(end2-start2)
    print(file)


# In[ ]:


#Sorting each dictinary to get top 100 elemets.
tkn1=dict(sorted(unigram_dict_syl.items(), key=lambda x: x[1], reverse=True))
tkn2=dict(sorted(bigram_dict_syl.items(), key=lambda x: x[1], reverse=True))
tkn3=dict(sorted(trigram_dict_syl.items(), key=lambda x: x[1], reverse=True))
tkn4=dict(sorted(quadgram_dict_syl.items(), key=lambda x: x[1], reverse=True))


# In[ ]:


import pickle
f1=open('unigram_dict_syl.pickle','wb')
pickle.dump(tkn1,f1)
f1.close()
f2=open('bigram_dict_syl.pickle','wb')
pickle.dump(tkn2,f2)
f2.close()
f3=open('trigram_dict_syl.pickle','wb')
pickle.dump(tkn3,f3)
f3.close()
f4=open('quadgram_dict_syl.pickle','wb')
pickle.dump(tkn4,f4)
f4.close()


# In[ ]:





# ## For top 100

# In[5]:


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


# In[10]:


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

