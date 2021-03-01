from flask import Flask, render_template, request, jsonify, url_for, redirect
from db_learning import MyDB
import logging
from logging import FileHandler
from flask_mysql_connector import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'ms2'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'learning3'

cur = MySQL(app)

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
    data_learning = cur.connection.cursor()
    app.logger.info("choosing python section")
    data_learning.execute("use learning3;")
    data_learning.execute("SELECT * FROM Python")
    result = data_learning.fetchall()
    return render_template('sectionPython.html', result=result, section='Python', \
                            description='Python is a leader programming language. \
                            It’s one of the world’s most popular high-level programming\
                            languages and remains a firm favorite among many programmers.\
                            It is easy to learn and use, it is suitable for any tasks and \
                            it is incredibly reliable. Learn Pyhton with the collection of \
                            good quality videos we gathered for you from Youtube')

# section Cloud
@app.route('/sections/cloud/')
def select_cloud():
    data_learning = cur.connection.cursor()
    app.logger.info("choosing cloud section")
    data_learning.execute("use learning3;")
    data_learning.execute("SELECT * FROM Cloud")
    result = data_learning.fetchall()
    return render_template('sectionCloud.html', result=result, section='Cloud', description='Cloud \
                            refers to servers that are accessed over the Internet, and the software and databases \
                            that run on those servers. Cloud servers are located in data centers all over the world. \
                            By using cloud computing, users and companies don\'\t have to manage physical servers \
                            themselves or run software applications on their own machines.')

# section Docker
@app.route('/sections/docker/')
def select_docker():
    data_learning = cur.connection.cursor()
    app.logger.info("choosing sectionDocker section")
    data_learning.execute("use learning3;")
    data_learning.execute(f"SELECT * FROM Docker")
    result = data_learning.fetchall()
    return render_template('sectionDocker.html', result=result, section='Docker', description='Docker is \
                            Vestibulum magna massa, rutrum et justo eget, rhoncus dapibus lorem. \
                            Nulla facilisis erat non turpis tempor, vitae porta enim posuere. \
                            Nam pretium at nulla at volutpat. Vestibulum vitae nibh ac enim \
                            tempor tincidunt. Ut purus massa, laoreet non consectetur ac, ornare \
                            ut nisi. Maecenas euismod varius odio. Ut in dictum ligula.')

#section js
@app.route('/sections/js/')
def select_js():
    data_learning = cur.connection.cursor()
    app.logger.info("choosing js section")
    data_learning.execute("use learning3;")
    data_learning.execute(f"SELECT * FROM Javascript")
    result = data_learning.fetchall()
    return render_template('sectionJS.html', result=result, section='JavaScript', description='JavaScript is \
                            Vestibulum magna massa, rutrum et justo eget, rhoncus dapibus lorem. \
                            Nulla facilisis erat non turpis tempor, vitae porta enim posuere. \
                            Nam pretium at nulla at volutpat. Vestibulum vitae nibh ac enim \
                            tempor tincidunt. Ut purus massa, laoreet non consectetur ac, ornare \
                            ut nisi. Maecenas euismod varius odio. Ut in dictum ligula.')

#section add video
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
        sql = f"INSERT INTO {categorie} (name, chaine, url, description) VALUES ("
        for ii, i in enumerate(val):
            if ii == 3:
                sql = sql + "'" + i + "');"
            else:
                sql = sql + "'" + i + "', "
        data_learning.execute("use learning3;")
        data_learning.execute(sql)
        cur.connection.commit()
        data_learning.execute(f"SELECT MAX(id) from {categorie};")
        data = data_learning.fetchall()
        id = data[0][0]
        if categorie == "Python":
            return redirect(url_for("watch_python", id=id))
        if categorie == "Cloud":
            return redirect(url_for("watch_cloud", id=id))
        if categorie == "Docker":
            return redirect(url_for("watch_Docker", id=id))
        if categorie == "Javascript":
            return redirect(url_for("watch_js", id=id))
    else:
        return render_template('addPage.html')

# app.route('/add/submit_video/')
# def submit_video():
#     app.logger.info("start insert of video in bdd")
#     data_learning.mycursor.execute(f"SELECT * FROM Javascript")
#     result = data_learning.mycursor.fetchall()

    
##########################################################
# endpoint + parameter Python
@app.route('/sections/python/watch/<id>')
def watch_python(id):
    data_learning = cur.connection.cursor()
    app.logger.info("choosing video from python section")
    data_learning.execute("use learning3;")
    data_learning.execute(f'SELECT * FROM Python WHERE ID={id}')
    result = data_learning.fetchall()
    return render_template('watch.html', result=result)

# endpoint + parameter Cloud
@app.route('/sections/cloud/watch/<id>')
def watch_cloud(id):
    data_learning = cur.connection.cursor()
    app.logger.info("choosing video from cloud section")
    data_learning.execute("use learning3;")
    data_learning.execute(f'SELECT * FROM Cloud WHERE ID={id}')
    result = data_learning.fetchall()
    return render_template('watch.html', result=result)

# endpoint + parameter Docker
@app.route('/sections/docker/watch/<id>')
def watch_Docker(id):
    data_learning = cur.connection.cursor()
    app.logger.info("choosing video from Docker section")
    data_learning.execute("use learning3;")
    data_learning.execute(f'SELECT * FROM Docker WHERE ID={id}')
    result = data_learning.fetchall()
    return render_template('watch.html', result=result)

# endpoint + parameter JS
@app.route('/sections/js/watch/<id>')
def watch_js(id):
    data_learning = cur.connection.cursor()
    app.logger.info("choosing video from js section")
    data_learning.execute("use learning3;")
    data_learning.execute(f'SELECT * FROM Javascript WHERE ID={id}')
    result = data_learning.fetchall()
    return render_template('watch.html', result=result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3051, debug=True)


