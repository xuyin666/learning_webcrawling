import pymysql

db = pymysql.connect(host="localhost", user='xuyin', password='123456', port=3306, db='spiders')
cursor = db.cursor()

# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#     cursor.execute(sql, (25, 'Bob'))
#     db.commit()
# except:
#     db.rollback()
# db.close()

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}

# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))

# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, \
#         keys=keys, values=values)
# update = ','.join(["{key} = %s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()

# table = 'students'
# condition = 'age >= 20'

# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()

sql = 'SELECT * FROM students WHERE age >= 20'

# try:
#     cursor.execute(sql)
#     print('Count:', cursor.rowcount)
#     one = cursor.fetchone()
#     print('One:', one)
#     results = cursor.fetchall()
#     print('Results:', results)
#     print('Results Type:', type(results))
#     for row in results:
#         print(row)
# except:
#     print('Error')

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')