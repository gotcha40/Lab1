# TODO решите задачу
import json

filename = 'input.json'
with open(filename) as file:
    data = json.load(file)


def task(data_json) -> float:
    summ = 0
    for i in data_json:
        summ += float(i["weight"]) * float(i["score"])
    return summ


print(f'{task(data):.3f}')