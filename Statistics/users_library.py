__author__ = 'danil.gizdatullin'

# I have some troubles with memory, and because of this I want to separate dictionary of users into some blocks
# and store it into files

import numpy as np
import itertools
from statistics import median
import json
from scipy import sparse


class UsersLibrary:
    def __init__(self, users_books_data="/Users/danil.gizdatullin/Projects/Recommendations/user_book.csv",
                 similarity_data="/Users/danil.gizdatullin/Projects/Recommendations/Similarity_data.csv"):
        self.users_books_data = users_books_data
        self.similarity_data = similarity_data
        self.user_ids = []
        self.library_structure = {}
        self.similarity_matrix = {}
        self.median_similarities = []
        self.size_of_similarity_matrix = 0

    def initialize_structure(self):
        data_file = open(self.users_books_data, 'r')
        next(data_file)
        users_library = {}
        for expression in data_file:
            data_line = expression[0:-1].split(',')
            user = int(data_line[0])
            book = int(data_line[1])
            if user in users_library:
                users_library[user].append(book)
            else:
                users_library[user] = [book]
        data_file.close()
        self.library_structure = users_library

    def initialize_similarity_matrix(self):
        similarity_matrix = {}
        data_file = open(self.similarity_data, 'r')
        next(data_file)
        for expression in data_file:
            data_line = expression[0:-1].split(',')
            book1 = int(data_line[0])
            book2 = int(data_line[1])
            sim = float(data_line[2])
            if book1 < book2:
                similarity_matrix[str(book1) + str(book2)] = sim
            else:
                similarity_matrix[str(book2) + str(book1)] = sim

        self.similarity_matrix = similarity_matrix

    def users_library_similarity_median(self, user_id):
        similarities = []
        books = self.library_structure[user_id]
        for pair in itertools.combinations(books, r=2):
            book1 = pair[0]
            book2 = pair[1]
            if book1 < book2:
                key = str(book1) + str(book2)
            else:
                key = str(book2) + str(book1)
            if key in self.similarity_matrix:
                sim = self.similarity_matrix[key]
                similarities.append(sim)

        if similarities:
            answer = median(similarities)
            del similarities
            return answer
        else:
            del similarities
            return -1

    def all_users_median_library_similarities(self, number_of_files=3):
        for i in xrange(number_of_files):
            with open("data" + str(i + 1) + ".json", "r") as fp:
                print("Stage %s"%(str(i)))
                data = json.load(fp)
                for user_id in data.iterkeys():
                    sim = self.users_library_similarity_median(data, user_id)
                    if sim != -1:
                        self.median_similarities.append(sim)

    # def all_users_median_library_similarities(self):
    #     median_similarities = []
    #     self.initialize_structure()
    #     self.initialize_similarity_matrix()
    #     # print len(self.library_structure.keys())
    #     # f = open("/Users/danil.gizdatullin/Projects/Recommendations/Median_similarity.csv", "w")
    #     for user_id in self.library_structure.keys():
    #         median_sim = self.users_library_similarity_median(user_id)
    #         if median_sim != -1:
    #             median_similarities.append(median_sim)
    #             # f.write(str(self.users_library_similarity_median(user_id)))
    #     # f.close()
    #             # np.append(median_similarities, self.users_library_similarity_median(user_id))
    #     return median_similarities

    # def all_users_median_library_similarities(self):
    #     median_similarities = {}
    #     self.initialize_structure()
    #     self.initialize_similarity_matrix()
    #     # print len(self.library_structure.keys())
    #     # f = open("/Users/danil.gizdatullin/Projects/Recommendations/Median_similarity.csv", "w")
    #     # for i in xrange(0, 214000, 2000):
    #     my_file = open("/Users/danil.gizdatullin/Projects/Recommendations/Median_similarity.csv", "a")
    #     # lower_bound = 0
    #     # upper_bound = 2000
    #     users_id = self.library_structure.keys()  # [lower_bound:upper_bound]
    #     for id in users_id:
    #         median_sim = self.users_library_similarity_median(id)
    #         print (id)
    #         if median_sim != -1:
    #             # median_similarities[id] = median_sim
    #             my_file.write(str(median_sim))
    #             my_file.write("\n")
    #     my_file.close()
    #
    #     return median_similarities

    def write_library_structure_into_files(self, number_of_files=3):
        if number_of_files > 0:
            number_of_files = int(number_of_files)
        else:
            number_of_files = 1
        user_ids = self.library_structure.keys()
        number_of_users = len(user_ids)
        len_of_file = int(round((number_of_users / float(number_of_files)) + 0.5))
        num_of_file = 1
        for i in xrange(0, number_of_users + 1, len_of_file):

            newdict = {user_id: self.library_structure[user_id] for user_id in user_ids[i: i + len_of_file]}
            with open("/Users/danil.gizdatullin/Projects/Recommendations/jsons/data" + str(num_of_file) + ".json", "w") as fp:
                json.dump(newdict, fp)
            num_of_file += 1
        self.library_structure = {}
