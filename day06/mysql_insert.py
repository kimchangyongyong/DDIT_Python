import pymysql

conn = pymysql.connect(host='localhost',
                              port=3305, 
                              database='python',
                              user='root',
                              password='python',
                              charset='utf8')

curs = conn.cursor()

sql = "insert into emp(e_id, e_name, gen, addr) values('4','4','4','4');"
    
    
curs.execute(sql)
conn.commit()

curs.close()
conn.close()