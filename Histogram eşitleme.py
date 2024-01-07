#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Histogram eşitleme işlemi
    equalized_image = cv2.equalizeHist(image)

    # Görüntüleri gösterme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')

    plt.show()

    return equalized_image

# Örnek olarak bir resim yolu belirtelim
image_path = 'your_image_path.jpg'

# Histogram eşitleme işlemini uygula
equalized_image = histogram_equalization(image_path)

