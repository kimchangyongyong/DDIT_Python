from flask import Flask,redirect,jsonify
from flask.globals import request
from flask.templating import render_template
import pymysql
from day08 import daoemp
from day08.daoemp import DaoEmp
from day11.daomem import DaoMem


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('static/ajax.html')
       # return '<script>location.href="static/ajax.html"</script>'


@app.route('/ajax',methods=['POST'])
def ajax():
    data = request.get_json()
    print(data['menu'])
    return jsonify(result="success")

@app.route('/mem_list',methods=['POST'])
def emp_list():
    de = DaoMem()
    list=de.selectList()
    return jsonify(list=list)

@app.route('/mem_one',methods=['POST'])
def emp_one():
    data = request.get_json()
    mem_id = data['mem_id']
    
    de = DaoMem()
    vo=de.select(mem_id)
    return jsonify(vo=vo)

@app.route('/mem_add',methods=['POST'])
def emp_add():
    data = request.get_json()
    mem_id = data['mem_id']
    mem_name = data['mem_name']
    mobile = data['mobile']
    email = data['email']
    
    de = DaoMem()
    cnt=de.insert(mem_id, mem_name, mobile, email)
    return jsonify(cnt=cnt)

@app.route('/mem_mod',methods=['POST'])
def emp_mod():
    data = request.get_json()
    mem_id = data['mem_id']
    mem_name = data['mem_name']
    mobile = data['mobile']
    email = data['email']
    
    de = DaoMem()
    cnt=de.update(mem_id, mem_name, mobile, email)
    return jsonify(cnt=cnt)

@app.route('/mem_del',methods=['POST'])
def emp_del():
    data = request.get_json()
    mem_id = data['mem_id']

    de = DaoMem()
    cnt=de.delete(mem_id)
    return jsonify(cnt=cnt)
    
    
if __name__ == '__main__':
    app.run(debug=True)
