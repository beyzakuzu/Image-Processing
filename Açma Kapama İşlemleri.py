#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import matplotlib.pyplot as plt

# Görüntüyü açma
image_path = 'path/to/your/image.jpg'
image = cv2.imread(image_path)

# Görüntüyü ekrana yazdırma
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Orijinal Görüntü')
plt.axis('off')
plt.show()

# Görüntüyü kapama (kapatma)
cv2.destroyAllWindows()

