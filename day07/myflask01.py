from flask import Flask
from flask.globals import request
from flask.templating import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, ChangYong!'


@app.route('/param')
def param():
    param = request.args.get('menu')
    return 'Param : ' + param


@app.route('/post', methods=['POST'])
def post():
    menu = request.form.get('menu')
    return 'Post : ' + menu


@app.route('/forw')
def forw():
    a = "홍길동"
    b = ["전우치", "일지매"]
    c = [
      {'e_id': 1, 'e_name':1, 'gen':1, 'addr':1},
      {'e_id': 2, 'e_name':2, 'gen':2, 'addr':2},
      {'e_id': 3, 'e_name':3, 'gen':3, 'addr':3}
      ]
    return 'FORW' + render_template("forw.html", a=a, b=b, c=c)


from flask import Flask, render_template
import mysql.connector


@app.route('/emp')
def emp():
    con = mysql.connector.connect(host='127.0.0.1',
                                  port='3305',
                                  database='python',
                                  user='root',
                                  password='python')
    cursor = con.cursor(dictionary=True)

    sql = "SELECT * FROM emp;"
    cursor.execute(sql)

    emps = cursor.fetchall()

    cursor.close()
    con.close()

    return render_template("emp.html", emps=emps)


if __name__ == '__main__':
    app.run(debug=True)
