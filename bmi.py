#!/usr/bin/env python
# coding: utf-8

# In[178]:


class BMI:
    def __init__(self,name,age,tizhong,shengao):
        self.name = name
        self.age = age
        self.tizhong = tizhong
        self.shengao = shengao
        n = self.tizhong/(self.shengao*self.shengao)
        if n<18.5:
            d = "偏瘦"
        elif 18.5<=n<24:
            d = "正常"
        elif 24<=n<30:
            d = "偏胖"
        else:
            d = "肥胖"
        self.d=d
    def say_name(self):
        print("我是{n}".format(n=self.name))
    def say_age(self):
        print("{n}的年龄是{a}".format(n=self.name,a=self.age))
    def say_tizhong(self):
        print("{n}的体重是{b}".format(n=self.name,b=self.tizhong))
    def say_shengao(self):
        print("{n}的身高是{c}".format(n=self.name,c=self.shengao))
    def say_bmi(self):
        print("{n}的bmi是{d}".format(n=self.name,d=self.d))


# In[179]:


bmi1 = BMI("zhaosi",18,70,1.75)


# In[180]:


bmi1.say_age()


# In[181]:


bmi1.say_tizhong()


# In[182]:


bmi1.say_shengao()


# In[183]:


bmi1.say_bmi()

