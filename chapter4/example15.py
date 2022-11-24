from redis import StrictRedis, ConnectionPool

# redis = StrictRedis(host='localhost', port=6379, db=0, password='pwd')
# redis.set('name', 'Bob')
# print(redis.get('name'))

# pool = ConnectionPool(host='localhost', port=6379, db=0, password='pwd')
# redis = StrictRedis(connection_pool=pool)
# redis.set('age', '10')
# print(redis.get('age'))

url = 'redis://:pwd@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)