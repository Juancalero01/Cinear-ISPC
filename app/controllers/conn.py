from sqlite3 import connect
from dotenv import load_dotenv
import os
load_dotenv()


class Database:

    def __init__(self) -> None:
        self.__CONN = os.getenv('DB_HOST')

    def query(self, query):
        with connect(self.__CONN) as conn:
            cursor = conn.cursor()
            try:
                res = cursor.execute(query).fetchall()
                cursor.commit()
                return res
            except Exception as ex:
                return ex
