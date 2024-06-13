#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().run_line_magic('pinfo', 'dictionary')
d = {"Name":"Ram" , "Age":23}


# In[8]:


d = {"Name":"Ram" , "Age":23}


# In[12]:


if "Age" in d:
    print("already exsists")
else:
    print("no")


# In[13]:


get_ipython().run_line_magic('pinfo', 'dictionaries')
d={"Name":"Ram" , "Age":23}
d1={"City": "Salem", "Gender": "Male"}


# In[22]:


d={"Name":"Ram" , "Age":23}
d1={"City": "Salem", "Gender": "Male"}

a=d.copy()
print(d)
a=d1.copy()
print(a)



# In[23]:


d={"Name":"Ram" , "Age":23}
d1={"City": "Salem", "Gender": "Male"}
merged_dict = {**d, **d1}
print(merged_dict)


# In[24]:


d.update(d1)


# In[25]:


print(d)


# In[30]:


a={'Name': 'Ram', 'Age': 23, 'City': 'Salem', 'Gender': 'Male'}


# In[34]:


if "rage" in a:
    print("rage")
else:
    print("key not found")


# In[35]:


a.update({"car":"Thar"})


# In[36]:


print(a)


# In[44]:


if "bike" in a:
    print("found")
else:
    print("not found")


# In[46]:


a.pop("car")


# In[47]:


print(a)


# In[48]:


len(a)


# In[51]:


a.update({"Age":23})


# In[52]:


print(a)


# In[54]:


a.popitem()


# In[55]:


a.update({"Age":23})


# In[56]:


print(a)


# In[57]:


a.update({"Age":31})


# In[58]:


print(a)


# In[61]:


a["car"]= "Thar"


# In[62]:


print(a)


# In[63]:


marks={"science":41, "maths":42, "social science": 78, "english": 79}


# In[84]:


a=marks.values()
print(a)


# In[85]:


print(a)


# In[94]:


b=0
for i in a:
    if i>0:
        b=b+i
print(b)


# In[95]:


avg_marks=b/len(a)


# In[96]:


print(avg_marks)


# In[97]:


def find_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return anagrams

word_list = ["listen", "silent", "hello", "world", "dog", "god"]
anagram_dict = find_anagrams(word_list)
print(anagram_dict)


# In[ ]:




