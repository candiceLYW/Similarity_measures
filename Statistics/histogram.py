__author__ = 'danil.gizdatullin'
import matplotlib.pyplot as plt
import numpy as np

name_of_file = '/Users/danil.gizdatullin/Projects/Recommendations/Similarity_data.csv'
f = open(name_of_file, 'r')
next(f)
similarity_values = []
checker = 0
book_times_in_neighbors = {}
for line in f:
    items = line[0:-1].split(',')
    book1 = int(items[0])
    book2 = int(items[1])
    if not(book1 in book_times_in_neighbors):
        book_times_in_neighbors[book1] = 0
    if not(book2 in book_times_in_neighbors):
        book_times_in_neighbors[book2] = 0
    # similarity_values.append(float(items[2]))
    checker += 1
print(checker)
similarity_values_arr = np.array(similarity_values)

plt.hist(similarity_values_arr, bins=200)
plt.title("Similarity")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
