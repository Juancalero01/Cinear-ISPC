from conn import Database

db = Database()

query_sql = None


#  TESTING DE BASE DE DATOS

query_sql = """
    SELECT * FROM USUARIOS
"""

print(query_sql)
