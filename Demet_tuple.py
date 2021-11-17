Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: D:/Artificial Intelligence/OpenCV A-Z™  Uygulamalarla Görüntü İşleme  2021  23 Saat/Starting Code/def2.py
Tur:  cizgili baykus
Ortalama Agırlıgı:  720
Beslenme Turu:  Etcil
Kanat Acıklıgı:  112
>>> tupl = (1,2,3,4)
>>> print(tupl)
(1, 2, 3, 4)
>>> demet=(1,2,3,4,"oguz","18")
>>> print(demet)
(1, 2, 3, 4, 'oguz', '18')
>>> demet=(1,2,3,4,"ahmet","20",)
>>> print(demet)
(1, 2, 3, 4, 'ahmet', '20')
>>> demet[2]
3
>>> demet[3]="123"
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    demet[3]="123"
TypeError: 'tuple' object does not support item assignment
>>> ikinciDemet=()
>>> print(ikinciDemet)
()
>>> demet=("betik","ahmet","25")
>>> print(demet)
('betik', 'ahmet', '25')
>>> birDemet=("okul","drone","yazılım")
>>> x = demet + birDemet
>>> print(x)
('betik', 'ahmet', '25', 'okul', 'drone', 'yazılım')
>>> x
('betik', 'ahmet', '25', 'okul', 'drone', 'yazılım')
>>> 