import pandas

df=pandas.read_csv("Day26/NATO-alphabet-start/Project26/nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for index,row in df.iterrows()}
# print(nato_dict)

user_word=input("Enter a word: ").upper()

user_list=[nato_dict[letter] for letter in user_word ]
print(user_list)


