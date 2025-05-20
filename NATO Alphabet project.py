#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pnd
data = pnd.read_csv("/Users/abhisheksinha/PycharmProjects/Day 26/pythonProject/NATO-alphabet-start/nato_phonetic_alphabet.csv")
print(data.head())
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word:").upper()
print(user_input)
# lst = []
# for letter in user_input:
#     for (key, value) in data_dict.items():
#         if letter == key:
#             lst.append(value)
# print(lst)
lst = [data_dict[letter] for letter in user_input]
print(lst)

