import json
import difflib

with open('extracted_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
titles = []
description =[]
urls = []

for item in data:
    titles.append(item['title'])
    description.append((item["description"]))
    urls.append((item["parent_url"]))

def find_most_similar_title(input_title):

    similarity_ratio = [difflib.SequenceMatcher(None, input_title, title).ratio() for title in titles]
    max_index = similarity_ratio.index(max(similarity_ratio))
    response = [description[max_index], urls[max_index]]
    return response

