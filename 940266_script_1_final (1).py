#!/usr/bin/env python
# coding: utf-8

# # LATE PAYMENT MODEL

# #### By : Faisal Dhio Saputra

# ## 1. Importing Data To Python

# In[185]:


import pymysql
import pandas as pd
import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# ### Load Dataset

# In[186]:


#Create connection to Mysql
conn=pymysql.connect(host='telkomathon.udata.id',port=int(33108),user='t_2021_user',passwd='WC843k48S',db='master')


# ### load data from sql per month

# In[4]:


TRAININGSET_TARGET=pd.read_sql_query("SELECT * FROM TRAININGSET_TARGET;",conn)


# In[5]:



TRAININGSET_POP=pd.read_sql_query("SELECT ID_CUSTOMER,LENGTH_OF_STAY,DIVRE_ID,TECHNOLOGY,KW,INDIHOME_TYPE,TOTAL_MINIPACK FROM TRAININGSET_POP;",conn)
TRAININGSET_SPEED=pd.read_sql_query("SELECT ID_CUSTOMER,Speed FROM TRAININGSET_SPEED;",conn)



TRAININGSET_USEE_USAGE_M1=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM TRAININGSET_USEE_USAGE WHERE PERIODE = 'M1';",conn)
TRAININGSET_USEE_USAGE_M2=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM TRAININGSET_USEE_USAGE WHERE PERIODE = 'M2';",conn)
TRAININGSET_USEE_USAGE_M3=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM TRAININGSET_USEE_USAGE WHERE PERIODE = 'M3';",conn)
TRAININGSET_USEE_USAGE_M4=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM TRAININGSET_USEE_USAGE WHERE PERIODE = 'M4';",conn)
TRAININGSET_USEE_USAGE_M5=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM TRAININGSET_USEE_USAGE WHERE PERIODE = 'M5';",conn)
TRAININGSET_USEE_USAGE_M6=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM TRAININGSET_USEE_USAGE WHERE PERIODE = 'M6';",conn)

TRAININGSET_INET_USAGE_M1=pd.read_sql_query("SELECT * FROM TRAININGSET_INET_USAGE WHERE PERIODE = 'M1';",conn)
TRAININGSET_INET_USAGE_M2=pd.read_sql_query("SELECT * FROM TRAININGSET_INET_USAGE WHERE PERIODE = 'M2';",conn)
TRAININGSET_INET_USAGE_M3=pd.read_sql_query("SELECT * FROM TRAININGSET_INET_USAGE WHERE PERIODE = 'M3';",conn)
TRAININGSET_INET_USAGE_M4=pd.read_sql_query("SELECT * FROM TRAININGSET_INET_USAGE WHERE PERIODE = 'M4';",conn)
TRAININGSET_INET_USAGE_M5=pd.read_sql_query("SELECT * FROM TRAININGSET_INET_USAGE WHERE PERIODE = 'M5';",conn)
TRAININGSET_INET_USAGE_M6=pd.read_sql_query("SELECT * FROM TRAININGSET_INET_USAGE WHERE PERIODE = 'M6';",conn)


# In[6]:



TRAININGSET_POTS_PAY_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_POTS_PAY WHERE PERIODE = 'M1';",conn)
TRAININGSET_POTS_PAY_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_POTS_PAY WHERE PERIODE = 'M2';",conn)
TRAININGSET_POTS_PAY_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_POTS_PAY WHERE PERIODE = 'M3';",conn)
TRAININGSET_POTS_PAY_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_POTS_PAY WHERE PERIODE = 'M4';",conn)
TRAININGSET_POTS_PAY_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_POTS_PAY WHERE PERIODE = 'M5';",conn)
TRAININGSET_POTS_PAY_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_POTS_PAY WHERE PERIODE = 'M6';",conn)


TRAININGSET_INET_PAY_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_INET_PAY WHERE PERIODE = 'M1';",conn)
TRAININGSET_INET_PAY_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_INET_PAY WHERE PERIODE = 'M2';",conn)
TRAININGSET_INET_PAY_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_INET_PAY WHERE PERIODE = 'M3';",conn)
TRAININGSET_INET_PAY_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_INET_PAY WHERE PERIODE = 'M4';",conn)
TRAININGSET_INET_PAY_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_INET_PAY WHERE PERIODE = 'M5';",conn)
TRAININGSET_INET_PAY_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM TRAININGSET_INET_PAY WHERE PERIODE = 'M6';",conn)

TRAININGSET_INET_TICKET_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_INET_TICKET WHERE PERIODE = 'M1';",conn)
TRAININGSET_INET_TICKET_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_INET_TICKET WHERE PERIODE = 'M2';",conn)
TRAININGSET_INET_TICKET_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_INET_TICKET WHERE PERIODE = 'M3';",conn)
TRAININGSET_INET_TICKET_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_INET_TICKET WHERE PERIODE = 'M4';",conn)
TRAININGSET_INET_TICKET_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_INET_TICKET WHERE PERIODE = 'M5';",conn)
TRAININGSET_INET_TICKET_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_INET_TICKET WHERE PERIODE = 'M6';",conn)

TRAININGSET_POTS_TICKET_M1=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_POTS_TICKET WHERE PERIODE = 'M1';",conn)
TRAININGSET_POTS_TICKET_M2=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_POTS_TICKET WHERE PERIODE = 'M2';",conn)
TRAININGSET_POTS_TICKET_M3=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_POTS_TICKET WHERE PERIODE = 'M3';",conn)
TRAININGSET_POTS_TICKET_M4=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_POTS_TICKET WHERE PERIODE = 'M4';",conn)
TRAININGSET_POTS_TICKET_M5=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_POTS_TICKET WHERE PERIODE = 'M5';",conn)
TRAININGSET_POTS_TICKET_M6=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM TRAININGSET_POTS_TICKET WHERE PERIODE = 'M6';",conn)


# In[7]:


TRAININGSET_POTS_REV_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_POTS_REV WHERE PERIODE = 'M1';",conn)
TRAININGSET_POTS_REV_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_POTS_REV WHERE PERIODE = 'M2';",conn)
TRAININGSET_POTS_REV_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_POTS_REV WHERE PERIODE = 'M3';",conn)
TRAININGSET_POTS_REV_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_POTS_REV WHERE PERIODE = 'M4';",conn)
TRAININGSET_POTS_REV_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_POTS_REV WHERE PERIODE = 'M5';",conn)
TRAININGSET_POTS_REV_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_POTS_REV WHERE PERIODE = 'M6';",conn)


TRAININGSET_INET_REV_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_INET_REV WHERE PERIODE = 'M1';",conn)
TRAININGSET_INET_REV_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_INET_REV WHERE PERIODE = 'M2';",conn)
TRAININGSET_INET_REV_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_INET_REV WHERE PERIODE = 'M3';",conn)
TRAININGSET_INET_REV_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_INET_REV WHERE PERIODE = 'M4';",conn)
TRAININGSET_INET_REV_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_INET_REV WHERE PERIODE = 'M5';",conn)
TRAININGSET_INET_REV_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM TRAININGSET_INET_REV WHERE PERIODE = 'M6';",conn)


TRAININGSET_POTS_USAGE_M1=pd.read_sql_query("SELECT * FROM TRAININGSET_POTS_USAGE WHERE PERIODE = 'M1';",conn)
TRAININGSET_POTS_USAGE_M2=pd.read_sql_query("SELECT * FROM TRAININGSET_POTS_USAGE WHERE PERIODE = 'M2';",conn)
TRAININGSET_POTS_USAGE_M3=pd.read_sql_query("SELECT * FROM TRAININGSET_POTS_USAGE WHERE PERIODE = 'M3';",conn)
TRAININGSET_POTS_USAGE_M4=pd.read_sql_query("SELECT * FROM TRAININGSET_POTS_USAGE WHERE PERIODE = 'M4';",conn)
TRAININGSET_POTS_USAGE_M5=pd.read_sql_query("SELECT * FROM TRAININGSET_POTS_USAGE WHERE PERIODE = 'M5';",conn)
TRAININGSET_POTS_USAGE_M6=pd.read_sql_query("SELECT * FROM TRAININGSET_POTS_USAGE WHERE PERIODE = 'M6';",conn)


# ### rename column per month

# In[8]:


TRAININGSET_USEE_USAGE_M1 = TRAININGSET_USEE_USAGE_M1.rename({ 'GENRE_PROGRAM': 'Genre_program_M1','FREQ': 'Freq_M1', 'DUREE': 'Duree_M1'}, axis=1)
TRAININGSET_USEE_USAGE_M2 = TRAININGSET_USEE_USAGE_M2.rename({ 'GENRE_PROGRAM': 'Genre_program_M2','FREQ': 'Freq_M2', 'DUREE': 'Duree_M2'}, axis=1)
TRAININGSET_USEE_USAGE_M3 = TRAININGSET_USEE_USAGE_M3.rename({'GENRE_PROGRAM': 'Genre_program_M3','FREQ': 'Freq_M3', 'DUREE': 'Duree_M3'}, axis=1)
TRAININGSET_USEE_USAGE_M4 = TRAININGSET_USEE_USAGE_M4.rename({ 'GENRE_PROGRAM': 'Genre_program_M4','FREQ': 'Freq_M4', 'DUREE': 'Duree_M4'}, axis=1)
TRAININGSET_USEE_USAGE_M5 = TRAININGSET_USEE_USAGE_M5.rename({ 'GENRE_PROGRAM': 'Genre_program_M5','FREQ': 'Freq_M5', 'DUREE': 'Duree_M5'}, axis=1)
TRAININGSET_USEE_USAGE_M6 = TRAININGSET_USEE_USAGE_M6.rename({'GENRE_PROGRAM': 'Genre_program_M6','FREQ': 'Freq_M6', 'DUREE': 'Duree_M6'}, axis=1)


