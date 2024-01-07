#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Normalizasyon İle Standardizasyon Arasındaki Farklar
## Veri madenciliği ve makine öğrenimi projelerinde, veri ön işleme adımı önemlidir. Bu adımda, veri setindeki özelliklerin ölçeklendirilmesi genellikle gereklidir. Normalizasyon ve standardizasyon, özellik değerlerini birbirlerine göre uygun bir şekilde ölçeklendirmek için kullanılan iki yaygın tekniktir.Normalizasyon
## Normalizasyon, özellik değerlerini belirli bir aralığa ölçeklendirir. Genellikle, [0, 1] aralığında ölçeklendirme kullanılır. Bu işlem, özelliklerin orijinal dağılımını korurken, değerleri belirli bir aralığa sıkıştırır.

## Örnek olarak, MinMaxScaler sınıfını kullanarak normalizasyon yapabiliriz:


# In[3]:


from sklearn.preprocessing import MinMaxScaler

veri = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

normalizer = MinMaxScaler()
normalized_data = normalizer.fit_transform(veri)


# In[13]:



#Standardizasyon, özellik değerlerini bir standart normal dağılıma dönüştürür. Bu, özelliklerin ortalamasını 0 ve standart sapmasını 1 yapar. Bu yöntem, veri setindeki anormalliklere daha az duyarlı olabilir.
#Örnek olarak, StandardScaler sınıfını kullanarak standardizasyon yapabiliriz:




# In[14]:


from sklearn.preprocessing import StandardScaler

veri = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

standardizer = StandardScaler()
standardized_data = standardizer.fit_transform(veri)


# In[ ]:




