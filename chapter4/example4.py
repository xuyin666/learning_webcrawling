import json

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]


# with open('data1.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(data))

with open('data1.json', 'w') as file:
    file.write(json.dumps(data, indent=2))