TRAININGSET_INET_USAGE_M1 = TRAININGSET_INET_USAGE_M1.rename({'TOTAL_FREQ': 'Total_Freq_M1', 'TOTAL_DURASI': 'Total_Durasi_M1','TOTAL_USAGE': 'Total_usage_M1', 'TOTAL_UPLOAD': 'Total_upload_M1', 'TOTAL_DOWNLOAD': 'Total_download_M1'}, axis=1)
TRAININGSET_INET_USAGE_M2 = TRAININGSET_INET_USAGE_M2.rename({'TOTAL_FREQ': 'Total_Freq_M2', 'TOTAL_DURASI': 'Total_Durasi_M2','TOTAL_USAGE': 'Total_usage_M2', 'TOTAL_UPLOAD': 'Total_upload_M2', 'TOTAL_DOWNLOAD': 'Total_download_M2'}, axis=1)
TRAININGSET_INET_USAGE_M3 = TRAININGSET_INET_USAGE_M3.rename({'TOTAL_FREQ': 'Total_Freq_M3', 'TOTAL_DURASI': 'Total_Durasi_M3','TOTAL_USAGE': 'Total_usage_M3', 'TOTAL_UPLOAD': 'Total_upload_M3', 'TOTAL_DOWNLOAD': 'Total_download_M3'}, axis=1)
TRAININGSET_INET_USAGE_M4 = TRAININGSET_INET_USAGE_M4.rename({'TOTAL_FREQ': 'Total_Freq_M4', 'TOTAL_DURASI': 'Total_Durasi_M4','TOTAL_USAGE': 'Total_usage_M4', 'TOTAL_UPLOAD': 'Total_upload_M4', 'TOTAL_DOWNLOAD': 'Total_download_M4'}, axis=1)
TRAININGSET_INET_USAGE_M5 = TRAININGSET_INET_USAGE_M5.rename({'TOTAL_FREQ': 'Total_Freq_M5', 'TOTAL_DURASI': 'Total_Durasi_M5','TOTAL_USAGE': 'Total_usage_M5', 'TOTAL_UPLOAD': 'Total_upload_M5', 'TOTAL_DOWNLOAD': 'Total_download_M5'}, axis=1)
TRAININGSET_INET_USAGE_M6 = TRAININGSET_INET_USAGE_M6.rename({'TOTAL_FREQ': 'Total_Freq_M6', 'TOTAL_DURASI': 'Total_Durasi_M6','TOTAL_USAGE': 'Total_usage_M6', 'TOTAL_UPLOAD': 'Total_upload_M6', 'TOTAL_DOWNLOAD': 'Total_download_M6'}, axis=1)


TRAININGSET_POTS_PAY_M1 = TRAININGSET_POTS_PAY_M1.rename({'Payment': 'Payment_pots_M1', 'Pay_status': 'Pay_status_pots_M1'}, axis=1)
TRAININGSET_POTS_PAY_M2 = TRAININGSET_POTS_PAY_M2.rename({'Payment': 'Payment_pots_M2', 'Pay_status': 'Pay_status_pots_M2'}, axis=1)
TRAININGSET_POTS_PAY_M3 = TRAININGSET_POTS_PAY_M3.rename({'Payment': 'Payment_pots_M3', 'Pay_status': 'Pay_status_pots_M3'}, axis=1)
TRAININGSET_POTS_PAY_M4 = TRAININGSET_POTS_PAY_M4.rename({'Payment': 'Payment_pots_M4', 'Pay_status': 'Pay_status_pots_M4'}, axis=1)
TRAININGSET_POTS_PAY_M5 = TRAININGSET_POTS_PAY_M5.rename({'Payment': 'Payment_pots_M5', 'Pay_status': 'Pay_status_pots_M5'}, axis=1)
TRAININGSET_POTS_PAY_M6 = TRAININGSET_POTS_PAY_M6.rename({'Payment': 'Payment_pots_M6', 'Pay_status': 'Pay_status_pots_M6'}, axis=1)

TRAININGSET_INET_PAY_M1 = TRAININGSET_INET_PAY_M1.rename({'Payment': 'Payment_inet_M1', 'Pay_status': 'Pay_status_inet_M1'}, axis=1)
TRAININGSET_INET_PAY_M2 = TRAININGSET_INET_PAY_M2.rename({'Payment': 'Payment_inet_M2', 'Pay_status': 'Pay_status_inet_M2'}, axis=1)
TRAININGSET_INET_PAY_M3 = TRAININGSET_INET_PAY_M3.rename({'Payment': 'Payment_inet_M3', 'Pay_status': 'Pay_status_inet_M3'}, axis=1)
TRAININGSET_INET_PAY_M4 = TRAININGSET_INET_PAY_M4.rename({'Payment': 'Payment_inet_M4', 'Pay_status': 'Pay_status_inet_M4'}, axis=1)
TRAININGSET_INET_PAY_M5 = TRAININGSET_INET_PAY_M5.rename({'Payment': 'Payment_inet_M5', 'Pay_status': 'Pay_status_inet_M5'}, axis=1)
TRAININGSET_INET_PAY_M6 = TRAININGSET_INET_PAY_M6.rename({'Payment': 'Payment_inet_M6', 'Pay_status': 'Pay_status_inet_M6'}, axis=1)



TRAININGSET_INET_TICKET_M1 = TRAININGSET_INET_TICKET_M1.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M1', 'N_ticket': 'N_ticket_inet_M1', 'Mttr': 'Mttr_inet_M1'}, axis=1)
TRAININGSET_INET_TICKET_M2 = TRAININGSET_INET_TICKET_M2.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M2', 'N_ticket': 'N_ticket_inet_M2', 'Mttr': 'Mttr_inet_M2'}, axis=1)
TRAININGSET_INET_TICKET_M3 = TRAININGSET_INET_TICKET_M3.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M3', 'N_ticket': 'N_ticket_inet_M3', 'Mttr': 'Mttr_inet_M3'}, axis=1)
TRAININGSET_INET_TICKET_M4 = TRAININGSET_INET_TICKET_M4.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M4', 'N_ticket': 'N_ticket_inet_M4', 'Mttr': 'Mttr_inet_M4'}, axis=1)
TRAININGSET_INET_TICKET_M5 = TRAININGSET_INET_TICKET_M5.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M5', 'N_ticket': 'N_ticket_inet_M5', 'Mttr': 'Mttr_inet_M5'}, axis=1)
TRAININGSET_INET_TICKET_M6 = TRAININGSET_INET_TICKET_M6.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M6', 'N_ticket': 'N_ticket_inet_M6', 'Mttr': 'Mttr_inet_M6'}, axis=1)


TRAININGSET_POTS_TICKET_M1 = TRAININGSET_POTS_TICKET_M1.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M1', 'N_ticket': 'N_ticket_pots_M1', 'Mttr': 'Mttr_pots_M1'}, axis=1)
TRAININGSET_POTS_TICKET_M2 = TRAININGSET_POTS_TICKET_M2.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M2', 'N_ticket': 'N_ticket_pots_M2', 'Mttr': 'Mttr_pots_M2'}, axis=1)
TRAININGSET_POTS_TICKET_M3 = TRAININGSET_POTS_TICKET_M3.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M3', 'N_ticket': 'N_ticket_pots_M3', 'Mttr': 'Mttr_pots_M3'}, axis=1)
TRAININGSET_POTS_TICKET_M4 = TRAININGSET_POTS_TICKET_M4.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M4', 'N_ticket': 'N_ticket_pots_M4', 'Mttr': 'Mttr_pots_M4'}, axis=1)
TRAININGSET_POTS_TICKET_M5 = TRAININGSET_POTS_TICKET_M5.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M5', 'N_ticket': 'N_ticket_pots_M5', 'Mttr': 'Mttr_pots_M5'}, axis=1)
TRAININGSET_POTS_TICKET_M6 = TRAININGSET_POTS_TICKET_M6.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M6', 'N_ticket': 'N_ticket_pots_M6', 'Mttr': 'Mttr_pots_M6'}, axis=1)


# In[9]:


TRAININGSET_POTS_REV_M1 = TRAININGSET_POTS_REV_M1.rename({'Revenue_billing': 'Revenue_billing_pots_M1'}, axis=1)
TRAININGSET_POTS_REV_M2 = TRAININGSET_POTS_REV_M2.rename({'Revenue_billing': 'Revenue_billing_pots_M2'}, axis=1)
TRAININGSET_POTS_REV_M3 = TRAININGSET_POTS_REV_M3.rename({'Revenue_billing': 'Revenue_billing_pots_M3'}, axis=1)
TRAININGSET_POTS_REV_M4 = TRAININGSET_POTS_REV_M4.rename({'Revenue_billing': 'Revenue_billing_pots_M4'}, axis=1)
TRAININGSET_POTS_REV_M5 = TRAININGSET_POTS_REV_M5.rename({'Revenue_billing': 'Revenue_billing_pots_M5'}, axis=1)
TRAININGSET_POTS_REV_M6 = TRAININGSET_POTS_REV_M6.rename({'Revenue_billing': 'Revenue_billing_pots_M6'}, axis=1)

TRAININGSET_INET_REV_M1 = TRAININGSET_INET_REV_M1.rename({'Revenue_billing': 'Revenue_billing_inet_M1'}, axis=1)
TRAININGSET_INET_REV_M2 = TRAININGSET_INET_REV_M2.rename({'Revenue_billing': 'Revenue_billing_inet_M2'}, axis=1)
TRAININGSET_INET_REV_M3 = TRAININGSET_INET_REV_M3.rename({'Revenue_billing': 'Revenue_billing_inet_M3'}, axis=1)
TRAININGSET_INET_REV_M4 = TRAININGSET_INET_REV_M4.rename({'Revenue_billing': 'Revenue_billing_inet_M4'}, axis=1)
TRAININGSET_INET_REV_M5 = TRAININGSET_INET_REV_M5.rename({'Revenue_billing': 'Revenue_billing_inet_M5'}, axis=1)
TRAININGSET_INET_REV_M6 = TRAININGSET_INET_REV_M6.rename({'Revenue_billing': 'Revenue_billing_inet_M6'}, axis=1)


# ### join table 

# In[10]:


TRAININGSET_JOIN = pd.merge(TRAININGSET_TARGET,TRAININGSET_INET_USAGE_M1,how='left',on='ID_CUSTOMER',validate='many_to_many')


# In[12]:


#Join Target and Usee Usage
TRAININGSET_JOIN = TRAININGSET_TARGET.merge(TRAININGSET_USEE_USAGE_M1,on='ID_CUSTOMER',how='left').merge(TRAININGSET_USEE_USAGE_M2,on='ID_CUSTOMER',how='left').merge(TRAININGSET_USEE_USAGE_M3,on='ID_CUSTOMER',how='left').merge(TRAININGSET_USEE_USAGE_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_USEE_USAGE_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_USEE_USAGE_M5,on='ID_CUSTOMER',how='left').merge(TRAININGSET_USEE_USAGE_M6,on='ID_CUSTOMER',how='left')


