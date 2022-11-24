from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['https://elastic:is4LvwmBGm6L*_cmt+lS@localhost:9200'],
    verify_certs=False
)
# es.indices.create(index='news', ignore=400)
# result = es.indices.delete(index='news', ignore=[400, 404])
# print(result)

# data = {
#     'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
#     'url': 'http://view.inews.qq.com/a/EDU2021041600732200'
# }
# result = es.create(index='news', id=1, body=data)
# result = es.index(index='news', body=data)
# print(result)

# data = {
#     'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
#     'url': 'http://view.inews.qq.com/a/EDU2021041600732200',
#     'date': '2021-07-10'
# }
# result = es.update(index='news', body={"doc" : data}, id=1)
# print(result)

# result = es.index(index='news', body={"doc" : data}, id=1)

# result = es.delete(index='news', id=1)
# print(result)

# mapping = {
#     'properties': {
#         'title': {
#             'type': 'text',
#             'analyzer': 'ik_max_word',
#             'search_analyzer': 'ik_max_word'
#         }
#     }
# }

# es.indices.delete(index='news', ignore=[400, 404])
# es.indices.create(index='news', ignore=400)
# result = es.indices.put_mapping(index='news', body=mapping)
# print(result)

# datas =[
#     {
#         'title': '高考结局大不同',
#         'url': 'https://k.sina.com.cn/article_7571064628_1c34547340010111z9.html',
#     },
#     {
#         'title': '进入职业大洗牌时代，“吃香”职业还吃香吗?',
#         'url': 'https://new.qq.com/omn/20210828/202108284025LKOO.html',
#     },
#     {
#         'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
#         'url': 'http://view.inews.99.com/a/EDU2021041600732200',
#     },
#     {
#         'title':'他，活出了我理想的样子',
#         'url': 'https://new.qq.com/omn/20210821/20210821A020IDOO.html',
#     }
# ]

# for data in datas:
#     es.index(index='news', body=data)

# result = es.search(index='news')
# print(result)

# dsl = {
#     'query': {
#         'match': {
#             'title': '高考 圆梦'
#         }
#     }
# }

# result = es.search(index='news', body=dsl)
# print(result)