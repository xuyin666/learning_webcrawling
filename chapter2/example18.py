# parse_qs translate query to dict
# from urllib.parse import parse_qs

# query = 'name=germey&age=25'
# print(parse_qs(query))

# parse_qsl translate query to tuple
from urllib.parse import parse_qsl
query = 'name=germey&age=25'
print(parse_qsl(query))
print(parse_qsl(query)[0][0])
