#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Task #1
for i in range(11):
    if i == 0:
        print(i,i)
    else:
        current_num = i
        pre_num = i - 1
        succeeding_num = current_num + pre_num
        print(succeeding_num,i)


# In[12]:


# Task #2
for i in range(6):
    x = i
    if x == 0:
        print(x)
    else:
        print(str(x) * i)


# In[26]:


# Task #3

list = [12,75,150,180,145,525,50]
my_list = []
for i in list:
    if i > 150:
        if i > 500:
            break
        continue
    if i % 5 == 0:
        my_list.append(i)
        print(i)
print(my_list)
    
    


# In[43]:


# Task #4
def fib_series(n):
    a,b = 0,1
    f_series = []
    for _ in range(n):
        f_series.append(a)
        a,b = b, a + b
    return f_series
num_times = 10
result = fib_series(num_times)
print(result)
        


# In[2]:


# Task #5
def calculate_factorial(n):
    factorial = 1
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            factorial *= i

        return factorial
number = int(input("Enter a number to find its factorial: "))

result = calculate_factorial(number)
print(f"The factorial of {number} is: {result}")


# In[5]:


# Task #6
def count_occurrences(lst):
    count_dict = {}  
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
            
    print("Printing count of each item:", end=" ")
    for key, value in count_dict.items():
        print(f"{key}: {value}", end=", ")

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count_occurrences(sample_list)


# In[7]:


# Task #7
def create_l3(l1, l2):
    l3 = [] 

    for i in range(len(l1)):
        if i % 2 != 0: 
            l3.append(l1[i]) 

    for i in range(len(l2)):
        if i % 2 == 0: 
            l3.append(l2[i]) 

    return l3

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

result = create_l3(l1, l2)
print("Third list (l3) combining odd-index elements from l1 and even-index elements from l2:", result)


# In[ ]:




