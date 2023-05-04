
import pandas as pd
import random
# data = pd.read_csv("./data/french_words.csv")
# df = pd.DataFrame(data)

# dict = {row.French: row.English   for (index, row) in df.iterrows() }

# # print(dict)

# french_list = list(df["French"])

# # print(df.to_dict())
# # print(random.choice(french_list))


# D = {1:'zara',2:'jim',3:"tom"}

# print (D)

# D.pop(2)

# print (D)

# D.to_csv("test.csv")


data = pd.read_csv("./data/french_words.csv")
df = pd.DataFrame(data)
df.to_csv("./data/words_to_learn.csv", index = False)
french_list = list(df["French"])
dict = {row.French: row.English   for (index, row) in df.iterrows() }
dict_to_learn = dict

#print(dict_to_learn)
dict_to_learn.pop("partie")
#print(dict_to_learn)

word_to_learn = pd.DataFrame(dict_to_learn.items(), columns = ['French','English'])
print(word_to_learn)
word_to_learn.to_csv ("./data/words_to_learn.csv", index = None)