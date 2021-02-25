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
    return render_template('index.html')

# section python
@app.route('/sections/python/')
def select_python():
    app.logger.info("choosing python section")
    data_learning.mycursor.execute(f"SELECT * FROM Python")
    result = data_learning.mycursor.fetchall()
    return render_template('test.html', result=result)

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
    return render_template('test.html', result=result)

#section add video
@app.route('/add/')
def add_page():
    return render_template('addPage.html')

app.route('/add/submit_video/')
def submit_video():
    app.logger.info("start insert of video in bdd")
    data_learning.mycursor.execute(f"SELECT * FROM Javascript")
    result = data_learning.mycursor.fetchall()
##########################################################

# endpoint + parameter Python
@app.route('/sections/python/watch/<id>')
def watch_python(id):
    app.logger.info("choosing video from python section")
    data_learning.mycursor.execute(f'SELECT * FROM Python WHERE ID={id}')
    result = data_learning.mycursor.fetchall()
    return render_template('watch.html', result=result)

# endpoint + parameter Cloud
@app.route('/sections/cloud/watch/<id>')
def watch_cloud(id):
    app.logger.info("choosing video from cloud section")
    data_learning.mycursor.execute(f'SELECT * FROM Cloud WHERE ID={id}')
    result = data_learning.mycursor.fetchall()
    img = '~/devCloud/dossier_git/E-learning/Python/static/img/cloud.jpg'
    return render_template('watch.html', result=result, img=img)

# endpoint + parameter Docker
@app.route('/sections/Docker/watch/<id>')
def watch_Docker(id):
    app.logger.info("choosing video from Docker section")
    data_learning.mycursor.execute(f'SELECT * FROM Docker WHERE ID={id}')
    result = data_learning.mycursor.fetchall()
    img = '~/devCloud/dossier_git/E-learning/Python/static/img/docker.png'
    return render_template('watch.html', result=result, img=img)

# endpoint + parameter JS
@app.route('/sections/js/watch/<id>')
def watch_js(id):
    app.logger.info("choosing video from js section")
    data_learning.mycursor.execute(f'SELECT * FROM Javascript WHERE ID={id}')
    result = data_learning.mycursor.fetchall()
    img = '~/devCloud/dossier_git/E-learning/Python/static/img/JS.jpg'
    return render_template('watch.html', result=result, img=img)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5200, debug=True)