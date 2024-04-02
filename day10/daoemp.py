import pymysql

class DaoEmp:
    
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
        sql = "SELECT * FROM emp;"
        self.cursor.execute(sql)

        result_list = self.cursor.fetchall()
        return result_list

    def select(self, e_id):
        
        sql = f"""SELECT * FROM EMP WHERE E_ID='{e_id}';"""
        self.cursor.execute(sql)
        
        vo=self.cursor.fetchone()
        return vo
    
    def insert(self, e_id, e_name, gen, addr):
    
        sql = f"""
              insert into emp
              (e_id, e_name, gen, addr)
              values
              ('{e_id}','{e_name}','{gen}','{addr}');
              """
        cnt = self.cursor.execute(sql)
    
        self.con.commit()
        return cnt
    
    def update(self, e_id, e_name, gen, addr):
        
        sql = f"""
            update emp set e_id='{e_id}', e_name='{e_name}', 
            gen='{gen}', addr='{addr}'
            where e_id = '{e_id}';
             """   
        cnt = self.cursor.execute(sql)
    
        self.con.commit()
        
        return cnt
    
    def delete(self,e_id):
        sql=f"""
            delete from emp
            where
            e_id='{e_id}'
            """
        cnt = self.cursor.execute(sql)
        self.con.commit()
        return cnt
    
    
    
    def __del__(self):
        self.cursor.close()
        self.con.close()

if __name__ == '__main__':
    de = DaoEmp()
    
    cnt=de.delete('6')
    print(cnt)
    
    
