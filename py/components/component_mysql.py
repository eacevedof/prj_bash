#python -m pip install mysql-connector-python
import mysql.connector
from typing import Union, Optional, Dict, List

"""
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()
"""

class ComponentMysql:

    def __init__(self, arconn = Dict):
        self.__iserror = False
        self.__ifoundrows = 0
        self.__iaffectedrows = 0
        self.__ilastid = -1
        self.__arconn = arconn
        self.__connection = None

    def __get_connection(self):
        if not self.__connection:
            self.__connection mysql.connector.connect(
                host=self.__arconn.get("server",{}),
                user=self.__arconn.get("user",""),
                password=self.__arconn.get("password",""),
                database=self.__arconn.get("database",""),
            )
        return self.__connection

    def close(self) -> None:
        if self.__connection and self.__connection.is_connected():
            self.__connection.close()

    def query(self, sql: str) -> List:
        try:
            conn = self.__get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            result = cursor.fetchall()
            self.__ifoundrows = cursor.rowcount
            return result
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            cursor.close()

    def execute(self, sql: str):
        try:
            conn = self.__get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            self.__iaffectedrows = cursor.rowcount
        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))
        finally:
            cursor.close()
