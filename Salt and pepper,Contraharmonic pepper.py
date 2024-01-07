#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.size

    # Add salt noise
    num_salt = np.ceil(salt_prob * total_pixels)
    salt_coordinates = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[salt_coordinates[0], salt_coordinates[1]] = 255

    # Add pepper noise
    num_pepper = np.ceil(pepper_prob * total_pixels)
    pepper_coordinates = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[pepper_coordinates[0], pepper_coordinates[1]] = 0

    return noisy_image

def contraharmonic_mean_filter(image, kernel_size, Q):
    padded_image = cv2.copyMakeBorder(image, kernel_size // 2, kernel_size // 2, kernel_size // 2, kernel_size // 2, cv2.BORDER_CONSTANT)

    result = np.zeros_like(image, dtype=np.float32)

    for i in range(kernel_size // 2, padded_image.shape[0] - kernel_size // 2):
        for j in range(kernel_size // 2, padded_image.shape[1] - kernel_size // 2):
            neighborhood = padded_image[i - kernel_size // 2:i + kernel_size // 2 + 1, j - kernel_size // 2:j + kernel_size // 2 + 1]
            numerator = np.sum(neighborhood ** (Q + 1))
            denominator = np.sum(neighborhood ** Q)
            result[i - kernel_size // 2, j - kernel_size // 2] = numerator / max(1, denominator)

    result = np.clip(result, 0, 255)
    result = np.uint8(result)

    return result

# Örnek olarak bir resim yükleyelim
image = cv2.imread('your_image_path.jpg', cv2.IMREAD_GRAYSCALE)

# Salt and pepper gürültüsü ekleme
salt_prob = 0.02  # Salt gürültüsü olasılığı
pepper_prob = 0.02  # Pepper gürültüsü olasılığı
noisy_image = add_salt_and_pepper_noise(image, salt_prob, pepper_prob)

# Contraharmonic Mean filtresini uygulama
kernel_size = 3  # Filtre boyutu
Q = 1.5  # Q değeri
filtered_image = contraharmonic_mean_filter(noisy_image, kernel_size, Q)

# Sonuçları gösterme
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

