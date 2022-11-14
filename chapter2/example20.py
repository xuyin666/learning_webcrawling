# robotparser

from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

# rp = RobotFileParser()
# rp.set_url('https://www.baidu.com/robots.txt')
# rp = RobotFileParser('https://www.baidu.com/robots.txt')

# rp.read()
# print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
# print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
# print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))


rp = RobotFileParser()
rp.parse(urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))