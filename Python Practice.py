#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=[1,2,3,4,5]
y = x[1:4]


# In[2]:


print(y)


# In[5]:


x="python"
x[2:5:2]


# In[2]:


6-7


# In[3]:


2*3


# In[5]:


12345-765432


# In[6]:


5345*7845


# In[7]:


5678/45


# In[3]:


a=45
type(a)



# In[11]:


a= "ankita"
type(a)
print(a)


# In[12]:


5>4


# In[13]:


123>45


# In[14]:


56>12345


# # Data types

# In[21]:


x=7854


a= x//1000
b= x//100%10
c= x//10%10
d= x%10

print(a)
print(b)
print(c)
print(d)


# In[25]:


x=6523

a=x//1000
b=x//100%10
c=x//10%10
d=x%10

print(a)
print(b)
print(c)
print(d)


# In[31]:


x=456321

a=x//100000
b=x//10000%10
c=x//1000%10
d=x//100%10
e=x//10%10
f=x%10
print(f)


# In[41]:


x=789652

a=x//100000
b=x//10000%10
c=x//1000%10
d=x//100%10
e=x//10%10
f=x%10
print(f)


# In[64]:


x=9874566

a=x//1000000
b=x//100000%10
c=x//10000%10
d=x//1000%10
e=x//100%10
f=x//10%10
g=x%10
print(b)


# In[89]:


x=7854

a=x//10000000
b=x//1000000%10
c=x//100000%10
d=x//10000%10
e=x//1000%10
f=x//100%10
g=x//10%10
h=x%10
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)


# In[91]:


x=74563214523

a=x//10000000000
b=x//1000000000%10
c=x//100000000%10
d=x//10000000%10
e=x//1000000%10
f=x//100000%10
g=x//10000%10
h=x//1000%10
i=x//100%10
j=x//10%10
k=x%10

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)


# In[93]:


x=7845561224568

a=x//1000000000000
b=x//100000000000%10
c=x//10000000000%10
d=x//1000000000%10
e=x//100000000%10
f=x//10000000%10
g=x//1000000%10
h=x//100000%10
i=x//10000%10
j=x//1000%10
k=x//100%10
l=x//10%10
m=x%10

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)


# In[1]:


x=8484151501515626

a=x//1000000000000000
b=x//100000000000000%10
c=x//10000000000000%10
d=x//1000000000000%10
e=x//100000000000%10
f=x//10000000000%10
g=x//1000000000%10
h=x//100000000%10
i=x//10000000%10
j=x//1000000%10
k=x//100000%10
l=x//10000%10
m=x//1000%10
n=x//100%10
o=x//10%10
p=x%10


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
print(p)


# In[3]:


z="apple"

type(z)


# In[4]:


x=input()


# In[5]:


type(x)


# In[7]:


x=int(input())


# In[8]:


type(x)


# In[16]:


x=bool(input())


# In[17]:


type(x)


# In[19]:


x=int(input())

type(x)


# In[22]:


x= 123456

if x%2==0:
    print("even")
else:
    print("odd")


# In[26]:


x=999999967453789
if x%2==0:
    print("even")
else:
    print("odd")


# In[28]:


x=input()

if x%2==0:
    print("even")
else:
    print("odd")


# In[4]:


if x%2==0:
    print("even")
else:
    print("odd")


# In[ ]:


x=input()


# In[31]:


if x%2 == 0:
    print("even")
else:
    print("odd")


# In[32]:


x=int(input())

if x%2==0:
    print("even")
else:
    print("odd")


# In[33]:


x=int(input())

if x%7==0:
    print("yes")
else:
    print("no")


# In[35]:


x=int(input())

if x%2==0:
    print("yes")
else:
    print("no")


# In[41]:


x=int(input())

if x%10%3==0:
    print('yes')
else:
    print('no')


# In[45]:


x=int(input())

if x//10%5==0:
    print("yes")
else:
    print("no")


# In[ ]:


check whether 2345678 is a multiple of 34


# In[1]:


x=int(input())

if x//34==0:
    print("yo")
else:
    print("nahh")


# In[ ]:


x=int(input())

if x


# In[2]:


x=int(input())

if x==5:
    print(l*b)
else:
    print(2*(l+b))


# In[10]:


x=int(input("enter the number:"))
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))

if x==5:
    print("area",l*b)
else:
    print("perimeter",2*(l+b))


# In[ ]:





# In[13]:


x=int(input("no. given by user:"))
r=int(input("radius given by user:"))

if x%11==0:
    print("circumference", 2*3.14*r)
else:
    print("area", 3.14*r**2)


# In[14]:


x=int(input("no. given by user:"))
r=int(input("radius given by user:"))

