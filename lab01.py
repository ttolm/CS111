#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#0, "None", '' '', '[]' are all false values, everything else is false
# and evaluates to True only if both operands evaluate to True; if at least one operand is False, then and evaluates to False
# True and 13
# False or 0
# not 10
# not None
# # True and 1/0 and False
# True or 1/0 or False
# False or 1
# 1 and 3 and 6 and 10 and 15
# -1 and 1 > 0
# 0 or False or 2 or 1/0
# not 0
# (1 + 1) and 1
# 1/0 or True
# (True or False) and False


# In[44]:


# def func(a, b):
#     if a == 4:
#         return 6
#     elif b % 2 == 0:
#         return a // 2
#     else:
#         return 3 * b + 1

# print(func(10, 6)) #5
# print(func(4, 6)) #6
# print(func(0, 3)) #10


# In[48]:


# def how_big(x):
#     if x > 10:
#         print('huge')
#     elif x > 5:
#         print('big')
#     elif x > 0:
#         print('small')
#     else:
#         print("nothing")
        
# print(how_big(7)) #big
# print(how_big(12)) #huge
# print(how_big(-1)) #nothing 

#because there is no return statement, it also prints 'None', because that is a function's type


# In[49]:


# n = 3
# while n >= 0:
#     n -= 1
#     print(n)
#n = 3, returns 2
#n = 2, returns 1
#n = 1, returns 0
#n = 0, returns -1


# In[ ]:


# positive = 13
# while positive:
#     print("positive?")
#     positive -= 3
    
#triggers an infinite loop because all values (except 0) are True


# In[56]:


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    result = 1
    for i in range(k):
        result *= n
        n -= 1
    return result


# In[3]:


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    result = 0
    while y > 0:
        result += y % 10
        y //= 10
    return result

