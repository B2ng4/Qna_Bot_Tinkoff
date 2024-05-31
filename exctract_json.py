import json
import difflib

with open('extracted_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
titles = []
description =[]


for item in data:
    titles.append(item['title'])
    description.append((item["description"]))

def find_most_similar_title(input_title, titles):

    similarity_ratio = [difflib.SequenceMatcher(None, input_title, title).ratio() for title in titles]
    max_index = similarity_ratio.index(max(similarity_ratio))
    response = [titles[max_index],description[max_index]]
    return response


quest = "Я ошибся при отправке денег. Могу отменить платеж?"

print(find_most_similar_title(quest,titles))