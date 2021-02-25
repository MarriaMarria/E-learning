from db_learning import MyDB
from backend import *

mydb = MyDB()
mydb.get_tables()
mydb.create_table()
mydb.insert_table()

# we will add if __name__ == __main__ etc

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3051, debug=True)