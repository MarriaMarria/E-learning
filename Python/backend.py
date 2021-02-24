from flask import Flask, render_template, request, jsonify
from db_learning import MyDB
import logging
from logging import FileHandler

data_learning = MyDB()  # instance of the class
data_learning.mycursor  # to use mycursor we use the instance

app = Flask(__name__)

# setting logger
app.logger.setLevel("INFO")
for h in app.logger.handlers:
    app.logger.removeHandler(h)
handler = FileHandler("backend.log")
handler.setLevel("INFO")
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(threadName)s :: %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
print(app.logger.handlers)
logging.getLogger("werkzeug").addHandler(handler)
# logger set

# homepage
@app.route('/')
def greeting():
    app.logger.info("opening homepage")
    return "HOME PAGE"

# section python
@app.route('/sections/python/')
def select_python():
    app.logger.info("choosing python section")
    data_learning.mycursor.execute(f"SELECT * FROM Python")
    result = data_learning.mycursor.fetchall()
    return jsonify(result)

# section Cloud
@app.route('/sections/cloud/')
def select_cloud():
    app.logger.info("choosing cloud section")
    data_learning.mycursor.execute("SELECT * FROM Cloud")
    result = data_learning.mycursor.fetchall()
    return jsonify(result)

# section Docker
@app.route('/sections/docker/')
def select_docker():
    app.logger.info("choosing docker section")
    data_learning.mycursor.execute(f"SELECT * FROM Docker")
    result = data_learning.mycursor.fetchall()
    return jsonify(result)

#section js
@app.route('/sections/js/')
def select_js():
    app.logger.info("choosing js section")
    data_learning.mycursor.execute(f"SELECT * FROM Javascript")
    result = data_learning.mycursor.fetchall()
    return jsonify(result)

##########################################################

# endpoint + parameter Python
@app.route('/sections/python/watch/<id>')
def watch_python():
    app.logger.info("choosing video from python section")
    data_learning.mycursor.execute(f'SELECT {id} FROM Python')
    result = data_learning.mycursor.fetchall()
    return jsonify(result)

# endpoint + parameter Cloud
@app.route('/sections/cloud/watch/<id>')
def watch_cloud():
    app.logger.info("choosing video from cloud section")
    data_learning.mycursor.execute(f'SELECT {id} FROM Cloud')
    result = data_learning.mycursor.fetchall()
    return jsonify(result)

# endpoint + parameter Docker
@app.route('/sections/Docker/watch/<id>')
def watch_Docker():
    app.logger.info("choosing video from Docker section")
    data_learning.mycursor.execute(f'SELECT {id} FROM Docker')
    result = data_learning.mycursor.fetchall()
    return jsonify(result)

# endpoint + parameter JS
@app.route('/sections/js/watch/<id>')
def watch_js():
    app.logger.info("choosing video from js section")
    data_learning.mycursor.execute(f'SELECT {id} FROM Javascript')
    result = data_learning.mycursor.fetchall()
    return jsonify(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3051, debug=True)