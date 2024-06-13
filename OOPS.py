#!/usr/bin/env python
# coding: utf-8

# In[1]:


class pranshu:
    def name1(self):
        print('i am priyanka')
    
    def name2(self):
        print('i am aditya')
        
    def name3(self):
        print('i am arpit')
        
    def name4(self):
        print('i am harsh')


# In[2]:


obj = pranshu()


# In[3]:


obj.name1()


# In[4]:


obj.name4()


# In[5]:


class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
        
    def area(self):
        print(self.length * self.breadth)
        
    def perimeter(self):
        print(2*(self.length+ self.breadth))


# In[6]:


obj = rectangle(10,20)


# In[7]:


obj.area()


# In[8]:


obj.perimeter()


# In[9]:


# make the class of circle and find the area and circumference of the circle


# In[18]:


class circle:
    def __init__(self,r):
        self.radius=r
    
    def area(self):
        print(3.14**2*self.radius)
    def perimeter(self):
        print(2*3.14*self.radius)


# In[19]:


obj = circle(4)


# In[20]:


obj.area()


# In[21]:


obj.perimeter()


# In[31]:


class rectangle:
    def __init__(kajal,l,b):
        kajal.length=l
        kajal.breadth=b
        
    def area(rahul):
        print(rahul.length * rahul.breadth)
        
    def perimeter(uttam):
        print(2*(uttam.length+ uttam.breadth))


# In[32]:


obj = rectangle(10,20)


# In[33]:


obj.perimeter()


# In[34]:


obj.area()


# In[73]:


class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
        
    def area(self):
        print(self.length*self.breadth)
        
    def perimeter(self):
        print(2*(self.length+self.breadth))
        
    def __to_str__(self):
        print(f'this is length {self.length}, this is breadth {self.breadth}')


# In[74]:


obj=rectangle(5,10)


# In[75]:


obj.area()


# In[76]:


obj.__to_str__()


# In[81]:


class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
        
    def area(self):
        print(self.length*self.breadth)
        
    def perimeter(self):
        print(2*(self.length+self.breadth))
        
    def __str__(self):
        return(f'this is length {self.length}, this is breadth {self.breadth}')


# In[82]:


obj = rectangle (15,30)


# In[83]:


str(obj)


# In[91]:


class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
        
    def area(self):
        print(self.length*self.breadth)
        
    def perimeter(self):
        print(2*(self.length+self.breadth))
        
    def __str__(self):
        return(f'this is length {self.length}, this is breadth {self.breadth}')
    
    def __repr__(self):
        return(f'this {self.length}, this {self.breadth}')


# In[92]:


obj = rectangle(15,30)


# In[93]:


str(obj)


# In[94]:


obj


# In[95]:


print(obj)


# # Inheritence

# In[96]:


class father:
    def function1(self):
        print('I am father')
        
class child(father):
    def function2(self):
        print('I am child')


# In[97]:


obj = child()


# In[98]:


obj.function2()


# In[99]:


obj.function1()


# In[ ]:


father --> parent class --> base class

child --> child class --> derived class


# In[104]:


class grandfather:
    def function1(self):
        print('I am grandfather')
    
class father(grandfather):
    def function2(self):
        print('I am Father')
        
class child(father):
    def function3(self):
        print('I am child')


# In[105]:


obj = child()


# In[106]:


obj.function1()


# In[107]:


obj.function2()


# In[108]:


obj.function3()


# In[109]:


class grandfather:
    def function1(self):
        print('I am grandfather')
    
class father:
    def function2(self):
        print('I am Father')
        
class child(father,grandfather):
    def function3(self):
        print('I am child')


# In[112]:


obj=child()


# In[116]:


obj.function2()


# # task

# In[ ]:


class info:
    def name(self):
        name=input()
        print(name)
    def age(self):
        age=int(input())
        print(age)
        
    def gender(self):
        gender=input()
        print(gender)
    
    def salary(self):
        salary=int(input())
        print(salary)
    
    def city(self):
        city=input()
        print(city)
    
obj=info()



admin=input('admin: ')
password=input('password:  ')

attempt=0


while attempt<3:
    if admin=='ankita' and password=='yadav@123':
        print('You have successfully logged in')
        print(obj.name(),obj.age(),obj.gender(),obj.salary(),obj.city())
    else:
        print('incorrect information,Check if u have entered worng admin or password and try again')
        attempt +=1
        


# In[ ]:




