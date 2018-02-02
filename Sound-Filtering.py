
# coding: utf-8

# In[9]:


import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write     # Imported libaries such as numpy, scipy(read, write), matplotlib.pyplot
from scipy import signal
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[10]:


# Replace this with the location of your downloaded file.
(Frequency, array) = read('D:\\window\\user\\david\\Downloads\\eagle.wav') # Reading the sound file. 


# In[11]:


len(array) # length of our array


# In[12]:


plt.plot(array) 
plt.title('Original Signal Spectrum')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')


# In[13]:


FourierTransformation = sp.fft(array) # Calculating the fourier transformation of the signal


# In[14]:


scale = sp.linspace(0, Frequency, len(array))


# In[15]:


plt.stem(scale[0:5000], np.abs(FourierTransformation[0:5000]), 'r')  # The size of our diagram
plt.title('Signal spectrum after FFT')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')


# In[16]:


GuassianNoise = np.random.rand(len(FourierTransformation)) # Adding guassian Noise to the signal.


# In[17]:


NewSound = GuassianNoise + array


# In[18]:


write("New-Sound-Added-With-Guassian-Noise.wav", Frequency, NewSound) # Saving it to the file.


# In[19]:


b,a = signal.butter(5, 1000/(Frequency/2), btype='highpass') # ButterWorth filter 4350


# In[20]:


filteredSignal = signal.lfilter(b,a,NewSound)
plt.plot(filteredSignal) # plotting the signal.
plt.title('Highpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')


# In[21]:


c,d = signal.butter(5, 380/(Frequency/2), btype='lowpass') # ButterWorth low-filter
newFilteredSignal = signal.lfilter(c,d,filteredSignal) # Applying the filter to the signal
plt.plot(newFilteredSignal) # plotting the signal.
plt.title('Lowpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')


# In[22]:


write("New-Filtered-Eagle-Sound.wav", Frequency, newFilteredSignal) # Saving it to the file.

