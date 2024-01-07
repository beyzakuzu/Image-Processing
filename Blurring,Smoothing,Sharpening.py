#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Blurring Operation with Laplace (Bulanıklaştırma ile Laplace Operatörü):
python
Copy code
import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplacian_blurring(image_path, kernel_size=3):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Gaussian blurring işlemi
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    
    # Laplace operatörü uygula
    laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)
    
    # Görüntüleri görselleştir
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title('Bulanıklaştırılmış Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(laplacian, cmap='gray')
    plt.title('Laplace Operatörü Sonrası')
    plt.axis('off')
    
    plt.show()

# Örnek bir görüntü yolu veriniz
image_path = 'path/to/your/image.jpg'

# Laplace operatörü uygula (opsiyonel: kernel_size değeri ayarlanabilir)
laplacian_blurring(image_path, kernel_size=5)
2. Smoothing (Düzeltme) ile Sharpening (Keskinleştirme):
python
Copy code
import cv2
import numpy as np
import matplotlib.pyplot as plt

def smoothing_sharpening(image_path, alpha=1.5):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Smoothing (düzeltme) işlemi (örneğin, Gaussian blurring)
    smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Keskinleştirme işlemi
    sharpened_image = cv2.addWeighted(image, 1.0 + alpha, smoothed_image, -alpha, 0)
    
    # Görüntüleri görselleştir
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(smoothed_image, cmap='gray')
    plt.title('Düzeltme (Smoothing)')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(sharpened_image, cmap='gray')
    plt.title(f'Keskinleştirme (alpha={alpha})')
    plt.axis('off')
    
    plt.show()

# Örnek bir görüntü yolu veriniz
image_path = 'path/to/your/image.jpg'

# Keskinleştirme uygula (opsiyonel: alpha değeri ayarlanabilir)
smoothing_sharpening(image_path, alpha=1.5)

