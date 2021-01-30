#!/usr/bin/env python
# coding: utf-8

# # Menggunakan data HTML

# In[1]:


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 


# In[2]:


receiver_list = open('receiver_list.txt')
a = receiver_list.readlines()


# In[3]:


a


# In[5]:


receiver = []
for name in a:
    name = name.replace('\n', '')
    receiver.append(name)
print(receiver)


# In[9]:


html = Template(Path('thankyou.html').read_text())
email = EmailMessage()
email.set_content(html.substitute({}), 'html')
    
email['from'] = 'Najma'
email['to'] = receiver
email['subject'] = 'Final Project Basic Python'


# In[10]:


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('EMAIL', 'PASSWORD')
  smtp.send_message(email)
  print('email has been sent!')


# In[ ]:





# In[ ]:





# In[ ]:





# # Tidak menggunakan file text

# In[20]:


import smtplib
from email.message import EmailMessage


# In[21]:


receiver_list = open('receiver_list.txt')
a = receiver_list.readlines()


# In[22]:


receiver = []
for name in a:
    name = name.replace('\n', '')
    receiver.append(name)
print(receiver)


# In[23]:


email = EmailMessage()
email['from'] = 'Najma'
email['to'] = receiver
email['subject'] = 'Your project send email worked!!'


# In[24]:


content = '''Hallo Future Data Scientist!'''
email.set_content(content)


# In[25]:


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('EMAIL', 'PASSWORD')
  smtp.send_message(email)
  print('email has been sent!')


# In[ ]:




