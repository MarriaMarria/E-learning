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
    data_learning.mycursor.execute("SELECT * FROM Python")
    result = data_learning.mycursor.fetchall()
    return render_template('section.html', result=result, section='Python', \
                            description='Python is a leader programming language. \
                            It’s one of the world’s most popular high-level programming\
                            languages and remains a firm favorite among many programmers.\
                            It is easy to learn and use, it is suitable for any tasks and \
                            it is incredibly reliable. Learn Pyhton with the collection of \
                            good quality videos we gathered for you from Youtube')

# section Cloud
@app.route('/sections/cloud/')
def select_cloud():
    app.logger.info("choosing cloud section")
    data_learning.mycursor.execute("SELECT * FROM Cloud")
    result = data_learning.mycursor.fetchall()
    return render_template('section.html', result=result, section='Cloud', description='Cloud is \
                            Vestibulum magna massa, rutrum et justo eget, rhoncus dapibus lorem. \
                            Nulla facilisis erat non turpis tempor, vitae porta enim posuere. \
                            Nam pretium at nulla at volutpat. Vestibulum vitae nibh ac enim \
                            tempor tincidunt. Ut purus massa, laoreet non consectetur ac, ornare \
                            ut nisi. Maecenas euismod varius odio. Ut in dictum ligula.')

# section Docker
@app.route('/sections/docker/')
def select_docker():
    app.logger.info("choosing docker section")
    data_learning.mycursor.execute(f"SELECT * FROM Docker")
    result = data_learning.mycursor.fetchall()
    return render_template('section.html', result=result, section='Docker', description='Docker is \
                            Vestibulum magna massa, rutrum et justo eget, rhoncus dapibus lorem. \
                            Nulla facilisis erat non turpis tempor, vitae porta enim posuere. \
                            Nam pretium at nulla at volutpat. Vestibulum vitae nibh ac enim \
                            tempor tincidunt. Ut purus massa, laoreet non consectetur ac, ornare \
                            ut nisi. Maecenas euismod varius odio. Ut in dictum ligula.')

#section js
@app.route('/sections/js/')
def select_js():
    app.logger.info("choosing js section")
    data_learning.mycursor.execute(f"SELECT * FROM Javascript")
    result = data_learning.mycursor.fetchall()
    return render_template('section.html', result=result, section='JavaScript', description='JavaScript is \
                            Vestibulum magna massa, rutrum et justo eget, rhoncus dapibus lorem. \
                            Nulla facilisis erat non turpis tempor, vitae porta enim posuere. \
                            Nam pretium at nulla at volutpat. Vestibulum vitae nibh ac enim \
                            tempor tincidunt. Ut purus massa, laoreet non consectetur ac, ornare \
                            ut nisi. Maecenas euismod varius odio. Ut in dictum ligula.')

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
    app.run(host="0.0.0.0", port=3051, debug=True)