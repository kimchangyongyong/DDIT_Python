import pymysql
from mysql.connector import cursor

conn = pymysql.connect(host='localhost',
                              port=3305, 
                              database='python',
                              user='root',
                              password='python',
                              charset='utf8')

curs = conn.cursor()
e_id = "6"
e_name = "6"
gen = "6"
addr = "6"

sql = f"""
    insert into emp
    (e_id, e_name, gen, addr)
    values
    ('{e_id}','{e_name}','{gen}','{addr}');
    """
    
    
cnt=curs.execute(sql)
print(cnt)

#print(curs.rowcount)

conn.commit()

curs.close()
conn.close()