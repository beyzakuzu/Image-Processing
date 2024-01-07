#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching(image_path, min_out=0, max_out=255):
  
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  
    normalized_image = cv2.normalize(image, None, min_out, max_out, cv2.NORM_MINMAX)
    
   
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(normalized_image, cmap='gray')
    plt.title('Kontrast Genişletme Sonrası')
    plt.axis('off')
    
    plt.show()


image_path = 'path/to/your/image.jpg'

contrast_stretching(image_path)

