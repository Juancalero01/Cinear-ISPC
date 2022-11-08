from sqlite3 import connect
from dotenv import load_dotenv
import os
load_dotenv()


class Database:

    def __init__(self) -> None:
        self.__CONN = os.getenv('DB_HOST')

    def findAll(self, query):
        with connect(self.__CONN) as conn:
            cursor = conn.cursor()
            try:
                res = cursor.execute(query).fetchall()
                cursor.commit()
                return res
            except Exception as ex:
                return ex

    def findOne(self, query):
        with connect(self.__CONN) as conn:
            cursor = conn.cursor()
            try:
                res = cursor.execute(query).fetchone()
                cursor.commit()
                return res
            except Exception as ex:
                return ex

    def default(self, query):
        with connect(self.__CONN) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query)
                cursor.commit()
            except Exception as ex:
                return ex
