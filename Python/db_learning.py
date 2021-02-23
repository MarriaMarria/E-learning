import json
import mysql.connector

class Mydb_scrap:
    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="pw",
                    database= "learning2",
                    auth_plugin='mysql_native_password'
                )
        self.mycursor=self.mydb.cursor()
        self.list_tables = []
        self.data_dict = {}
    
    def get_tables(self):
        with open('links.json') as json_data:
            self.data_dict = json.load(json_data)
        for i in self.data_dict:
            self.list_tables.append(i)

    def create_table(self):
        for i in self.list_tables:
            sql = "CREATE TABLE IF NOT EXISTS {} (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), chaine VARCHAR(100), url TEXT);".format(i)
            print("c ok")
            self.mycursor.execute(sql)

    def insert_table(self):
        for i in self.data_dict.items():
            categorie = i[0]
            for y in i[1]:
                val = tuple(y.values())
                db_key = ", ".join(y.keys())
                sql = "INSERT INTO {} ({}) VALUES {};".format(categorie, db_key, val)
                self.mycursor.execute("USE learning2;")
                self.mycursor.execute(sql)
                self.mydb.commit()