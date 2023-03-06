#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing Speech Recognition library
import speech_recognition as sr


# In[2]:


rec = sr.Recognizer()

#print(sr.Microphone().list_microphone_names())
with sr.Microphone() as mic:
    #cleaning noise
    rec.adjust_for_ambient_noise(mic)
    print("Diga: 'Olá,mundo!'")
    
    #recondig your voice
    audio = rec.listen(mic)
    
    #convert audio for text from google open source database
    text = rec.recognize_google(audio, language = "pt-BR")
    
    print(text)


# In[ ]:




