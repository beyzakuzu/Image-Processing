#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slicing(image_path):
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    rows, cols = image.shape
    
    masks = [1, 2, 4, 8, 16, 32, 64, 128]
  
    plt.figure(figsize=(15, 10))
    plt.gray()
    
    for i, mask in enumerate(masks, 1):
        
        bit_plane = np.bitwise_and(image, mask)
        
       
        plt.subplot(2, 4, i)
        plt.imshow(bit_plane)
        plt.title(f'Bit Plane {i}')
        plt.axis('off')
    
    plt.show()


image_path = 'path/to/your/image.jpg'


bit_plane_slicing(image_path)

