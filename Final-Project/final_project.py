#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 


# In[2]:


receiver_list = open('receiver_list.txt')
a = receiver_list.readlines()


# In[3]:


receiver = []
for name in a:
    name = name.replace('\n', '')
    receiver.append(name)
print(receiver)


# In[4]:


html = Template(Path('thankyou.html').read_text())
email = EmailMessage()
email.set_content(html.substitute({'name': name}), 'html')
    
email['from'] = 'Najma'
email['to'] = receiver
email['subject'] = 'Final Project Basic Python'


# In[6]:


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('(ALAMAT_EMAIL)', '(PASSWORD_EMAIL)')
  smtp.send_message(email)
  print('email has been sent!')
print('email has been sent!')


# In[ ]:




