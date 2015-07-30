__author__ = 'danil.gizdatullin'

import itertools
import json
from statistics import median

import config as conf


class UsersLibrary:
    def __init__(self, users_books_data=conf.path_to_users_library, similarity_data=conf.path_to_similarity_data):
        self.users_books_data = users_books_data
        self.similarity_data = similarity_data
        self.library_structure = {}
        self.similarity_matrix = {}

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
            return answer
        else:
            return -1

    def all_users_median_library_similarities(self, path_to_store_result=conf.path_to_store_median_similarities):

        self.initialize_similarity_matrix()
        self.initialize_structure()

        # clear file to store computed median similarity
        open(path_to_store_result, 'w').close()

        f = open(path_to_store_result, "a")
        for user_id in self.library_structure.iterkeys():
            sim = self.users_library_similarity_median(user_id)
            if sim != -1:
                f.write(str(sim)+"\n")
        f.close()