# In[14]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join inet pay
TRAININGSET_JOIN = TRAININGSET_JOIN.merge(TRAININGSET_INET_PAY_M1,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_PAY_M2,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_PAY_M3,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_PAY_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_PAY_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_PAY_M5,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_PAY_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join inet usage
TRAININGSET_JOIN=TRAININGSET_JOIN.merge(TRAININGSET_INET_USAGE_M1,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_USAGE_M2,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_USAGE_M3,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_USAGE_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_USAGE_M5,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_USAGE_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join pots pay
TRAININGSET_JOIN = TRAININGSET_JOIN.merge(TRAININGSET_POTS_PAY_M1,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_PAY_M2,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_PAY_M3,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_PAY_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_PAY_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_PAY_M5,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_PAY_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#JOIN pots ticket
TRAININGSET_JOIN = TRAININGSET_JOIN.merge(TRAININGSET_POTS_TICKET_M1,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_TICKET_M2,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_TICKET_M3,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_TICKET_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_TICKET_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_TICKET_M5,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_TICKET_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join inet ticket
TRAININGSET_JOIN = TRAININGSET_JOIN.merge(TRAININGSET_INET_TICKET_M1,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_TICKET_M2,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_TICKET_M3,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_TICKET_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_TICKET_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_TICKET_M5,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_TICKET_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join inet rev
TRAININGSET_JOIN = TRAININGSET_JOIN.merge(TRAININGSET_INET_REV_M1,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_REV_M2,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_REV_M3,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_REV_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_REV_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_REV_M5,on='ID_CUSTOMER',how='left').merge(TRAININGSET_INET_REV_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join pots rev
TRAININGSET_JOIN = TRAININGSET_JOIN.merge(TRAININGSET_POTS_REV_M1,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_REV_M2,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_REV_M3,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_REV_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_REV_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_REV_M5,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_REV_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join pots usage
TRAININGSET_JOIN = TRAININGSET_JOIN.merge(TRAININGSET_POTS_USAGE_M1,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_USAGE_M2,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_USAGE_M3,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_USAGE_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_USAGE_M4,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_USAGE_M5,on='ID_CUSTOMER',how='left').merge(TRAININGSET_POTS_USAGE_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join pop and speed
TRAININGSET_JOIN = TRAININGSET_JOIN.merge(TRAININGSET_POP,on='ID_CUSTOMER',how='left').merge(TRAININGSET_SPEED,on='ID_CUSTOMER',how='left')


# In[ ]:


TRAININGSET_JOIN = TRAININGSET_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[15]:


TRAININGSET_JOIN.shape


# In[16]:


TRAININGSET = TRAININGSET_JOIN


# In[122]:


TRAININGSET.to_csv('TRAININGSET_ALLMONTH.csv', index = False)


# In[187]:


# baca data CSV, jadikan variable df_load
TRAININGSET = pd.read_csv("TRAININGSET_ALLMONTH.csv",delimiter=';') 


# In[189]:


# lihat banyaknya observasi
TRAININGSET.shape


# ## 2. Data Preprocessing

# ### Drop Duplicate

# In[190]:


TRAININGSET = TRAININGSET.drop_duplicates()


# In[191]:


# lihat banyaknya observasi
TRAININGSET.shape


# ### Data Dtypes

# In[192]:


TRAININGSET.dtypes


# ### Missing Values

# In[193]:


# Check Total Missing Value
TRAININGSET.isnull().mean().sort_values(ascending=False)


# In[194]:


TRAININGSET.drop(['Tipe_gangguan_pots_M1','Tipe_gangguan_pots_M2','Tipe_gangguan_pots_M3','Tipe_gangguan_pots_M4','Tipe_gangguan_pots_M5','Tipe_gangguan_pots_M6','Tipe_gangguan_inet_M1','Tipe_gangguan_inet_M2','Tipe_gangguan_inet_M3','Tipe_gangguan_inet_M4','Tipe_gangguan_inet_M5','Tipe_gangguan_inet_M6','Genre_program_inet_M1','Genre_program_inet_M2','Genre_program_inet_M3','Genre_program_inet_M4','Genre_program_inet_M5','Genre_program_inet_M6','Call_lokal_M1','Call_lokal_M2','Call_lokal_M3','Call_lokal_M4','Call_lokal_M5','Call_lokal_M6','Call_sljj_M1','Call_sljj_M2','Call_sljj_M3','Call_sljj_M4','Call_sljj_M5','Call_sljj_M6','Call_mobile_M1','Call_mobile_M2','Call_mobile_M3','Call_mobile_M4','Call_mobile_M5','Call_mobile_M6','Call_sli_M1','Call_sli_M2','Call_sli_M3','Call_sli_M4','Call_sli_M5','Call_sli_M6','Call_other_M1','Call_other_M2','Call_other_M3','Call_other_M4','Call_other_M5','Call_other_M6','Duree_lokal_M1','Duree_lokal_M2','Duree_lokal_M3','Duree_lokal_M4','Duree_lokal_M5','Duree_lokal_M6','Duree_sljj_M1','Duree_sljj_M2','Duree_sljj_M3','Duree_sljj_M4','Duree_sljj_M5','Duree_sljj_M6','Duree_mobile_M1','Duree_mobile_M2','Duree_mobile_M3','Duree_mobile_M4','Duree_mobile_M5','Duree_mobile_M6','Duree_sli_M1','Duree_sli_M2','Duree_sli_M3','Duree_sli_M4','Duree_sli_M5','Duree_sli_M6','Duree_other_M1','Duree_other_M2','Duree_other_M3','Duree_other_M4','Duree_other_M5','Duree_other_M6','Revenue_billing_pots_M1','Revenue_billing_pots_M2','Revenue_billing_pots_M3','Revenue_billing_pots_M4','Revenue_billing_pots_M5','Revenue_billing_pots_M6','N_ticket_pots_M1','N_ticket_pots_M2','N_ticket_pots_M3','N_ticket_pots_M4','N_ticket_pots_M5','N_ticket_pots_M6','Mttr_pots_M1','Mttr_pots_M2','Mttr_pots_M3','Mttr_pots_M4','Mttr_pots_M5','Mttr_pots_M6','N_ticket_inet_M1','N_ticket_inet_M2','N_ticket_inet_M3','N_ticket_inet_M4','N_ticket_inet_M5','N_ticket_inet_M6','Mttr_inet_M1','Mttr_inet_M2','Mttr_inet_M3','Mttr_inet_M4','Mttr_inet_M5','Mttr_inet_M6','Freq_M1','Freq_M2','Freq_M3','Freq_M4','Freq_M5','Freq_M6','Duree_M1','Duree_M2','Duree_M3','Duree_M4','Duree_M5','Duree_M6','Total_Minipack'], axis=1, inplace = True)


# In[195]:


# Check Total Missing Value
TRAININGSET.isnull().mean().sort_values(ascending=False)


# ### Target Proportion

# In[196]:


print(TRAININGSET['Y'].value_counts())
print(TRAININGSET['Y'].value_counts(normalize=True))

(TRAININGSET['Y'].value_counts(normalize = True)*100).plot(kind = 'bar', title = 'Late Payment rate')
plt.xlabel('Late Payment')
plt.ylabel('Percentage %')


# ### Remove ID

# In[197]:


id_col = ['Id_customer']


# In[198]:


TRAININGSET.drop(id_col, axis=1, inplace = True)


# In[199]:


TRAININGSET.head(5)


# In[200]:


TRAININGSET.shape


# ### Separating X and Y variables

# In[201]:


target = ['Y']


# In[202]:


X = TRAININGSET.loc[:, TRAININGSET.columns != target[0]]
y = TRAININGSET[target[0]]

print(X.shape, y.shape)


# ### Tes and Train Split

# In[203]:


from sklearn.model_selection import train_test_split


# In[204]:


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=123)


# In[205]:


x_train.head()


# In[206]:


# Calculate target proportion
print("Proportion of training data:")
print(y_train.value_counts())
print(y_train.value_counts(normalize=True))
print("\nProportion of testing data:")
print(y_test.value_counts())
print(y_test.value_counts(normalize=True))


# ### Select Numerical and Categorical Variables

# In[207]:


# Define Categorical Columns
cat_col = ['Pay_status_inet_M1','Pay_status_inet_M2','Pay_status_inet_M3','Pay_status_inet_M4','Pay_status_inet_M5','Pay_status_inet_M6','Pay_status_pots_M1','Pay_status_pots_M2','Pay_status_pots_M3','Pay_status_pots_M4','Pay_status_pots_M5','Pay_status_pots_M6','Tipe_gangguan_pots_M1','Tipe_gangguan_pots_M2','Tipe_gangguan_pots_M3','Tipe_gangguan_pots_M4','Tipe_gangguan_pots_M5','Tipe_gangguan_pots_M6','Tipe_gangguan_inet_M1','Tipe_gangguan_inet_M2','Tipe_gangguan_inet_M3','Tipe_gangguan_inet_M4','Tipe_gangguan_inet_M5','Tipe_gangguan_inet_M6','Genre_program_inet_M1','Genre_program_inet_M2','Genre_program_inet_M3','Genre_program_inet_M4','Genre_program_inet_M5','Genre_program_inet_M6','Speed','Divre_id','Technology','Kw','Indihome_type']


# In[208]:


# Get Numerical Columns using Set
num_col = list(set(x_train.columns) - set(cat_col))
num_col


# In[209]:


# train data
x_train_numerical   = x_train.filter(num_col, axis=1)
x_train_categorical = x_train.filter(cat_col, axis=1)

# test data
x_test_numerical    = x_test.filter(num_col, axis=1)
x_test_categorical  = x_test.filter(cat_col, axis=1)


# In[210]:


x_train_numerical.head(5)


# In[211]:


x_train_categorical.head(5)


# ### Outlier for Handling Numerical Data

# In[212]:


x_train_numerical.describe()


# In[213]:


# Capping X_train values: AVG(X) +- 3*STDDEV(X)
mean_X               = x_train_numerical.mean()
std_X                = x_train_numerical.std()
up_bound             = mean_X + (3*std_X)
low_bound            = mean_X - (3*std_X)
more_than_up_bound   = (x_train_numerical > up_bound)
lower_than_low_bound = (x_train_numerical < low_bound)
df_cap               = x_train_numerical.mask(more_than_up_bound, up_bound, axis=1) 
df_cap               = df_cap.mask(lower_than_low_bound, low_bound, axis=1)
x_train_numerical    = df_cap

# Capping X_test values: AVG(X) +- 3*STDDEV(X)
more_than_up_bound   = (x_test_numerical > up_bound)
lower_than_low_bound = (x_test_numerical < low_bound)
df_cap               = x_test_numerical.mask(more_than_up_bound, up_bound, axis=1) 
df_cap               = df_cap.mask(lower_than_low_bound, low_bound, axis=1)
x_test_numerical     = df_cap

# Check data shape
print(x_train_numerical.shape, x_test_numerical.shape)


# In[214]:


x_train_numerical.describe()


# ### Numerical Imputation

# In[215]:


# from sklearn.preprocessing import Imputer # Old Version
# New in version 0.20: sklearn.impute.SimpleImputer replaces the previous 
#                      sklearn.preprocessing.Imputer estimator which is now removed.

# imput_numerical = Imputer(missing_values = 'NaN', strategy = 'median') # Old Version

from sklearn.impute import SimpleImputer

imput_numerical = SimpleImputer(missing_values = np.nan, strategy = 'median', fill_value=None)

# Impute Training Data
def numericalImputation(numerical_data):
    '''Imputasi data numerical
    data: <pandas dataframe> sample data input 
    numerical: <list> list nama column numerical    
    '''
    
    train_numerical_data = numerical_data
    imput_numerical.fit(train_numerical_data)
    
    numerical_data_imputed = pd.DataFrame(imput_numerical.transform(train_numerical_data))
    numerical_data_imputed.columns = numerical_data.columns
    numerical_data_imputed.index = train_numerical_data.index

    return  numerical_data_imputed, imput_numerical

# Impute Testing Data
def imput_numeric(numerical_data, imput_numerical):
    numerical_data_columns = list(numerical_data)
    numerical_data_imput   = pd.DataFrame(imput_numerical.transform(numerical_data), index = numerical_data.index) # imput numerical test
    numerical_data_imput.columns = numerical_data_columns
        
    return numerical_data_imput


# In[216]:


x_train_numerical_imputed, imput_numerical = numericalImputation(x_train_numerical)
x_test_numerical_imputed = imput_numeric(x_test_numerical, imput_numerical)


# In[217]:


# Cek apakah ada data numerical yang kosong
x_train_numerical_imputed.isnull().any()


# In[218]:


x_train_numerical_imputed.head()


# ### Categorical Imputation

# In[219]:


# Isi NaN dari categorical data dengan value baru == "KOSONG"
x_train_categorical_imputed = x_train_categorical.fillna(value="KOSONG")
x_test_categorical_imputed  = x_test_categorical.fillna(value="KOSONG")


# In[220]:


# Cek apakah ada data numerical yang kosong
x_train_categorical_imputed.isnull().any()


# In[221]:


x_train_categorical_imputed.head()


# ### Categorical Dummy Variables

# In[222]:


# Buat data categorical menjadi dummies 1 dan 0
x_train_categorical_dummy = pd.get_dummies(x_train_categorical_imputed.astype(str), drop_first=True)
x_test_categorical_dummy  = pd.get_dummies(x_test_categorical_imputed.astype(str), drop_first=True)


# In[223]:


x_train_categorical_dummy.head()


# ### Join Categorical and Numerical Data

# In[224]:


x_train = pd.concat([x_train_numerical_imputed, x_train_categorical_dummy], axis =1)
x_test  = pd.concat([x_test_numerical_imputed, x_test_categorical_dummy], axis =1)


# In[225]:


x_train.isnull().any()


# ## 3. Exploratory Data Analysis and Feature Selection

# ### Check Statistical Summary

# In[226]:


x_train.describe()


# ### Check Distribution

# In[227]:


import seaborn as sns


# In[228]:


eda_data = pd.concat([x_train, y_train], axis = 1)


# In[229]:


eda_data.dtypes


# In[230]:


ax = sns.boxplot(x="Y", y="Total_durasi_M6", data=eda_data)


# In[231]:


ax = sns.boxplot(x="Y", y="Payment_inet_M6", data=eda_data)


# In[233]:


ax = sns.boxplot(x="Y", y="Revenue_billing_inet_M1", data=eda_data)


# In[235]:


ax = sns.boxplot(x="Y", y="Total_upload_M1", data=eda_data)


# In[236]:


ax = sns.boxplot(x="Y", y="Total_freq_M1", data=eda_data)


# In[239]:


ax = sns.boxplot(x="Y", y="Total_usage_M6", data=eda_data)


# In[240]:


ax = sns.boxplot(x="Y", y="Length_of_stay", data=eda_data)


# In[242]:


ax = sns.boxplot(x="Y", y="Total_download_M6", data=eda_data)


# In[243]:


ax = sns.boxplot(x="Y", y="Payment_pots_M6", data=eda_data)


# ### Check Relation between Independent Variables and Dependent Variables

# In[244]:


def plot_bins(df, y, col, bins=None, lowest=True, rotation=0):
    
    df_tmp = df[[col, y]]
    if bins is None:
        bins_ = df_tmp[col]
    else:
        bins_ = pd.cut(df_tmp[col], bins=bins, include_lowest=lowest)
        
    df_tmp = df_tmp.assign(bins = bins_)
    
    f = {y:['count','sum']}
    agg = df_tmp.groupby('bins').agg(f)
    agg.columns = ['ncust', 'nlate_pay']
    agg['rate'] = 1.0 * agg['nlate_pay'] / agg['ncust']
    
    x = agg.index.astype(str)
    y1 = agg['ncust']
    y2 = agg['rate']
    
    y1 = y1.reset_index()
    y2 = y2.reset_index()

    fig, ax1 = plt.subplots()
    plt.xticks(rotation=rotation)
    
    ax2 = ax1.twinx()
    ax1.bar(y1.index.tolist(), y1.ncust, color='b')
    ax2.plot(y2.index.tolist(), y2.rate, 'r-')

    ax1.set_xlabel(col)
    ax1.set_ylabel('Total customers', color='b')
    ax2.set_ylabel('Late Payment rate', color='r')
    
    plt.grid(False)
    plt.show()
    
    return(agg)


# In[245]:


eda_data.dtypes


# In[246]:


eda_data.head()


# In[247]:


plot_bins(eda_data, 'Y', 'Total_durasi_M6', bins=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 13.0], rotation=90)


# In[248]:


plot_bins(eda_data, 'Y', 'Payment_inet_M6', bins=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 13.0], rotation=90)


# In[96]:


plot_bins(eda_data, 'Y', 'Total_upload', bins=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 13.0], rotation=90)


# In[251]:


plot_bins(eda_data, 'Y', 'Length_of_stay', bins=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 13.0], rotation=90)


# In[252]:


plot_bins(eda_data, 'Y', 'Total_freq_M1', bins=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 13.0], rotation=90)


# In[100]:


plot_bins(eda_data, 'Y', 'Total_usage', bins=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 13.0], rotation=90)


# In[254]:


plot_bins(eda_data, 'Y', 'Total_download_M6', bins=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 13.0], rotation=90)


