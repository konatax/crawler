import pymysql

conn = pymysql.connect(
        host='112.74.41.22',
        user='root',
        password='123456',
        database='mytest'
    )
cursor = conn.cursor()