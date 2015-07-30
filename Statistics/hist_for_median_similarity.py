__author__ = 'danil.gizdatullin'

import matplotlib.pyplot as plt

import config as conf

f = open(conf.path_to_store_median_similarities, "r")
similarities = []
for line in f:
    value = float(line[0: -1])
    similarities.append(value)

print(len(similarities))

bin1 = 0
bin2 = 0
for val in similarities:
    if val <= 0.4:
        bin1 += 1
    if val >= 0.8:
        bin2 += 1
print bin1
print bin2

plt.hist(similarities, bins=100)
plt.title("Similarities median")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
