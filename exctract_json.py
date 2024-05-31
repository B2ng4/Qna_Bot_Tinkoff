import json
import difflib

with open('extracted_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
titles = []

for item in data:
    titles.append(item['title'])

def find_most_similar_title(input_title, titles):

    similarity_ratio = [difflib.SequenceMatcher(None, input_title, title).ratio() for title in titles]
    max_index = similarity_ratio.index(max(similarity_ratio))
    return titles[max_index]
