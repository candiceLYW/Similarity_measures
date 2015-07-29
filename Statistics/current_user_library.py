__author__ = 'danil.gizdatullin'
from k_nearest_neighbors import KNearestNeighbors

data_name = '/Users/danil.gizdatullin/Projects/Recommendations/Similarity_data.csv'
K_Nearest_Neighbors = KNearestNeighbors(file_name=data_name)

print K_Nearest_Neighbors.statistics(20)