# In[255]:


plot_bins(eda_data, 'Y', 'Payment_pots_M6', bins=[0.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 13.0], rotation=90)


# ### Check Correlation

# In[256]:


# Heatmap Correlation
plt.figure(figsize=(20,20))
sns.heatmap(x_train.corr(), annot = True)


# ### Select K Best

# In[257]:


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# https://www.programcreek.com/python/example/85917/sklearn.feature_selection.f_classif
def select_kbest(X, y, k=20):

    feat_selector = SelectKBest(f_classif, k=k)
    _ = feat_selector.fit(X, y)
    
    support = feat_selector.get_support()
    
    feat_scores = pd.DataFrame()
    feat_scores["attribute"] = X.columns
    feat_scores["f_score"] = feat_selector.scores_
    feat_scores["p_value"] = feat_selector.pvalues_
    feat_scores["support"] = support
    
    x_new = X[X.columns[support.tolist()]]
    
    return x_new, feat_scores


# In[258]:


X_best, feat_scores = select_kbest(x_train, y_train, k=102)


# In[259]:


feat_scores.sort_values('p_value', ascending=True)


# In[260]:


# If we use confidence level 0.95 or alpha=0.05
feat_scores[feat_scores.p_value <= 0.05].sort_values('p_value', ascending=True)


# In[261]:


selected_columns = list(feat_scores[feat_scores.p_value <= 0.05]['attribute'])
selected_columns


# In[262]:


# Heatmap Correlation
plt.figure(figsize=(20,20))
sns.heatmap(X_best[selected_columns].corr(), annot = True)


# In[263]:


# Exclude: VMail_Message, Intl_Mins, Eve_Mins, Day_Mins
selected_columns = ['Total_durasi_M6',
 'Payment_inet_M4',
 'Revenue_billing_inet_M1',
 'Revenue_billing_inet_M6',
 'Revenue_billing_inet_M2',
 'Length_of_stay',
 'Total_durasi_M2',
 'Total_freq_M5',
 'Revenue_billing_inet_M3',
 'Total_durasi_M4',
 'Total_freq_M2',
 'Total_durasi_M5',
 'Payment_pots_M1',
 'Payment_pots_M3',
 'Total_freq_M3',
 'Payment_inet_M3',
 'Total_upload_M5',
 'Total_freq_M6',
 'Total_freq_M4',
 'Payment_pots_M4',
 'Total_upload_M4',
 'Payment_pots_M2',
 'Total_freq_M1',
 'Revenue_billing_inet_M5',
 'Payment_pots_M6',
 'Total_upload_M2',
 'Payment_inet_M1',
 'Payment_inet_M2',
 'Payment_inet_M6',
 'Total_upload_M1',
 'Total_upload_M3',
 'Payment_pots_M5',
 'Revenue_billing_inet_M4',
 'Total_durasi_M3',
 'Pay_status_inet_M1_LATE_SAME_MONTH',
 'Pay_status_inet_M1_NOT_LATE',
 'Pay_status_inet_M2_LATE_SAME_MONTH',
 'Pay_status_inet_M2_NOT_LATE',
 'Pay_status_inet_M3_LATE_SAME_MONTH',
 'Pay_status_inet_M3_NOT_LATE',
 'Pay_status_inet_M4_LATE_SAME_MONTH',
 'Pay_status_inet_M4_NOT_LATE',
 'Pay_status_inet_M5_LATE_NEXT_MONTH',
 'Pay_status_inet_M5_LATE_SAME_MONTH',
 'Pay_status_inet_M5_NOT_LATE',
 'Pay_status_inet_M6_LATE_NEXT_MONTH',
 'Pay_status_inet_M6_LATE_SAME_MONTH',
 'Pay_status_inet_M6_NOT_LATE',
 'Pay_status_pots_M1_LATE_SAME_MONTH',
 'Pay_status_pots_M1_NOT_LATE',
 'Pay_status_pots_M2_LATE_SAME_MONTH',
 'Pay_status_pots_M2_NOT_LATE',
 'Pay_status_pots_M3_LATE_SAME_MONTH',
 'Pay_status_pots_M3_NOT_LATE',
 'Pay_status_pots_M4_LATE_SAME_MONTH',
 'Pay_status_pots_M4_NOT_LATE',
 'Pay_status_pots_M5_LATE_NEXT_MONTH',
 'Pay_status_pots_M5_LATE_SAME_MONTH',
 'Pay_status_pots_M5_NOT_LATE',
 'Pay_status_pots_M6_LATE_NEXT_MONTH',
 'Pay_status_pots_M6_LATE_SAME_MONTH',
 'Pay_status_pots_M6_NOT_LATE',
 'Speed_1024.0',
 'Speed_10240.0',
 'Speed_102400.0',
 'Speed_2048.0',
 'Speed_204800.0',
 'Speed_30720.0',
 'Speed_40960.0',
 'Speed_51200.0',
 'Divre_id_2',
 'Divre_id_4',
 'Divre_id_5',
 'Divre_id_6',
 'Divre_id_7',
 'Technology_FIBER',
 'Technology_NON-FIBER',
 'Indihome_type_3P']


