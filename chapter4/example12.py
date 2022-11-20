import pymysql

db = pymysql.connect(host="localhost", user='xuyin', password='123456', port=3306, db='spiders')
cursor = db.cursor()
# data = {
#     'id': '2012001',
#     'name': 'Bob',
#     'age': 25
# }
# data = {
#     'id': '20120011',
#     'name': 'Mary',
#     'age': 21
# }
# data = {
#     'id': '20120012',
#     'name': 'Mike',
#     'age': 20
# }
data = {
    'id': '20120013',
    'name': 'James',
    'age': 22
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()