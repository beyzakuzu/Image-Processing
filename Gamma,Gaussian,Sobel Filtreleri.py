#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Gamma Düzeltme (Gamma Correction):


import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image_path, gamma=1.0):
    # Görüntüyü oku
    image = cv2.imread(image_path)
    
    # Gamma düzeltme işlemi
    corrected_image = np.power(image / 255.0, gamma)
    corrected_image = (corrected_image * 255).astype(np.uint8)
    
    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(corrected_image, cv2.COLOR_BGR2RGB))
    plt.title(f'Gamma Düzeltme (gamma={gamma})')
    plt.axis('off')
    
    plt.show()

# Örnek bir görüntü yolu veriniz
image_path = 'path/to/your/image.jpg'

# Gamma düzeltme uygula (opsiyonel: gamma değeri ayarlanabilir)
gamma_correction(image_path, gamma=1.5)
2. Ortalama Filtre (Average Filter):
python
Copy code
import cv2
import numpy as np
import matplotlib.pyplot as plt

def average_filter(image_path, kernel_size=3):
    # Görüntüyü oku
    image = cv2.imread(image_path)
    
    # Ortalama filtre işlemi
    blurred_image = cv2.blur(image, (kernel_size, kernel_size))
    
    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    plt.title(f'Ortalama Filtre (kernel_size={kernel_size})')
    plt.axis('off')
    
    plt.show()

# Örnek bir görüntü yolu veriniz
image_path = 'path/to/your/image.jpg'

# Ortalama filtre uygula (opsiyonel: kernel_size değeri ayarlanabilir)
average_filter(image_path, kernel_size=5)
3. Gaussian Filtre:
python
Copy code
import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(image_path, kernel_size=3):
    # Görüntüyü oku
    image = cv2.imread(image_path)
    
    # Gaussian filtre işlemi
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    
    # Görüntüleri görselleştir
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    plt.title(f'Gaussian Filtre (kernel_size={kernel_size})')
    plt.axis('off')
    
    plt.show()

# Örnek bir görüntü yolu veriniz
image_path = 'path/to/your/image.jpg'

# Gaussian filtre uygula (opsiyonel: kernel_size değeri ayarlanabilir)
gaussian_filter(image_path, kernel_size=5)
4. Sobel Filtresi:
python
Copy code
import cv2
import numpy as np
import matplotlib.pyplot as plt

def sobel_filter(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Sobel filtre işlemi
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Görüntüleri görselleştir
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(sobel_x, cmap='gray')
    plt.title('Sobel X Filtresi')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(sobel_y, cmap='gray')
    plt.title('Sobel Y Filtresi')
    plt.axis('off')
    
    plt.show()

# Örnek bir görüntü yolu veriniz
image_path = 'path/to/your/image.jpg'

# Sobel filtresi uygula
sobel_filter(image_path)