# In[264]:


len(selected_columns)


# In[265]:


x_train_selected = x_train[selected_columns]


# In[266]:


x_test_selected = x_test[selected_columns]


# In[254]:


# Heatmap Correlation
plt.figure(figsize=(20,20))
sns.heatmap(x_train_selected.corr(), annot = True)


# ## 4. Training Machine Learning Model

# ### Scaling

# In[267]:


# Standard Scaling
from sklearn.preprocessing import StandardScaler

# Standardize Training Data
def standardizer(data):
    data_columns = data.columns  # agar nama column tidak hilang
    data_index = data.index # agar index tidak hilang
    normalize = StandardScaler()
    normalize.fit(data)
    
    normalize_x = pd.DataFrame(normalize.transform(data), index = data_index)
    normalize_x.columns = data_columns
    return normalize_x, normalize

# Standardize Testing Data
def standard_data(numerical_data, standard):
    numerical_data_columns  = list(numerical_data)
    numerical_data_standard = pd.DataFrame(standard.transform(numerical_data), index = numerical_data.index) # standardization
    numerical_data_standard.columns = numerical_data_columns # samakan nama column
        
    return numerical_data_standard


# In[268]:


x_train_standardized, standardizer = standardizer(x_train_selected)
x_test_standardized = standard_data(x_test_selected, standardizer)


# ### Benchmark

# In[269]:


y_train.value_counts(normalize=True)


# * Angka terbesar adalah benchmark, yaitu 70,1%
# * Sekarand Anda diminta untuk dapat membuat model machine learning dengan akurasi lebih dari 70,1%

# ### Logistic Regression Model (w/o cross-validation)

# In[270]:


from sklearn.linear_model import LogisticRegression


# In[271]:


# Define Model
logit = LogisticRegression(random_state=123)

# Run Model
model_logit = logit.fit(x_train_standardized, y_train)


# ### Logistic Regression Model (w cross-validation)

# In[272]:


# Cross Validation: Hyperparameter Tuning
from sklearn.model_selection import RandomizedSearchCV

def bestparam_randCV(model,hyperparam,x_train, y_train, n_iter=10):
    
    hyperparam = hyperparam
    randomizedCV = RandomizedSearchCV(model, param_distributions = hyperparam, cv = 10,
                                      n_iter = n_iter, scoring = 'roc_auc', n_jobs=1, 
                                      random_state = 123, verbose = True)
    randomizedCV.fit(x_train, y_train)
    
    print("Best ROC_AUC", randomizedCV.score(x_train, y_train))
    print("Best Param", randomizedCV.best_params_)
    return randomizedCV


# In[273]:


# Define Model
logit = LogisticRegression(random_state=123)

# Get the best Hyperparameter
hyperparam = {'penalty': ['l2'],
              'C': [100000, 33333, 10000, 3333, 1000, 333, 100, 33.33,
                  10, 3.33, 10, 3.33, 1, 0.33, 0.1, 0.033, 0.01]}
n_iter     = 10
best_logit = bestparam_randCV(logit, hyperparam, x_train_standardized, y_train, n_iter)


# print(best_logit.best_params_.get('C'))

# In[274]:


# Initialize Classifier
logit = LogisticRegression(C            = best_logit.best_params_.get('C'), 
                           penalty      = best_logit.best_params_.get('penalty'), 
                           random_state = 123)

# Run Model
model_best_logit = logit.fit(x_train_standardized, y_train)


# In[275]:


model_best_logit


# ## 5. Evaluation

# ### Model Performance

# In[276]:


from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
# from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score

def model_performace(model, x_test, y_test):
    #Make Prediction
    y_pred       = model.predict(x_test)
    y_pred_proba = model.predict_proba(x_test)

    #Generate model performance
    print('')
    print(classification_report(y_test, y_pred))

    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

    print('Confusion Matrix : ' + "[" + str(tp) + "," + str(fp) + "][" + str(fn) + "," + str(tn) + "]")
    print("")

    score_rocauc = roc_auc_score(y_test, y_pred_proba[:,1])
    
    # Manual Calculation
    print('Accuracy      : {0:2.6f}'.format((tp+tn)*1./(tp+fp+tn+fn)))
    print('Sensitivity   : {0:2.6f}'.format((tp)*1./(tp+fn)))
    print('Spesificity   : {0:2.6f}'.format((tn)*1./(tn+fp)))
    print('Precision     : {0:2.6f}'.format((tp)*1./(tp+fp)))
    print('ROC AUC Score : {0:2.6f}'.format(score_rocauc))
    
    # Using Library
#     print('Accuracy      : {0:2.6f}'.format(accuracy_score(y_test, y_pred)))
#     print('Sensitivity   : {0:2.6f}'.format(recall_score(y_test, y_pred)))
#     print('Precision     : {0:2.6f}'.format(precision_score(y_test, y_pred)))
    
    return score_rocauc, y_pred, y_pred_proba


# ### Performance w/o Hyperparameter Tuning

# In[277]:


# Performance Training
auc_train, y_pred_train, y_proba_train = model_performace(model_logit, x_train_standardized, y_train)


# In[278]:


# Performance Testing
auc_test, y_pred_test, y_proba_test = model_performace(model_logit, x_test_standardized, y_test)


# * Nilai Accuracy <font color='orange'>0.843</font> melebihi nilai benchmark <font color='orange'>0.701
# * Nilai Accuracy, Sensitivity, Precision, dan AUC tidak berbeda secara signifikan maka dapat diasumsikan bahwa model tidak mengalami overfitting

# ### Performance w Hyperparameter Tuning

# In[279]:


# Performance Training
auc_train, y_pred_train, y_proba_train = model_performace(model_best_logit, x_train_standardized, y_train)


# In[280]:


# Performance Testing
auc_test, y_pred_test, y_proba_test = model_performace(model_best_logit, x_test_standardized, y_test)


# * Hasil score AUC dengan hyperparameter tuning <font color='orange'>0.844134</font> lebih tinggi dibandingkan dengan tidak memakai hyperparameter tuning <font color='orange'>0.84397</font>

# ### ROC Curve

# In[281]:


import scikitplot as skplt

def plot_roc(y_actual, y_proba):
    plt.figure(figsize=(20,10))
    
    aucroc_score     = roc_auc_score(y_actual, y_proba[:,1])
    skplt.metrics.plot_roc(y_actual, y_proba, plot_micro=False,plot_macro=False, 
                           title='ROC Curve\nArea under Curve = %0.4f' % aucroc_score,
                           title_fontsize = 16, text_fontsize = 12)
      
    plt.show()


# In[282]:


# ROC Train
plot_roc(y_train, y_proba_train)


# In[283]:


# ROC Test
plot_roc(y_test, y_proba_test)


# In[77]:


feattr                 = x_train_standardized.columns
feature_importance     = model_best_logit.coef_.ravel()
feature_importance_abs = np.abs(feature_importance)
index_sort             = np.argsort(feature_importance_abs)[::-1]

for i in range(len(feattr)):
    print(feattr[index_sort[i]], feature_importance[index_sort[i]])
    
print('Intercept', model_best_logit.intercept_[0])


# ### Save Model

# In[284]:


import pickle


# In[285]:


pickle.dump(model_best_logit, open('model_logit_all_Month_no_filter_1.pkl', 'wb'))


# ## 6. Deployment (Test With Data Submission)

# ### Load Data Submission

# In[ ]:


SUBMISSION_POP=pd.read_sql_query("SELECT ID_CUSTOMER,LENGTH_OF_STAY,DIVRE_ID,TECHNOLOGY,KW,INDIHOME_TYPE,TOTAL_MINIPACK FROM SUBMISSION_POP;",conn)
SUBMISSION_SPEED=pd.read_sql_query("SELECT ID_CUSTOMER,Speed FROM SUBMISSION_SPEED;",conn)



SUBMISSION_USEE_USAGE_M1=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM SUBMISSION_USEE_USAGE WHERE PERIODE = 'M1';",conn)
SUBMISSION_USEE_USAGE_M2=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM SUBMISSION_USEE_USAGE WHERE PERIODE = 'M2';",conn)
SUBMISSION_USEE_USAGE_M3=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM SUBMISSION_USEE_USAGE WHERE PERIODE = 'M3';",conn)
SUBMISSION_USEE_USAGE_M4=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM SUBMISSION_USEE_USAGE WHERE PERIODE = 'M4';",conn)
SUBMISSION_USEE_USAGE_M5=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM SUBMISSION_USEE_USAGE WHERE PERIODE = 'M5';",conn)
SUBMISSION_USEE_USAGE_M6=pd.read_sql_query("SELECT ID_CUSTOMER, GENRE_PROGRAM,FREQ,DUREE FROM SUBMISSION_USEE_USAGE WHERE PERIODE = 'M6';",conn)

