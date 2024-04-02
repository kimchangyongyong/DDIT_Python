import pymysql

class DaoMem:
    
    def __init__(self):
        self.con = pymysql.connect(
            host='localhost',
            port=3305,
            database='python',
            user='root',
            password='python',
            charset='utf8'
        )
        self.cursor = self.con.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = "SELECT * FROM mem;"
        self.cursor.execute(sql)

        result_list = self.cursor.fetchall()
        return result_list

    def select(self, mem_id):
        
        sql = f"""SELECT * FROM mem WHERE mem_ID='{mem_id}';"""
        self.cursor.execute(sql)
        
        vo=self.cursor.fetchone()
        return vo
    
    def insert(self, mem_id, mem_name, mobile, email):
    
        sql = f"""
              insert into mem
              (mem_id, mem_name, mobile, email)
              values
              ('{mem_id}','{mem_name}','{mobile}','{email}');
              """
        cnt = self.cursor.execute(sql)
    
        self.con.commit()
        return cnt
    
    def update(self, mem_id, mem_name, mobile, email):
        
        sql = f"""
            update mem set mem_id='{mem_id}', mem_name='{mem_name}', 
            mobile='{mobile}', email='{email}'
            where mem_id = '{mem_id}';
             """   
        cnt = self.cursor.execute(sql)
    
        self.con.commit()
        
        return cnt
    
    def delete(self,mem_id):
        sql=f"""
            delete from mem
            where
            mem_id='{mem_id}'
            """
        cnt = self.cursor.execute(sql)
        self.con.commit()
        return cnt
    
    
    
    def __del__(self):
        self.cursor.close()
        self.con.close()

if __name__ == '__main__':
    de = DaoMem()
    
    cnt=de.delete('6')
    print(cnt)
    
    
