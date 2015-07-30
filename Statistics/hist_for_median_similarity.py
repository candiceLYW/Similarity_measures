__author__ = 'danil.gizdatullin'

import matplotlib.pyplot as plt

import config as conf

f = open(conf.path_to_store_median_similarities, "r")
similarities = []
for line in f:
    value = float(line[0: -1])
    similarities.append(value)

print(len(similarities))

plt.hist(similarities, bins=100)
plt.title("Similarities median")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
