__author__ = 'danil.gizdatullin'

users_books_data = "/Users/danil.gizdatullin/Projects/Recommendations/user_book.csv"
import users_library
import json

similarity_data = "/Users/danil.gizdatullin/Projects/Recommendations/Similarity_data.csv"

a = users_library.UsersLibrary(users_books_data="/Users/danil.gizdatullin/Projects/Recommendations/user_book.csv",
                               similarity_data="/Users/danil.gizdatullin/Projects/Recommendations/Similarity_data.csv")
a.initialize_similarity_matrix()
# a.initialize_structure()
# a.write_library_structure_into_files(1000)
# a.all_users_median_library_similarities(7)
# print(len(a.median_similarities))


# f = open("/Users/danil.gizdatullin/Projects/Recommendations/txts/median_similarities1.txt", "a")
# with open("/Users/danil.gizdatullin/Projects/Recommendations/jsons/data1.json", "r") as fp:
#     data = json.load(fp)
#     for user_id in data.iterkeys():
#         print(user_id)
#         sim = a.users_library_similarity_median(data, user_id)
#         if sim != -1:
#             f.write(str(sim))
#             f.write("\n")
# f.close()

for i in xrange(1, 1001):
    f = open("/Users/danil.gizdatullin/Projects/Recommendations/txts/median_similarities" + str(i) + ".txt", "w")
    fp = open("/Users/danil.gizdatullin/Projects/Recommendations/jsons/data" + str(i) + ".json", "r")
    data = json.load(fp)
    keys = data.iterkeys()
    for user_id in keys:
        # print(user_id)
        sim = a.users_library_similarity_median(data, user_id)
        if sim != -1:
            f.write(str(sim))
            f.write("\n")
    print (i)
    f.close()
    fp.close()
    del data
    del sim
    del f
    del fp
    del keys


# aa = a.all_users_median_library_similarities()
# the last user_id is 29760
# number of users 2158370
# max length of similarity 4573
# max length for file 4446
#############################################
# a.initialize_similarity_matrix()
# a.initialize_structure()
# similarity = []
# step = 10
# for i in xrange(7190, 2154370, step):
#     print(i)
#     my_file = open("/Users/danil.gizdatullin/Projects/Recommendations/Median_similarity.csv", "a")
#     for id in a.library_structure.keys()[i:(i + step)]:
#         median_sim = a.users_library_similarity_median(id)
#         my_file.write(str(median_sim))
#         my_file.write("\n")
#     my_file.close()
#############################################
# my_file = open("/Users/danil.gizdatullin/Projects/Recommendations/Median_similarity.csv", "a")
#
# for id in a.library_structure.iterkeys():
#     median_sim = a.users_library_similarity_median(id)
#     my_file.write(str(median_sim))
#     my_file.write("\n")
# my_file.close()
