# import os
#
# # if(not os.path.exists("data")):
# #     os.mkdir("data")
#
# # for i in range(0, 20):
# #     os.mkdir(f"data/Day{i+1}")
#
# # for i in range(0, 20):
# #     # os.rename(f"data/Day{i+1}", f"data/Tut{i+1}")
# #     os.rename(f"data/Tut{i+1}", f"data/Tut {i+1}")
#
#
# # os.getcwd()
# # os.listdir(data)
#
# # folders = os.listdir("data")
# # print(folders)
# #
# # for folder in folders:
# #     print(folder)
# #     print(os.listdir(f"data/{folder}"))
#
# # print(os.getcwd())
# # os.chdir("/home")
# # print(os.getcwd())
#
# # Reverse string
# # str= "vertex"[::-1]
# # print(str)
#
# # remove list duplicate??
#
# # lst = ["a", "b", "c", "c", "a", "b", "C"]
# # print(lst)
# # lst = list(dict.fromkeys(lst))
# # print(lst)
#
# # using function def
#
# # def remove_list_duplicate(lst1):
# #     return list(dict.fromkeys(lst1))
# #
# # print(remove_list_duplicate(lst1=["a", "b", "c", "c", "a", "b", "C"]))
# #
#
# # animals =['lion', 'tiger',  'monkey', 'elephant', 'frog']
# # filtered_animals = [ animals.title() for animal in animals ]
# # print(filtered_animals)
# # # filtered_animals = ['Lion', 'Tiger', 'Monkey', 'Elephant', 'Frog']
#
# # print("nepal match in usa but will nepal win?")
# # a = input("Enter value\n")
# # b = 1
# # print("This is introduction", a, b)
# # print("This is introduction", a + str(b))
#
# # name = 'MohitShrestha'
# # for i in name:
# #     print(i, end=", ")
#
#
# # lst = [3, 5, 6]
# # print(lst)
# # print(type(lst))
# # print(lst[1])
#
# # lst = [2, 5, 3, 6, 8, 7, 3, 6, 1, 7]
#
# # def find_all_indices(lst, element):
# #     indices = []
# #     for i in range(len(lst)):
# #         if lst[i] == element:
# #             indices.append(i)
# #     return indices
# #
# # lst = [1, 2, 3, 4, 5, 3, 6, 3]
# # element = 3
# # print(find_all_indices(lst, element))
#
# # tup = ("nepal", "india", "china", "thailand", "china", "japan", "bhutan")
# # newtup = list(tup)
# # newtup.append("srilanka")
# # print(newtup)
# # newtup.remove("thailand")
# # print(newtup)
# # newtup.pop(4)
# # x = newtup.count("china")
# # print(x)
# # newtup[2] = "USA"
# # tup = tuple(newtup)
# # print(tup)
#
# # print(tuple(newtup))
# # print(newtup)
#
# #old technique for format string
# # txt = f"My name is Mohit and I'm {} years old having height {}"
# # age = 24
# # height = 5.7
# # print(txt.format(age, height)
#
# tryset = {"hello", 8, True, "stha", False, 7}
# print(tryset)
# print(type(tryset))
#
from tsting import person_detail

person_detail()