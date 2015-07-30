__author__ = 'danil.gizdatullin'

f = open("/Users/danil.gizdatullin/Projects/Recommendations/txts/median_similarities.txt", "r")
similarities = []
for line in f:
    value = float(line[0: -1])
    similarities.append(value)