SUBMISSION_INET_USAGE_M1=pd.read_sql_query("SELECT * FROM SUBMISSION_INET_USAGE WHERE PERIODE = 'M1';",conn)
SUBMISSION_INET_USAGE_M2=pd.read_sql_query("SELECT * FROM SUBMISSION_INET_USAGE WHERE PERIODE = 'M2';",conn)
SUBMISSION_INET_USAGE_M3=pd.read_sql_query("SELECT * FROM SUBMISSION_INET_USAGE WHERE PERIODE = 'M3';",conn)
SUBMISSION_INET_USAGE_M4=pd.read_sql_query("SELECT * FROM SUBMISSION_INET_USAGE WHERE PERIODE = 'M4';",conn)
SUBMISSION_INET_USAGE_M5=pd.read_sql_query("SELECT * FROM SUBMISSION_INET_USAGE WHERE PERIODE = 'M5';",conn)
SUBMISSION_INET_USAGE_M6=pd.read_sql_query("SELECT * FROM SUBMISSION_INET_USAGE WHERE PERIODE = 'M6';",conn)


# In[ ]:



SUBMISSION_POTS_PAY_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_POTS_PAY WHERE PERIODE = 'M1';",conn)
SUBMISSION_POTS_PAY_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_POTS_PAY WHERE PERIODE = 'M2';",conn)
SUBMISSION_POTS_PAY_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_POTS_PAY WHERE PERIODE = 'M3';",conn)
SUBMISSION_POTS_PAY_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_POTS_PAY WHERE PERIODE = 'M4';",conn)
SUBMISSION_POTS_PAY_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_POTS_PAY WHERE PERIODE = 'M5';",conn)
SUBMISSION_POTS_PAY_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_POTS_PAY WHERE PERIODE = 'M6';",conn)


SUBMISSION_INET_PAY_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_INET_PAY WHERE PERIODE = 'M1';",conn)
SUBMISSION_INET_PAY_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_INET_PAY WHERE PERIODE = 'M2';",conn)
SUBMISSION_INET_PAY_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_INET_PAY WHERE PERIODE = 'M3';",conn)
SUBMISSION_INET_PAY_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_INET_PAY WHERE PERIODE = 'M4';",conn)
SUBMISSION_INET_PAY_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_INET_PAY WHERE PERIODE = 'M5';",conn)
SUBMISSION_INET_PAY_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Payment,Pay_status FROM SUBMISSION_INET_PAY WHERE PERIODE = 'M6';",conn)

SUBMISSION_INET_TICKET_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_INET_TICKET WHERE PERIODE = 'M1';",conn)
SUBMISSION_INET_TICKET_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_INET_TICKET WHERE PERIODE = 'M2';",conn)
SUBMISSION_INET_TICKET_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_INET_TICKET WHERE PERIODE = 'M3';",conn)
SUBMISSION_INET_TICKET_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_INET_TICKET WHERE PERIODE = 'M4';",conn)
SUBMISSION_INET_TICKET_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_INET_TICKET WHERE PERIODE = 'M5';",conn)
SUBMISSION_INET_TICKET_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_INET_TICKET WHERE PERIODE = 'M6';",conn)

SUBMISSION_POTS_TICKET_M1=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_POTS_TICKET WHERE PERIODE = 'M1';",conn)
SUBMISSION_POTS_TICKET_M2=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_POTS_TICKET WHERE PERIODE = 'M2';",conn)
SUBMISSION_POTS_TICKET_M3=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_POTS_TICKET WHERE PERIODE = 'M3';",conn)
SUBMISSION_POTS_TICKET_M4=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_POTS_TICKET WHERE PERIODE = 'M4';",conn)
SUBMISSION_POTS_TICKET_M5=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_POTS_TICKET WHERE PERIODE = 'M5';",conn)
SUBMISSION_POTS_TICKET_M6=pd.read_sql_query("SELECT Tipe_gangguan,N_ticket,Mttr FROM SUBMISSION_POTS_TICKET WHERE PERIODE = 'M6';",conn)


# In[ ]:



SUBMISSION_POTS_REV_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_POTS_REV WHERE PERIODE = 'M1';",conn)
SUBMISSION_POTS_REV_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_POTS_REV WHERE PERIODE = 'M2';",conn)
SUBMISSION_POTS_REV_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_POTS_REV WHERE PERIODE = 'M3';",conn)
SUBMISSION_POTS_REV_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_POTS_REV WHERE PERIODE = 'M4';",conn)
SUBMISSION_POTS_REV_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_POTS_REV WHERE PERIODE = 'M5';",conn)
SUBMISSION_POTS_REV_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_POTS_REV WHERE PERIODE = 'M6';",conn)


SUBMISSION_INET_REV_M1=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_INET_REV WHERE PERIODE = 'M1';",conn)
SUBMISSION_INET_REV_M2=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_INET_REV WHERE PERIODE = 'M2';",conn)
SUBMISSION_INET_REV_M3=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_INET_REV WHERE PERIODE = 'M3';",conn)
SUBMISSION_INET_REV_M4=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_INET_REV WHERE PERIODE = 'M4';",conn)
SUBMISSION_INET_REV_M5=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_INET_REV WHERE PERIODE = 'M5';",conn)
SUBMISSION_INET_REV_M6=pd.read_sql_query("SELECT ID_CUSTOMER,Revenue_billing FROM SUBMISSION_INET_REV WHERE PERIODE = 'M6';",conn)


SUBMISSION_POTS_USAGE_M1=pd.read_sql_query("SELECT * FROM SUBMISSION_POTS_USAGE WHERE PERIODE = 'M1';",conn)
SUBMISSION_POTS_USAGE_M2=pd.read_sql_query("SELECT * FROM SUBMISSION_POTS_USAGE WHERE PERIODE = 'M2';",conn)
SUBMISSION_POTS_USAGE_M3=pd.read_sql_query("SELECT * FROM SUBMISSION_POTS_USAGE WHERE PERIODE = 'M3';",conn)
SUBMISSION_POTS_USAGE_M4=pd.read_sql_query("SELECT * FROM SUBMISSION_POTS_USAGE WHERE PERIODE = 'M4';",conn)
SUBMISSION_POTS_USAGE_M5=pd.read_sql_query("SELECT * FROM SUBMISSION_POTS_USAGE WHERE PERIODE = 'M5';",conn)
SUBMISSION_POTS_USAGE_M6=pd.read_sql_query("SELECT * FROM SUBMISSION_POTS_USAGE WHERE PERIODE = 'M6';",conn)

SUBMISSION_USEE_USAGE_M1 = SUBMISSION_USEE_USAGE_M1.rename({ 'GENRE_PROGRAM': 'Genre_program_M1','FREQ': 'Freq_M1', 'DUREE': 'Duree_M1'}, axis=1)
SUBMISSION_USEE_USAGE_M2 = SUBMISSION_USEE_USAGE_M2.rename({ 'GENRE_PROGRAM': 'Genre_program_M2','FREQ': 'Freq_M2', 'DUREE': 'Duree_M2'}, axis=1)
SUBMISSION_USEE_USAGE_M3 = SUBMISSION_USEE_USAGE_M3.rename({'GENRE_PROGRAM': 'Genre_program_M3','FREQ': 'Freq_M3', 'DUREE': 'Duree_M3'}, axis=1)
SUBMISSION_USEE_USAGE_M4 = SUBMISSION_USEE_USAGE_M4.rename({ 'GENRE_PROGRAM': 'Genre_program_M4','FREQ': 'Freq_M4', 'DUREE': 'Duree_M4'}, axis=1)
SUBMISSION_USEE_USAGE_M5 = SUBMISSION_USEE_USAGE_M5.rename({ 'GENRE_PROGRAM': 'Genre_program_M5','FREQ': 'Freq_M5', 'DUREE': 'Duree_M5'}, axis=1)
SUBMISSION_USEE_USAGE_M6 = SUBMISSION_USEE_USAGE_M6.rename({'GENRE_PROGRAM': 'Genre_program_M6','FREQ': 'Freq_M6', 'DUREE': 'Duree_M6'}, axis=1)


SUBMISSION_INET_USAGE_M1 = SUBMISSION_INET_USAGE_M1.rename({'TOTAL_FREQ': 'Total_Freq_M1', 'TOTAL_DURASI': 'Total_Durasi_M1','TOTAL_USAGE': 'Total_usage_M1', 'TOTAL_UPLOAD': 'Total_upload_M1', 'TOTAL_DOWNLOAD': 'Total_download_M1'}, axis=1)
SUBMISSION_INET_USAGE_M2 = SUBMISSION_INET_USAGE_M2.rename({'TOTAL_FREQ': 'Total_Freq_M2', 'TOTAL_DURASI': 'Total_Durasi_M2','TOTAL_USAGE': 'Total_usage_M2', 'TOTAL_UPLOAD': 'Total_upload_M2', 'TOTAL_DOWNLOAD': 'Total_download_M2'}, axis=1)
SUBMISSION_INET_USAGE_M3 = SUBMISSION_INET_USAGE_M3.rename({'TOTAL_FREQ': 'Total_Freq_M3', 'TOTAL_DURASI': 'Total_Durasi_M3','TOTAL_USAGE': 'Total_usage_M3', 'TOTAL_UPLOAD': 'Total_upload_M3', 'TOTAL_DOWNLOAD': 'Total_download_M3'}, axis=1)
SUBMISSION_INET_USAGE_M4 = SUBMISSION_INET_USAGE_M4.rename({'TOTAL_FREQ': 'Total_Freq_M4', 'TOTAL_DURASI': 'Total_Durasi_M4','TOTAL_USAGE': 'Total_usage_M4', 'TOTAL_UPLOAD': 'Total_upload_M4', 'TOTAL_DOWNLOAD': 'Total_download_M4'}, axis=1)
SUBMISSION_INET_USAGE_M5 = SUBMISSION_INET_USAGE_M5.rename({'TOTAL_FREQ': 'Total_Freq_M5', 'TOTAL_DURASI': 'Total_Durasi_M5','TOTAL_USAGE': 'Total_usage_M5', 'TOTAL_UPLOAD': 'Total_upload_M5', 'TOTAL_DOWNLOAD': 'Total_download_M5'}, axis=1)
SUBMISSION_INET_USAGE_M6 = SUBMISSION_INET_USAGE_M6.rename({'TOTAL_FREQ': 'Total_Freq_M6', 'TOTAL_DURASI': 'Total_Durasi_M6','TOTAL_USAGE': 'Total_usage_M6', 'TOTAL_UPLOAD': 'Total_upload_M6', 'TOTAL_DOWNLOAD': 'Total_download_M6'}, axis=1)


# In[ ]:



