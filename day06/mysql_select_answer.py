import pymysql

conn = pymysql.connect(host='localhost',
                              port=3305, 
                              database='python',
                              user='root',
                              password='python',
                              charset='utf8')

curs = conn.cursor() 

sql="SELECT * FROM emp;"
curs.execute(sql)

rows = curs.fetchall()
print(rows)

curs.close()
conn.close()