if x%11==0:
    print("circumference", 2*3.14*r)
else:
    print("area", 3.14*r**2)


# In[ ]:


#take the user input and check if there last two digitnumbers are divisible by 6 then calculate area of rectangle otherwise 
calculate the area of circle


# In[21]:


x=int(input("no. given by me:"))
l=int(input("length:"))
b=int(input("breadth:"))
r=int(input("radius:"))

if x%100%6==0:
    print('area of rectangle:', l*b)
else:
    print("area of circle", 3.14*r**2)


# In[22]:


if the guven no. is greater than 80 then calculate the permiter of rectangle otherwise permiter of square


# In[24]:


x=int(input("given by me:"))
l=int(input("length:"))
b=int(input("breadth:"))
s=int(input("sides:"))

if x>80:
    print("square", 4*s)
else:
    print("rectangle", 2*(l+b))


# In[25]:


x=int(input("given by me:"))
l=int(input("length:"))
b=int(input("breadth:"))
s=int(input("sides:"))

if x>80:
    print("rectangle", 2*(l+b))
else:
    print("square", 4*s)


# In[3]:


x=int(input())

if x>=18:
    print("yes")
else:
    print("no")


# In[4]:


x=int(input())

if x//7==0:
    print('yes')
else:
    print("no")


# In[6]:


x=int(input())

if x%2==0:
    print("even")
else:
    print("odd")


# In[19]:


x=int(input())

if x%5==0:
    print("hello")
else:
    print("bye")


# In[11]:


if x is greater than 20 calculate area of square otherwise perimeter


# In[12]:


x=int(input())
s=int(input())

if x>20:
    print("area", s**s)
else:
    print("peri", 4*s)


# In[16]:


x=int(input())
s=int(input())

if x<3:
    print("area", s**2)
else:
    print("peri", 4*s)


# In[18]:


x=int(input())
r=int(input())

if x%20==0:
    print("area of circle", 3.14*r**2)
else:
    print("peri", 2*3.14*r)


# In[29]:


x=int(input())

if x==356:
    print("leap year")
else:
    print(" non leap year")


# In[25]:


x=int(input())

if x%5==0:
    print("hell yeah")
else:
    print("hell no")


# In[26]:


x=int(input())

if x>80:
    print("yes")
else:
    print("no")


# In[ ]:


nested if else


# In[10]:


x=int(input())

if x>0 or x<80:
    print('yes')
else:
    print("no")


# In[16]:


x=int(input())
s=int(input())
l=int(input())
b=int(input())

if x>=100 and x<=200:
    print('sq-area', s**2)
else:
    print("rec-area", l*b)


# In[1]:


x=int(input())

if x>20 or x<10:
    if x%2==0:
        print('even')
    else:
        print('odd')
else:
    print('not in range')
    
    
    


# In[26]:


x=int(input())

if x%100%7==0:
    if x//2==0:
        print("even")
    else:
        print("odd")
else:
    print("not divisible")
        
 
        


# In[ ]:


43. Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:

# Input a number: 6                                                       
# 6 x 1 = 6                                                               
# 6 x 2 = 12                                                              
# 6 x 3 = 18                                                              
# 6 x 4 = 24                                                              
# 6 x 5 = 30                                                              
# 6 x 6 = 36                                                              
# 6 x 7 = 42                                                              
# 6 x 8 = 48  


# In[1]:


x=int(input())

if x==1:
    print(6*1)
elif x==2:
    print(6*2)
elif x==3:
    print(6*3)
elif x==4:
    print(6*4)
elif x==5:
    print(6*5)
elif x==6:
    print(6*6)
elif x==7:
    print(6*7)
elif x==8:
    print(6*8)
elif x==9:
    print(6*9)
elif x==10:
    print(6*10)
else:
    print("not found")


# In[ ]:


Write a Python program to find the median of three values.
# Expected Output:

# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0


# In[18]:


a=int(input("first no"))
b=int(input("second"))
c=int(input("third"))

if a<b and a>c or a<c and a>b:
    print("a")
elif b<a and b>c or b<c and b>a:
    print("b")
else: print("c")


# In[ ]:


Write a Python program that  representing a month and  prints the season for that month .
# Expected Output:

# Input the month (e.g. January, February etc.): july                                                                           
# Season is autumn


# In[17]:


x=int(input())

if x==1:
    print("january and winters")
elif x==2:
    print("feburary and winters")
elif x==3:
    print("March and autumn")
else:
    print("not found")


# In[ ]:


36. Write a Python program to check if a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.


# In[3]:


a=int(input())
b=int(input())
c=int(input())

if a==b and b==c and a==c:
    print("equi")
elif a==b or b==c or a==c :
    print("iso")
