import json
from project.celery import app

# read a json file
def read_json(path):
    data = []
    with open(path) as f:
        for count, line in enumerate(f.readlines(), start=1):
            if count%2==1:
                data.append(json.loads(line))
    return data

# transform twitter dictionaries as a list of strings
def get_texts(data):
    texts = []
    for record in data:
        if record.get('retweeted_status') == None:
            texts.append(record.get('text').lower())
    return texts

# do statistics on the file
def check_words(texts, dict):
    for record in texts:
        words = record.split()
        for word in words:
            if dict.get(word) != None:
                dict[word] += 1
    return dict

@app.task
def analyze(path):
    stats = {'han':0, 'hon':0, 'den':0, 'det':0, 'denna':0, 'denne':0, 'hen':0}
    data = read_json(path)
    texts = get_texts(data)
    stats = check_words(texts, stats)
    return stats
