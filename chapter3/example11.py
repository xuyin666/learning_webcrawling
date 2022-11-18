# 父节点和祖先节点
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were 
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#         </p>
#         <p class="story">...</p>
# """

html = """
<html>
    <body>
        <p class="story">
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.a.parent)

print(type(soup.a.parents))
# print(list(enumerate(soup.a.parents)))
# for parent in soup.a.parents:
#     print(parent.name)
# p
# body
# html
# [document]