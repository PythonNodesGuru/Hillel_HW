from adapter import AdapterEuroInUsa
from client import UsaSocket,UsaFork


# Вставляем американскую вилку в американскую розетку.
uf = UsaFork() 
us = UsaSocket(uf) 
us.connect() 
# >>> power on. Usa
# Вставляем евро-адаптер в американскую розетку. 
ad = AdapterEuroInUsa()
us = UsaSocket(ad)
us.connect() 