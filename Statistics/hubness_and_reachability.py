__author__ = 'danil.gizdatullin'

import config as conf
from k_nearest_neighbors import KNearestNeighbors

data_name = '/Users/danil.gizdatullin/Projects/Recommendations/Similarity_data.csv'
K_Nearest_Neighbors = KNearestNeighbors(file_name=conf.path_to_similarity_data)

print K_Nearest_Neighbors.statistics(conf.number_of_nearest_neighbors)
