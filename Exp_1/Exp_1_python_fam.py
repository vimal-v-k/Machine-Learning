#!/usr/bin/env python
# coding: utf-8

# # Arithmetic Operators

# In[16]:


a=5
print(a)
print(type(a))


# In[7]:


f=1.5
print(f)
print(type(f))


# In[8]:



s="hello" 
print(s)
print(type(s))



# In[9]:


b=True 
print(b)
print(type(b))

 


# In[10]:


t=5+3j 
print(t)
print(type(t))


# # Boolean Operations

# In[12]:


T=True
F=False

print(T,F)


# In[13]:


p = 5 > 3

print(p)


# In[14]:


q = -1 < -12.5

print(q)


# In[15]:


print(p and q)
print(p or q)
print(not q)


# # Some String Operations

# In[18]:


s = 'hello' 
u = "hello"
print(s)
print(u)


# In[19]:


s1 = "python"
s2 = 'world'
s3 = s1 + ' ' + s2
print(s3)


# In[20]:


s3 = '%s %s %d' %(s1, s2, 1011)
print(s3)


# In[21]:


print(len(s3))


# In[22]:


print(s3.upper())


# In[23]:


print(s3.capitalize())


# In[24]:


print(s3.lower())


# In[25]:


print('hello world how are you'.split(' '))


# In[26]:


print('book'.replace('o','e'))


# In[27]:


word = 'jewellery'
print(word.find('well'))
print(word.find('is'))


# # Control Structures

# In[30]:


number = 987
if number > 99 and number < 1000:
    print('3 digit')
else:
    print('Not 3 digit')


# In[32]:


response = input('Are you familiar with python :')

if response.upper() == "YES":
    print("You can skip this course :-|") 
elif response.upper() == "NO":
    print("You are at the right place :-)")
else:
    print('Sorry wrong input :-(')


# In[33]:


for x in range(10):
    print(x,end=' ')


# In[37]:


limit = int(input('Enter a limit : ')) 
sum = 0

for i in range(1,limit + 1): 
    if i%2 !=0:
        sum += i
    
print("Odd sum = "+str(sum))


# In[38]:


print(list(range(10)))

print(list(range(1,10)))

print(list(range(1,10,2)))


# In[41]:


number = int(input('Enter number : ')) 
s = 0

while number > 0 :
    s += number%10
    number = number//10
print(s)


# In[45]:


limit = int(input('Enter number : ')) 
for num in range(2,limit+1):
    is_divisible = False
    k=2

    while k <= num//2 :
        if num % k == 0:
            is_divisible=True
            break;
        k += 1

    if not is_divisible:
        print(num,end=' ')


# # Containers

# # LIST

# In[101]:


# mylist = ['a','b', 1, 1.2, True]
print(mylist)


# In[49]:


mylist.append('new')

print(mylist)


# In[51]:



print(mylist.pop())
print(mylist)


# In[55]:


mylist.insert(2,'new')
print(mylist)


# In[54]:


mylist.remove('new')
print(mylist)


# In[56]:


b = [1,2,3]
mylist.append(b)
print(mylist)


# In[57]:


mylist.remove(b)
print(mylist)


# In[58]:


mylist.extend(b)
print(mylist)


# In[60]:


a = [2,3,1,4,5]
a.sort()

print(a)


# In[61]:


print(list('hello'))


# In[63]:


print(a[1],a[-1])


# In[65]:


sliced = a[2:7]

print(sliced)


# In[66]:


sliced = a[3:]
print(sliced)


# In[67]:


numbers = list(range(1, 8))

print(numbers)


# In[68]:


square = []

for i in numbers:
    square.append(pow(i,2))
    
print(square)


# In[69]:


odd_square =[x**2 for x in numbers if x%2 != 0]
print(odd_square)


# In[70]:


square = [x**2 for x in numbers]
print(square)


# # Dictionary

# In[71]:


person = {'name' : 'Manu', 'age': 28}
print(person['name'])


# In[72]:


print('name' in person)


# In[73]:


print('sex' in person)


# In[74]:


person['sex'] = 'male'

print(person)


# In[75]:


for item in person:
    print(item,person[item])


# In[76]:


for (key,value) in person.items():
    print(key.capitalize(),'\t:\t', value)


# In[77]:


print(person.keys())


# # Tuples

# In[78]:


t1 = (1,2,3)
t2 = 4,5,6
print(t1,t2)


# In[79]:


t3 = t1 +t2
print(t3)


# In[80]:


lt = tuple(['a','b','c','d'])
print(lt)


# In[82]:


s = (3)
print(type(s))

s = (3,)
print(type(s))


# # Sets

# In[83]:


s = {1,2,3}
print(s,type(s))


# In[84]:


fset = {"apple", "banana", "cherry"}
fset.remove("banana")

print(fset)


# In[85]:


fset = {"apple", "banana", "cherry"}
fset.discard("banana")

print(fset)


# In[86]:


fset = {"apple", "banana", "cherry"}
fset.clear()

print(fset)


# In[88]:


set1 = {"a", "b" , "c"} 
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# In[89]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)


# In[90]:


lst = [1,2,3,4,5,5,5,7,6]

myset = list(set(lst))
print(myset)


# # Functions

# In[91]:


def twice(number):
    return 2*number

t = twice(5)
print(t)


# In[93]:


def isPrime(number):
    for factor in range(2, (number//2)+1): 
        if number%factor == 0:
            return False

    return True

number = int(input('Enter the number '))
print(isPrime(number))


# In[94]:


def printPrimes(llimit, ulimit):
    
    for num in range(llimit, ulimit + 1):
        
        if isPrime(num) == True:
            print(num, end = ' ')

printPrimes(5,50)


# In[97]:


def swap(x,y):
    t = x
    x = y
    y = t
    return x,y


# In[98]:


b=7
a,b = swap(a,b)
print(a,b)


# # Classes

# In[99]:


class Adder:

    def init(self):
        self.x = 0
        self.y = 0

    def setValues(self, x, y):
        self.x = x
        self.y = y
        
    def calculate(self1):
        self1. sum = self1.x + self1. y
        
    def getSum(self): 
        return self.sum


# In[100]:


adder = Adder()
adder.setValues(5,4)

adder.calculate()

print(adder.getSum())


# In[ ]:




