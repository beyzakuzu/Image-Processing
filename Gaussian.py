#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(image_path, kernel_size=3):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Gaussian filtre işlemi
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    
    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title(f'Gaussian Filtre (kernel_size={kernel_size})')
    plt.axis('off')
    
    plt.show()

# Örnek bir görüntü yolu veriniz
image_path = 'path/to/your/image.jpg'

# Gaussian filtre uygula (opsiyonel: kernel_size değeri ayarlanabilir)
gaussian_filter(image_path, kernel_size=5)

