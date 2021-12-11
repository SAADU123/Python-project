#!/usr/bin/env python
# coding: utf-8

# In[2]:


#creating class and 5 different departments :
import random as r
class employee():
    def dep1(self):
        #looping statement :for loop used
        for i in range(1,7):
            fd = r.randint(1,5000)
            print("dep1 ID's  : ",fd)
        #conditional structure if/else condition used
        if(i>=10):
            print("count matched is :",i,": got 10 or more employee! and validated")                
        else:
            print("count matched is :",i,":it's less than 10 employee! can't validate !")
    def dep2(self):
        for i in range(1,11):
            fd = r.randint(1,5000)
            print("dep2 ID's  : ",fd)
        if(i>=10):
            print("count matched is :",i,": got 10 or more employee! and validated")                
        else:
            print("count matched is :",i,":it's less than 10 employee! can't validate !")
    def dep3(self):
        for i in range(1,12):
            fd = r.randint(1,5000)
            print("dep3 ID's  : ",fd)
        if(i>=10):
            print("count matched is :",i,": got 10 or more employee! and validated")                
        else:
            print("count matched is :",i,":it's less than 10 employee! can't validate !")
    def dep4(self):
        for i in range(1,11):
            fd = r.randint(1,5000)
            print("dep4 ID's  : ",fd)
        if(i>=10):
            print("count matched is :",i,": got 10 or more employee! and validated")                
        else:
            print("count matched is :",i,":it's less than 10 employee! can't validate !")
    def dep5(self):
        for i in range(1,2):
            fd = r.randint(1,5000)
            print("dep5 ID's  : ",fd)
        if(i>=10):
            print("count matched is :",i,": got 10 or more employee! and validated")                
        else:
            print("count matched is :",i,":it's less than 10 employee! can't validate !")

#object creation for class employee and function calling         
f= employee()  
f.dep1()
f.dep2()
f.dep3()
f.dep4()
f.dep5()


# In[ ]:




