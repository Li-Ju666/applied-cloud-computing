import os
import json
import functools
from datetime import datetime as time

#read file
def read_json(path):
    data = []
    with open(path) as f:
        for count, line in enumerate(f.readlines(), start=1):
            if count%2==1:
                data.append(json.loads(line))

    return data

def get_texts(data):
    texts = []
    for record in data:
        texts.append(record.get('text').lower())
    return texts

def check_words(texts, dict):
    for record in texts:
        words = record.split()
        for word in words:
            if dict.get(word) != None:
                dict[word] += 1
    return dict

# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # Used for recursion
# # define foldr function
# def foldr(func, acc, xs):
#     return functools.reduce(lambda x, y: func(y, x), xs[::-1], acc)
#
# # Check if target pronouns exist and update dictionary
# def check(string, accdict):
#     words = string.split()
#     def check_word(word, dict):
#         if dict.get(word) != None:
#             dict[word] += 1
#         return dict
#     return foldr(check_word, accdict, words)

baseDir = "./data/"
files = os.listdir(baseDir)
files = map(lambda a: baseDir+a, files)

# base case
stats = {'han':0, 'hon':0, 'den':0, 'det':0, 'denna':0, 'denne':0, 'hen':0}
count = 0
time1 = time.now()

for file in files:
    print(file)
    data = read_json(file)
    count += len(data)
    # Recursion approach
    # texts = foldr(lambda a, acc: [a.get('text').lower()] + acc, [], data)
    # stats = foldr(check, stats, texts)
    texts = get_texts(data)
    stats = check_words(texts, stats)
    print(stats)
print("===========")
print(time.now()-time1)
print(count)
print(stats)

# Tweet data (count: 452723):
# 	Han: 183594
# 	Hon: 69878
# 	Den: 318783
# 	Det: 128571
# 	Denna: 4217
# 	Denne: 1436
# 	Hen: 25491

# {'han': 135600, 'hon': 45919, 'den': 245615, 'det': 95813, 'denna': 3891,
# 'denne': 1290, 'hen': 3574}

# loop: 0:00:33.309594
# Recursion: 0:00:41.141866