# import csv

# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)

import pandas as pd

df = pd.read_csv('data.csv')
# print(df)

# data = df.values.tolist()
# # print(df.values)
# print(data)

for index, row in df.iterrows():
    print(index, row.tolist())