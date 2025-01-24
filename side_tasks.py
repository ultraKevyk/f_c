import pickle
import os

data_dir = "./website/data/downloaded_data/"
data22_dir =  "./website/data/downloaded_data/2022/"


# from collections import OrderedDict
#
# # printing areas for label form
# new_name_dict = OrderedDict(sorted(name_dict.items(), key=lambda x: x[1]))
# for key in new_name_dict.items():
#     print(f'<option value="{key[0]}" class="dropdown-item">{key[1]}</option>')
#
# import unicodedata
#
# # printing fish for label form
# for fish in sorted(fish_list):
#     clear_fish = unicodedata.normalize('NFKD', fish).encode('ASCII', 'ignore').decode('utf-8')
#     print(f'<option value="{clear_fish}" class="dropdown-item">{fish}</option>')


# stare_reviry = ["431110", "431109", "431107","431105", "431076","04431123", "431099", "431021", "431111", "431114", "431117", "431108", "04431124", "431106", "431093", "431098", "05431125"] #na smazani
# for revir in stare_reviry:
#     for file in os.listdir(data_dir):
#         if revir in file:
#             print(file)


# new = {}
# counter = 0
# with open(data22_dir + "NAMES_NEW.pkl", 'rb') as g:
#     name_dict = pickle.load(g)
#     for key, value in name_dict.items():
#     #     value = value.upper()
#     #     if "VLTAVA" in value:
#     #         value = "VLTAVA - ÚDOLNÍ NÁDRŽ ORLÍK"
#     #     new[key] = value
#     # print(new)
#     # save_dictionary(new, "NAMES_NEW")

nove_reviry = ["05431138", "431141", "431142", "04431136"] # na pridani
stare_reviry = ["431110", "431109", "431107","431105", "431076","04431123", "431099", "431021", "431111", "431114", "431117", "431108", "04431124", "431106", "431093", "431098", "05431125"]


with open(data22_dir + "NAMES.pkl", 'rb') as g:
    name_dictionary = pickle.load(g)
    for revir in nove_reviry:
        print(revir)
        print(name_dictionary[revir])


