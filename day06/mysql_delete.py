import pymysql
from mysql.connector import cursor

conn = pymysql.connect(host='localhost',
                              port=3305, 
                              database='python',
                              user='root',
                              password='python',
                              charset='utf8')

curs = conn.cursor()
e_id="6"
e_name = "7"
gen = "7"
addr = "7"

sql = f"""
    update emp set
    e_name='{e_name}',gen='{gen}',addr='{addr}'
    where e_id = '{e_id}';
    """
    
    
cnt=curs.execute(sql)
print(cnt)

#print(curs.rowcount)

conn.commit()

curs.close()
conn.close()