elif a>b or a>c and b>a or b>c and c>a or c>b:
    print('scalene')
else:
    print("not found")
        


# In[4]:


a=int(input())
b=int(input())
c=int(input())

if a==b and b==c and a==c:
    print("equi")
elif a>b or a>c and b>a or b>c and c>a or c>b:
    print('scalene')
else:
    print("iso")


# In[6]:


l=int(input())
b=int(input())

if l==b:
    print("square")
else:
    print("not")


# In[ ]:


X=int(input("eneter the absent days"))
y=int(input("enter the total days"))

present_days= y-x
present_percentage =(present_days/y*100)

print("i was present for",present_days, "days")
print("present persentage",present_percentage)

if present_precentage>75:
    print('yes')
else:
    print('no')


# In[ ]:


x=int(input("salary"))
y=int(input("experience"))

if y>=10:
    bonus=x*12%
    print("bonus")
elif y


# In[15]:


x=int(input("Marks"))

if x<=100 and x>91:
    print("A+")
elif x<90 and x>81:
    print("A")
elif x<=80 and x>71:
    print("B")
elif x<=70 and x>61:
    print("C")
elif x<=60 and x>51:
    print("D+")
elif x<=50 and x>41:
    print("D")
elif x>0 and x<=40:
    print("fail")
else:
    print("enter proper marks")


# In[18]:


x=int(input("first person"))
y=int(input("second person"))
z=int(input("third person"))

if x>y and x>z:
    print("x is oldest")
elif y>x and y>z:
    print("y is oldest")
else:
    print("z is oldest")


# In[23]:


x=int(input("days"))

if x>12:
    print("charges", x*5)
elif x==12 and x>8:
    print("charges", x*7)
elif x==8 and x>6:
    print("charges", x*8)
elif x==5 and x>0:
    print("charges", x*10)
    


# In[ ]:


practice slicing question---->


# In[3]:


x= 'I told my friend, "Python is my favorite language!"' "The language 'Python' is named after Monty Python, not the snake.""One of Python's strengths is its diverse and supportive community."

print(x)


# In[1]:


a=45
b=36
print(a,b)


# In[7]:


x=7854


a= x//1000
b= x//100%10
c= x//10%10
d=x%10
print(a,b,c,)


# In[14]:


x=74563214523


a= x%1000//10//10
print(a)


# In[29]:


x = [1,2,3,4,5,6,7,8,9,10,11,12]

# add apple before 10
# add 'orange' after 12
# add lichi after 2
# add pine apple after orange
# add 5000 before 1
# insert 100 after lichi
# add 90 after 9
# add 22 before 7
# remove 11 with help of indexing
# add guava after 3
# add blue berry after 4


# In[30]:


x.insert(9,"apple")
print(x)


# In[31]:


x.append("orange")


# In[32]:


print(x)


# In[33]:


x.insert(2,"lichi")


# In[34]:


print(x)


# In[35]:


x.append("pineapple")


# In[36]:


print(x)


# In[37]:


x.insert(0,5000)


# In[38]:


print(x)


# In[39]:


x.insert(4,100)


# In[40]:


print(x)


# In[41]:


x.insert(12,90)
print(x)


# In[42]:


x.insert(9,22)
print(x)


# In[43]:


x.pop(17)
print(x)


# In[46]:


x.insert(6,"guava")


# In[47]:


print(x)


# In[50]:


x.insert(8,"blueberry")


# In[51]:


print(x)


# In[52]:


len(x)


# In[ ]:


list1 = [5,10,15,20]
list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']

for i in x:
    


# In[17]:


x=[1,2,3,4,5]
a=[]
for i in x:
    if i==x[0]:
        x.append(i)
        x.pop(0)
    else:
        x.insert(0,x[-2])
        x.pop(4)
        break
print(x)
    
    


# In[ ]:


i=1  if i==x[0], i==1 True x.append(i) 1 is in last [1,2,3,4,5,1] x.pop(0) [2,3,4,5,1]
i=2  if i==x[0], i==2 False 
else
x.insert(0,x[-2])---> [5,2,3,4,5,1]
x.pop(4)----->  [5,2,3,4,1]
break


# In[ ]:


x="AD2T3E4"
a=""
b=""
c=""
d=""
for i in x:
    if i.isalpha():
        a=a+i
    else:
        b=i
        c=int(b)*a
        d=d+c
        a=""
print(d)


# In[ ]:


i="A"  if A.isalpha()  True  a=a+A  a=A
i="D"  if D.isapha()  True   a=a+D  a="AD"
i="2"  if 2.isalpha() False  (b=i, b=2) c=int(2)*a  c=int(2)*AD= ADAD d=""+ADAD



# In[ ]:




