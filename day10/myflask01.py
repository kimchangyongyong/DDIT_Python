from flask import Flask,redirect,jsonify
from flask.globals import request
from flask.templating import render_template
import pymysql
from day08 import daoemp
from day08.daoemp import DaoEmp
from day06.mysql_delete import e_id


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

@app.route('/emp_list',methods=['POST'])
def emp_list():
    de = DaoEmp()
    list=de.selectList()
    return jsonify(list=list)

@app.route('/emp_one',methods=['POST'])
def emp_one():
    data = request.get_json()
    e_id = data['e_id']
    
    de = DaoEmp()
    vo=de.select(e_id)
    return jsonify(vo=vo)

@app.route('/emp_add',methods=['POST'])
def emp_add():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    de = DaoEmp()
    cnt=de.insert(e_id, e_name, gen, addr)
    return jsonify(cnt=cnt)

@app.route('/emp_mod',methods=['POST'])
def emp_mod():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    de = DaoEmp()
    cnt=de.update(e_id, e_name, gen, addr)
    return jsonify(cnt=cnt)

@app.route('/emp_del',methods=['POST'])
def emp_del():
    data = request.get_json()
    e_id = data['e_id']

    de = DaoEmp()
    cnt=de.delete(e_id)
    return jsonify(cnt=cnt)
    
    
if __name__ == '__main__':
    app.run(debug=True)