SUBMISSION_POTS_PAY_M1 = SUBMISSION_POTS_PAY_M1.rename({'Payment': 'Payment_pots_M1', 'Pay_status': 'Pay_status_pots_M1'}, axis=1)
SUBMISSION_POTS_PAY_M2 = SUBMISSION_POTS_PAY_M2.rename({'Payment': 'Payment_pots_M2', 'Pay_status': 'Pay_status_pots_M2'}, axis=1)
SUBMISSION_POTS_PAY_M3 = SUBMISSION_POTS_PAY_M3.rename({'Payment': 'Payment_pots_M3', 'Pay_status': 'Pay_status_pots_M3'}, axis=1)
SUBMISSION_POTS_PAY_M4 = SUBMISSION_POTS_PAY_M4.rename({'Payment': 'Payment_pots_M4', 'Pay_status': 'Pay_status_pots_M4'}, axis=1)
SUBMISSION_POTS_PAY_M5 = SUBMISSION_POTS_PAY_M5.rename({'Payment': 'Payment_pots_M5', 'Pay_status': 'Pay_status_pots_M5'}, axis=1)
SUBMISSION_POTS_PAY_M6 = SUBMISSION_POTS_PAY_M6.rename({'Payment': 'Payment_pots_M6', 'Pay_status': 'Pay_status_pots_M6'}, axis=1)

SUBMISSION_INET_PAY_M1 = SUBMISSION_INET_PAY_M1.rename({'Payment': 'Payment_inet_M1', 'Pay_status': 'Pay_status_inet_M1'}, axis=1)
SUBMISSION_INET_PAY_M2 = SUBMISSION_INET_PAY_M2.rename({'Payment': 'Payment_inet_M2', 'Pay_status': 'Pay_status_inet_M2'}, axis=1)
SUBMISSION_INET_PAY_M3 = SUBMISSION_INET_PAY_M3.rename({'Payment': 'Payment_inet_M3', 'Pay_status': 'Pay_status_inet_M3'}, axis=1)
SUBMISSION_INET_PAY_M4 = SUBMISSION_INET_PAY_M4.rename({'Payment': 'Payment_inet_M4', 'Pay_status': 'Pay_status_inet_M4'}, axis=1)
SUBMISSION_INET_PAY_M5 = SUBMISSION_INET_PAY_M5.rename({'Payment': 'Payment_inet_M5', 'Pay_status': 'Pay_status_inet_M5'}, axis=1)
SUBMISSION_INET_PAY_M6 = SUBMISSION_INET_PAY_M6.rename({'Payment': 'Payment_inet_M6', 'Pay_status': 'Pay_status_inet_M6'}, axis=1)



SUBMISSION_INET_TICKET_M1 = SUBMISSION_INET_TICKET_M1.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M1', 'N_ticket': 'N_ticket_inet_M1', 'Mttr': 'Mttr_inet_M1'}, axis=1)
SUBMISSION_INET_TICKET_M2 = SUBMISSION_INET_TICKET_M2.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M2', 'N_ticket': 'N_ticket_inet_M2', 'Mttr': 'Mttr_inet_M2'}, axis=1)
SUBMISSION_INET_TICKET_M3 = SUBMISSION_INET_TICKET_M3.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M3', 'N_ticket': 'N_ticket_inet_M3', 'Mttr': 'Mttr_inet_M3'}, axis=1)
SUBMISSION_INET_TICKET_M4 = SUBMISSION_INET_TICKET_M4.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M4', 'N_ticket': 'N_ticket_inet_M4', 'Mttr': 'Mttr_inet_M4'}, axis=1)
SUBMISSION_INET_TICKET_M5 = SUBMISSION_INET_TICKET_M5.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M5', 'N_ticket': 'N_ticket_inet_M5', 'Mttr': 'Mttr_inet_M5'}, axis=1)
SUBMISSION_INET_TICKET_M6 = SUBMISSION_INET_TICKET_M6.rename({'Tipe_gangguan': 'Tipe_gangguan_inet_M6', 'N_ticket': 'N_ticket_inet_M6', 'Mttr': 'Mttr_inet_M6'}, axis=1)


SUBMISSION_POTS_TICKET_M1 = SUBMISSION_POTS_TICKET_M1.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M1', 'N_ticket': 'N_ticket_pots_M1', 'Mttr': 'Mttr_pots_M1'}, axis=1)
SUBMISSION_POTS_TICKET_M2 = SUBMISSION_POTS_TICKET_M2.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M2', 'N_ticket': 'N_ticket_pots_M2', 'Mttr': 'Mttr_pots_M2'}, axis=1)
SUBMISSION_POTS_TICKET_M3 = SUBMISSION_POTS_TICKET_M3.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M3', 'N_ticket': 'N_ticket_pots_M3', 'Mttr': 'Mttr_pots_M3'}, axis=1)
SUBMISSION_POTS_TICKET_M4 = SUBMISSION_POTS_TICKET_M4.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M4', 'N_ticket': 'N_ticket_pots_M4', 'Mttr': 'Mttr_pots_M4'}, axis=1)
SUBMISSION_POTS_TICKET_M5 = SUBMISSION_POTS_TICKET_M5.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M5', 'N_ticket': 'N_ticket_pots_M5', 'Mttr': 'Mttr_pots_M5'}, axis=1)
SUBMISSION_POTS_TICKET_M6 = SUBMISSION_POTS_TICKET_M6.rename({'Tipe_gangguan': 'Tipe_gangguan_pots_M6', 'N_ticket': 'N_ticket_pots_M6', 'Mttr': 'Mttr_pots_M6'}, axis=1)


# In[ ]:



SUBMISSION_POTS_REV_M1 = SUBMISSION_POTS_REV_M1.rename({'Revenue_billing': 'Revenue_billing_pots_M1'}, axis=1)
SUBMISSION_POTS_REV_M2 = SUBMISSION_POTS_REV_M2.rename({'Revenue_billing': 'Revenue_billing_pots_M2'}, axis=1)
SUBMISSION_POTS_REV_M3 = SUBMISSION_POTS_REV_M3.rename({'Revenue_billing': 'Revenue_billing_pots_M3'}, axis=1)
SUBMISSION_POTS_REV_M4 = SUBMISSION_POTS_REV_M4.rename({'Revenue_billing': 'Revenue_billing_pots_M4'}, axis=1)
SUBMISSION_POTS_REV_M5 = SUBMISSION_POTS_REV_M5.rename({'Revenue_billing': 'Revenue_billing_pots_M5'}, axis=1)
SUBMISSION_POTS_REV_M6 = SUBMISSION_POTS_REV_M6.rename({'Revenue_billing': 'Revenue_billing_pots_M6'}, axis=1)

SUBMISSION_INET_REV_M1 = SUBMISSION_INET_REV_M1.rename({'Revenue_billing': 'Revenue_billing_inet_M1'}, axis=1)
SUBMISSION_INET_REV_M2 = SUBMISSION_INET_REV_M2.rename({'Revenue_billing': 'Revenue_billing_inet_M2'}, axis=1)
SUBMISSION_INET_REV_M3 = SUBMISSION_INET_REV_M3.rename({'Revenue_billing': 'Revenue_billing_inet_M3'}, axis=1)
SUBMISSION_INET_REV_M4 = SUBMISSION_INET_REV_M4.rename({'Revenue_billing': 'Revenue_billing_inet_M4'}, axis=1)
SUBMISSION_INET_REV_M5 = SUBMISSION_INET_REV_M5.rename({'Revenue_billing': 'Revenue_billing_inet_M5'}, axis=1)
SUBMISSION_INET_REV_M6 = SUBMISSION_INET_REV_M6.rename({'Revenue_billing': 'Revenue_billing_inet_M6'}, axis=1)


# In[ ]:


