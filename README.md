# Similarity_measures

Проект нужен для подсчета различных Hubness, Reachability и медианы для показателя сходства книг внутри библиотеки каждого пользователя по данным о сходстве книг между собой и данным о библиотеках пользователей.  
  
В папке Data_Extraction лежат sql скрипты для извлечения данных о пользователях и сходстве книг.  
  
Полученные результаты нужно сохранить в .csv файлы в директории, которые затем нужно указать в файле config.py в папке Statistics.  
  
Также в файле config.py нужно указать файл для записи значений медианы похожести книг для каждого пользователя, и кол-во ближайших соседей которое мы хотим рассматривать при нахождении k ближайших соседей для конкретной книги.  
  
