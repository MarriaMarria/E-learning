from flask import Flask, render_template, request, jsonify, url_for, redirect
from db_learning import MyDB
import logging
from logging import FileHandler
from flask_mysql_connector import MySQL
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pw'
app.config['MYSQL_DB'] = 'scrap'

cur = MySQL(app)

@app.route('/add', methods=['POST', 'GET'])
def add_page():
    data_learning = cur.connection.cursor()
    if request.method == 'POST':
        name = request.form["name"]
        chaine = request.form["chaine"]
        categorie = request.form["menu"]
        description = request.form["description"]
        url = request.form["url"]
        val = [name, chaine, url, description]
        sql = f"INSERT INTO Python (name, chaine, url, description) VALUES ("
        for ii, i in enumerate(val):
            if ii == 3:
                sql = sql + "'" + i + "');"
            else:
                sql = sql + "'" + i + "', "
        data_learning.execute("use learning3;")
        data_learning.execute(sql)
        cur.connection.commit()
        data_learning.execute("SELECT MAX(id) from Python;")
        id = data_learning.fetchall()
        return jsonify(sql)
    else:
        return render_template('addPage.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5200, debug=True)