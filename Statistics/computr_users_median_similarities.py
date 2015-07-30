__author__ = 'danil.gizdatullin'

import users_library_similarity
import config as conf

similarity_data = conf.path_to_similarity_data
users_books_data = conf.path_to_users_library

a = users_library_similarity.UsersLibrary(users_books_data=users_books_data, similarity_data=similarity_data)

a.all_users_median_library_similarities(path_to_store_result=conf.path_to_store_median_similarities)
