import json
import mysql.connector
import logging

logging.basicConfig(filename='db_learning.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')


class MyDB: # I changed name as SCRAP has nothing to do with it

    logging.info("connecting to the database: start")

    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="ms2", # "localhost" # remember to change HOST
                    user="root",
<<<<<<< HEAD
                    password="password", #pw # change password
                    database= "learning3",
=======
                    password="Legalcy97.1", #pw
                    database= "learning2",
>>>>>>> 21144f0 (mise en page de la page watch)
                    auth_plugin='mysql_native_password'
                )

        self.mycursor = self.mydb.cursor()
        self.list_tables = []
        self.data_dict = {}

    logging.info("connecting to the database: end")
    
    def get_tables(self):

        logging.info("Getting tables: start")

        with open('./links.json') as json_data:
            self.data_dict = json.load(json_data)
        for i in self.data_dict:
            self.list_tables.append(i)

        logging.info("Getting tables: end")

    def create_table(self):

        logging.info("creating table: start")

        for i in self.list_tables:
            sql = "CREATE TABLE IF NOT EXISTS {} (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), chaine VARCHAR(100), url TEXT, description TEXT);".format(i)
            self.mycursor.execute(sql)

        logging.info("creating table: end")

    def insert_table(self):

        logging.info("inserting into table: start")

        for i in self.data_dict.items():

            categorie = i[0]

            for y in i[1]:
                val = tuple(y.values())
                db_key = ", ".join(y.keys())
                sql = "INSERT INTO {} ({}) VALUES {};".format(categorie, db_key, val)
                
                self.mycursor.execute("USE learning2;")
                self.mycursor.execute(sql)
                self.mydb.commit()

        logging.info("inserting into table: end")

# test = MyDB()  # instance of the class
# test.get_tables()
# test.create_table()
# test.insert_table()