"""
python -m pip install mysql-connector-python

si hay varias versiones de python
c:\python39\python -m pip install mysql-connector-python
"""
import mysql.connector
#from typing import Union, Optional, Dict, List
from typing import Dict, List


class MysqlCli:

    def __init__(self, arconn = Dict):
        self.__arerrors = []
        self.__ifoundrows = 0
        self.__iaffectedrows = 0
        self.__ilastid = -1
        self.__arconn = arconn
        self.__connection = None

    def __get_connection(self):
        if not self.__connection:
            self.__connection = mysql.connector.connect(**self.__arconn)
        return self.__connection

    def close(self) -> None:
        if self.__connection and self.__connection.is_connected():
            self.__connection.close()
            self.__connection.disconnect()
        self.__connection = None

    def query(self, sql: str) -> List:
        cursor = None
        try:
            conn = self.__get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            result = cursor.fetchall()
            self.__ifoundrows = self.__get_found_rows(cursor)
            self.__iaffectedrows = cursor.rowcount
            return result
        except mysql.connector.Error as error:
            self.__arerrors.append(error)
        finally:
            if cursor:
                cursor.close()

    @staticmethod
    def __get_found_rows(cursor) -> int:
        cursor.execute("SELECT FOUND_ROWS() n")
        result = cursor.fetchall()
        if result:
            return int(result[0].get("n",-1))
        return 0

    @staticmethod
    def __get_last_insert_id(cursor) -> int:
        cursor.execute("SELECT LAST_INSERT_ID() id")
        result = cursor.fetchall()
        if result:
            return int(result[0][0])
        return -1

    def exec(self, sql: str, ismulti:bool = False) -> None:
        cursor = None
        try:
            conn = self.__get_connection()
            cursor = conn.cursor()
            if not ismulti:
                cursor.execute(sql)
            else:
                for r in cursor.execute(sql, multi=ismulti): pass;

            conn.commit()

            self.__iaffectedrows = cursor.rowcount
            if sql.find("INSERT INTO ("):
                self.__ilastid = self.__get_last_insert_id(cursor)

        except mysql.connector.Error as error:
            self.__arerrors.append(error)
        finally:
            if cursor:
                cursor.close()

    def is_error(self) -> bool:
        return True if self.__arerrors else False

    def get_errors(self) -> List:
        return self.__arerrors

    def get_lastid(self)->int:
        return self.__ilastid
