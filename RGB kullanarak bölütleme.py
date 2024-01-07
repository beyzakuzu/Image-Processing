#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_segmentation(image_path, threshold_r, threshold_g, threshold_b):
    # Görüntüyü oku (renkli)
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Renk kanallarına ayrıl
    r_channel = image_rgb[:,:,0]
    g_channel = image_rgb[:,:,1]
    b_channel = image_rgb[:,:,2]
    
    # Eşik değerlerine göre bölütlenmiş görüntü oluştur
    segmented_image = np.zeros_like(image_rgb)
    segmented_image[(r_channel > threshold_r) & (g_channel > threshold_g) & (b_channel > threshold_b)] = [255, 255, 255]
    
    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Orijinal Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(segmented_image)
    plt.title('Bölütlenmiş Görüntü')
    plt.axis('off')
    
    plt.show()

# Örnek bir görüntü yolu veriniz
image_path = 'path/to/your/image.jpg'

# Eşik değerlerini belirleyerek bölütlenmiş görüntü oluştur
rgb_segmentation(image_path, threshold_r=100, threshold_g=120, threshold_b=80)

