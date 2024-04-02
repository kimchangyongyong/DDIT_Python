import mysql.connector

con = mysql.connector.connect(host='127.0.0.1',
                              port='3305', 
                              database='python',
                              user='root',
                              password='python')
cursor = con.cursor(dictionary=True) # True로 해야 row에서 column 이름으로 값을 불러올 수 있다.

sql="SELECT * FROM emp;"

cursor.execute(sql)

for row in cursor:
    print(str(row['e_id']),row['e_name'],row['gen'],row['addr'])

cursor.close()