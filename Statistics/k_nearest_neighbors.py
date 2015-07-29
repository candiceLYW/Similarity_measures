__author__ = 'danil.gizdatullin'
import numpy as np
from scipy.stats import skew


def add_new_neighbor(old_neighbors={}, new_obj={}, number_of_neighbors=5):
    book2 = new_obj['obj']
    similarity = new_obj['similarity']
    if len(old_neighbors) < number_of_neighbors:
        old_neighbors[book2] = similarity
    else:
        key_of_min = min(old_neighbors, key=old_neighbors.get)
        min_val = old_neighbors[key_of_min]
        if similarity > min_val:
            del old_neighbors[key_of_min]
            old_neighbors[book2] = similarity

    return old_neighbors


class KNearestNeighbors:
    def __init__(self, file_name='/Users/danil.gizdatullin/Projects/Recommendations/Similarity_data.csv'):
        self.file_name = file_name
        self.structure = {}
        self.book_times = {}

    def k_nearest_neighbors(self, k=5):
        k_nearest_dic = {}
        data_file = open(self.file_name, 'r')
        next(data_file)
        for expression in data_file:
            data_line = expression[0:-1].split(',')
            book1 = int(data_line[0])
            book2 = int(data_line[1])
            similarity = float(data_line[2])

            if not(book1 in k_nearest_dic):
                k_nearest_dic[book1] = {book2: similarity}
            else:
                k_nearest_dic[book1] = add_new_neighbor(k_nearest_dic[book1],
                                                        new_obj={'obj': book2, 'similarity': similarity},
                                                        number_of_neighbors=k)

            if not(book2 in k_nearest_dic):
                k_nearest_dic[book2] = {book1: similarity}
            else:
                k_nearest_dic[book2] = add_new_neighbor(k_nearest_dic[book2],
                                                        new_obj={'obj': book1, 'similarity': similarity},
                                                        number_of_neighbors=k)
        self.structure = k_nearest_dic

    def how_many_times_in_nearest(self):
        book_nearest_times = {}
        for book in self.structure.keys():
            book_nearest_times[book] = 0
        for books in self.structure.values():
            for book in books.keys():
                book_nearest_times[book] += 1

        self.book_times = book_nearest_times

    def statistics(self, number_of_nearest_neighbors=5):
        stat_dict = {}
        self.k_nearest_neighbors(k=number_of_nearest_neighbors)
        self.how_many_times_in_nearest()
        times_values = self.book_times.values()
        stat_dict["Hubness"] = skew(times_values)

        times_values_arr = np.array(times_values)
        times_values_arr_non_zero = times_values_arr[np.nonzero(times_values_arr)]
        stat_dict["Reachability"] = len(times_values_arr_non_zero) / float(len(times_values_arr))

        return stat_dict