#Join Pop , Speed and Usee Usage
SUBMISSION_JOIN = SUBMISSION_POP.merge(SUBMISSION_SPEED,on='ID_CUSTOMER',how='left').merge(SUBMISSION_USEE_USAGE_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_USEE_USAGE_M1,on='ID_CUSTOMER',how='left').merge(SUBMISSION_USEE_USAGE_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_USEE_USAGE_M3,on='ID_CUSTOMER',how='left').merge(SUBMISSION_USEE_USAGE_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_USEE_USAGE_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_USEE_USAGE_M5,on='ID_CUSTOMER',how='left').merge(SUBMISSION_USEE_USAGE_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


SUBMISSION_JOIN = SUBMISSION_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join inet pay
SUBMISSION_JOIN = SUBMISSION_JOIN.merge(SUBMISSION_INET_PAY_M1,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_PAY_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_PAY_M3,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_PAY_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_PAY_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_PAY_M5,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_PAY_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


SUBMISSION_JOIN = SUBMISSION_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:


#join inet usage
SUBMISSION_JOIN=SUBMISSION_JOIN.merge(SUBMISSION_INET_USAGE_M1,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_USAGE_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_USAGE_M3,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_USAGE_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_USAGE_M5,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_USAGE_M6,on='ID_CUSTOMER',how='left')


# In[ ]:



#join pots pay
SUBMISSION_JOIN = SUBMISSION_JOIN.merge(SUBMISSION_POTS_PAY_M1,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_PAY_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_PAY_M3,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_PAY_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_PAY_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_PAY_M5,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_PAY_M6,on='ID_CUSTOMER',how='left')


# In[ ]:



SUBMISSION_JOIN = SUBMISSION_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:



#JOIN pots ticket
SUBMISSION_JOIN = SUBMISSION_JOIN.merge(SUBMISSION_POTS_TICKET_M1,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_TICKET_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_TICKET_M3,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_TICKET_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_TICKET_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_TICKET_M5,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_TICKET_M6,on='ID_CUSTOMER',how='left')


# In[ ]:



#join inet ticket
SUBMISSION_JOIN = SUBMISSION_JOIN.merge(SUBMISSION_INET_TICKET_M1,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_TICKET_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_TICKET_M3,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_TICKET_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_TICKET_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_TICKET_M5,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_TICKET_M6,on='ID_CUSTOMER',how='left')


# In[ ]:



SUBMISSION_JOIN = SUBMISSION_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:



#join inet rev
SUBMISSION_JOIN = SUBMISSION_JOIN.merge(SUBMISSION_INET_REV_M1,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_REV_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_REV_M3,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_REV_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_REV_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_REV_M5,on='ID_CUSTOMER',how='left').merge(SUBMISSION_INET_REV_M6,on='ID_CUSTOMER',how='left')


# In[ ]:



SUBMISSION_JOIN = SUBMISSION_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:



#join pots rev
SUBMISSION_JOIN = SUBMISSION_JOIN.merge(SUBMISSION_POTS_REV_M1,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_REV_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_REV_M3,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_REV_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_REV_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_REV_M5,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_REV_M6,on='ID_CUSTOMER',how='left')


# In[ ]:



SUBMISSION_JOIN = SUBMISSION_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:



#join pots usage
SUBMISSION_JOIN = SUBMISSION_JOIN.merge(SUBMISSION_POTS_USAGE_M1,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_USAGE_M2,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_USAGE_M3,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_USAGE_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_USAGE_M4,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_USAGE_M5,on='ID_CUSTOMER',how='left').merge(SUBMISSION_POTS_USAGE_M6,on='ID_CUSTOMER',how='left')


# In[ ]:


SUBMISSION_JOIN = SUBMISSION_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[ ]:



#join pop and speed
SUBMISSION_JOIN = SUBMISSION_JOIN.merge(SUBMISSION_POP,on='ID_CUSTOMER',how='left').merge(SUBMISSION_SPEED,on='ID_CUSTOMER',how='left')


# In[ ]:



SUBMISSION_JOIN = SUBMISSION_JOIN.drop_duplicates(subset='ID_CUSTOMER', keep="last")


# In[242]:


SUBMISSION_JOIN.to_csv('SUBMISSIONSET_ALLMONTH.csv', index = False)


# In[286]:


# baca data CSV, jadikan variable df_load
SUBMISSION = pd.read_csv("SUBMISSIONSET_ALLMONTH.csv",delimiter=';') 


# ### Drop Duplicate

# In[287]:


SUBMISSION = SUBMISSION.drop_duplicates()


# ### Check Missing Value

# In[288]:


# Check Total Missing Value
SUBMISSION.isnull().mean().sort_values(ascending=False)


# In[289]:


SUBMISSION.drop(['Tipe_gangguan_pots_M1','Tipe_gangguan_pots_M2','Tipe_gangguan_pots_M3','Tipe_gangguan_pots_M4','Tipe_gangguan_pots_M5','Tipe_gangguan_pots_M6','Tipe_gangguan_inet_M1','Tipe_gangguan_inet_M2','Tipe_gangguan_inet_M3','Tipe_gangguan_inet_M4','Tipe_gangguan_inet_M5','Tipe_gangguan_inet_M6','Genre_program_inet_M1','Genre_program_inet_M2','Genre_program_inet_M3','Genre_program_inet_M4','Genre_program_inet_M5','Genre_program_inet_M6','Call_lokal_M1','Call_lokal_M2','Call_lokal_M3','Call_lokal_M4','Call_lokal_M5','Call_lokal_M6','Call_sljj_M1','Call_sljj_M2','Call_sljj_M3','Call_sljj_M4','Call_sljj_M5','Call_sljj_M6','Call_mobile_M1','Call_mobile_M2','Call_mobile_M3','Call_mobile_M4','Call_mobile_M5','Call_mobile_M6','Call_sli_M1','Call_sli_M2','Call_sli_M3','Call_sli_M4','Call_sli_M5','Call_sli_M6','Call_other_M1','Call_other_M2','Call_other_M3','Call_other_M4','Call_other_M5','Call_other_M6','Duree_lokal_M1','Duree_lokal_M2','Duree_lokal_M3','Duree_lokal_M4','Duree_lokal_M5','Duree_lokal_M6','Duree_sljj_M1','Duree_sljj_M2','Duree_sljj_M3','Duree_sljj_M4','Duree_sljj_M5','Duree_sljj_M6','Duree_mobile_M1','Duree_mobile_M2','Duree_mobile_M3','Duree_mobile_M4','Duree_mobile_M5','Duree_mobile_M6','Duree_sli_M1','Duree_sli_M2','Duree_sli_M3','Duree_sli_M4','Duree_sli_M5','Duree_sli_M6','Duree_other_M1','Duree_other_M2','Duree_other_M3','Duree_other_M4','Duree_other_M5','Duree_other_M6','Revenue_billing_pots_M1','Revenue_billing_pots_M2','Revenue_billing_pots_M3','Revenue_billing_pots_M4','Revenue_billing_pots_M5','Revenue_billing_pots_M6','N_ticket_pots_M1','N_ticket_pots_M2','N_ticket_pots_M3','N_ticket_pots_M4','N_ticket_pots_M5','N_ticket_pots_M6','Mttr_pots_M1','Mttr_pots_M2','Mttr_pots_M3','Mttr_pots_M4','Mttr_pots_M5','Mttr_pots_M6','N_ticket_inet_M1','N_ticket_inet_M2','N_ticket_inet_M3','N_ticket_inet_M4','N_ticket_inet_M5','N_ticket_inet_M6','Mttr_inet_M1','Mttr_inet_M2','Mttr_inet_M3','Mttr_inet_M4','Mttr_inet_M5','Mttr_inet_M6','Freq_M1','Freq_M2','Freq_M3','Freq_M4','Freq_M5','Freq_M6','Duree_M1','Duree_M2','Duree_M3','Duree_M4','Duree_M5','Duree_M6','Total_Minipack'], axis=1, inplace = True)


# ### GET ID

# In[290]:


id_col = ['Id_customer']
df_id  = SUBMISSION.filter(id_col, axis=1)
df_id.head()


# In[291]:


SUBMISSION.drop(id_col, axis=1, inplace = True)


# In[292]:


SUBMISSION.head()


# ### Get X attributes

# In[293]:


print(SUBMISSION.shape)


# In[294]:


X_deploy = SUBMISSION


# In[295]:


# Define Categorical Columns
cat_col = ['Pay_status_inet_M1','Pay_status_inet_M2','Pay_status_inet_M3','Pay_status_inet_M4','Pay_status_inet_M5','Pay_status_inet_M6','Pay_status_pots_M1','Pay_status_pots_M2','Pay_status_pots_M3','Pay_status_pots_M4','Pay_status_pots_M5','Pay_status_pots_M6','Tipe_gangguan_pots_M1','Tipe_gangguan_pots_M2','Tipe_gangguan_pots_M3','Tipe_gangguan_pots_M4','Tipe_gangguan_pots_M5','Tipe_gangguan_pots_M6','Tipe_gangguan_inet_M1','Tipe_gangguan_inet_M2','Tipe_gangguan_inet_M3','Tipe_gangguan_inet_M4','Tipe_gangguan_inet_M5','Tipe_gangguan_inet_M6','Genre_program_inet_M1','Genre_program_inet_M2','Genre_program_inet_M3','Genre_program_inet_M4','Genre_program_inet_M5','Genre_program_inet_M6','Speed','Divre_id','Technology','Kw','Indihome_type']


# In[296]:


# Get Numerical Columns using Set
num_col = list(set(X_deploy.columns) - set(cat_col))
num_col


# In[297]:


x_numerical   = X_deploy.filter(num_col, axis=1)
x_categorical = X_deploy.filter(cat_col, axis=1)


# ### Outlier Handling for Numerical Data

# In[298]:


# Capping X_test values: AVG(X) +- 3*STDDEV(X)
more_than_up_bound   = (x_numerical > up_bound)
lower_than_low_bound = (x_numerical < low_bound)
df_cap               = x_numerical.mask(more_than_up_bound, up_bound, axis=1) 
df_cap               = df_cap.mask(lower_than_low_bound, low_bound, axis=1)
x_numerical          = df_cap

# Check data shape
print(x_numerical.shape)


# ### Numerical Imputation

# In[299]:


# from sklearn.preprocessing import Imputer # Old Version
from sklearn.impute import SimpleImputer

# Impute Prediction Data
def imput_numeric(numerical_data, imput_numerical):
    numerical_data_columns = list(numerical_data)
    numerical_data_imput   = pd.DataFrame(imput_numerical.transform(numerical_data), index = numerical_data.index) # imput numerical test
    numerical_data_imput.columns = numerical_data_columns
        
    return numerical_data_imput


# In[300]:


x_numerical_imputed, imput_numerical = numericalImputation(x_numerical)


# In[301]:


# Cek apakah ada data numerical yang kosong
x_numerical_imputed.isnull().any()


# In[302]:


x_numerical_imputed.shape


# In[303]:


x_numerical_imputed.isnull().mean().sort_values(ascending=False)


# ### Categorical Imputation

# In[304]:


# Isi NaN dari categorical data dengan value baru == "KOSONG"
x_categorical_imputed = x_categorical.fillna(value="KOSONG")


# In[305]:


# Cek apakah ada data numerical yang kosong
x_categorical_imputed.isnull().any()


# In[306]:


x_categorical_imputed.shape


# ### Categorical Dummy Variables

# In[307]:


x_categorical_dummy = pd.get_dummies(x_categorical_imputed.astype(str))


# In[308]:


x_categorical_dummy.shape


# In[309]:


x_join = pd.concat([x_numerical_imputed, x_categorical_dummy], axis =1)


# In[310]:


x_join.shape


# ### Get Selected Features

# In[311]:


x_join.isnull().any()


# In[312]:


x_categorical_dummy.shape


# In[313]:


x_numerical_imputed.isnull().any()


# In[314]:


x_selected = x_join[selected_columns]


# In[315]:


x_selected.isnull().any()


# ### Scaling

# In[316]:


# Standard Scaling
from sklearn.preprocessing import StandardScaler

# Standardize Prediction Data
def standard_data(numerical_data, standard):
    numerical_data_columns  = list(numerical_data)
    numerical_data_standard = pd.DataFrame(standard.transform(numerical_data), index = numerical_data.index) # standardization
    numerical_data_standard.columns = numerical_data_columns # samakan nama column
        
    return numerical_data_standard

x_standardized = standard_data(x_selected, standardizer)


# ### Make a Prediction

# In[317]:


# Load Model
model = pickle.load(open('model_logit_all_Month_no_filter_1.pkl', 'rb'))


# In[318]:


# Check Total Missing Value
x_standardized.isnull().mean().sort_values(ascending=False)


# In[320]:


y_pred       = model.predict(x_standardized)
y_pred_proba = model.predict_proba(x_standardized)


# ### Make a Dataframe from y_pred and y_pred_proba

# In[321]:


y_pred        = pd.DataFrame(y_pred)
y_pred_proba  = pd.DataFrame(y_pred_proba[:,1])


# In[322]:


df_id['id'] = df_id['Id_customer']
df_id['prob'] = y_pred_proba


# In[323]:



df_id.drop('Id_customer', axis=1, inplace = True)


# In[324]:


df_id.head()


# In[325]:


df_id.shape


# In[326]:


df_id.to_csv('940266_prediction_20211017_2.csv', index = False)


# In[218]:


get_ipython().system("jupyter nbconvert --to script '940266_script_2_m1.ipynb'")


# In[215]:


get_ipython().system('pip install ipynb-py-convert')

