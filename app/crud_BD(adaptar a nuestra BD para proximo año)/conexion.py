import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'contrasena',
                db = 'NombreEjemplo'
            )
            
        except mysql.connector.Error as descripcionError:
            print("¡No se conecto!",descripcionError)

    def InsertarValor(self ,nombre,telefono,direccion):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                sentenciaSQL= "INSERT INTO TablaEjemplo VALUES(%s,%s,%s)" # en los % despues se pasan los valores al llamar metodo
                data= (nombre, telefono, direccion)

                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()
                
            except:
                print("no se puede conectar a la base de datos")
#LEER, BUSCAR

    def BuscarObjeto(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM TablaEjemplo"
                cursor.execute(sentenciaSQL)
                resultadoREAD = cursor.fetchall()
                self.conexion.close()
                return resultadoREAD
            except:
                print("no se puede conectar a la base de datos")

#ELIMINAR 
    def EliminarObjeto(self,id):
        if self.conexion.is_connected():
            try: 
                cursor= self.conexion.cursor()
                sentenciaSQL= "DELATE from TablaEjemplo where id=ID"
                cursor.execute(sentenciaSQL)

                self.conexion.commit()
                self.conexion.close()
           
            except:
                print("no se puede conectar a la base de datos")

#EDITAR
    def InsertarValor(self,nombre,telefono,direccion):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                sentenciaSQL= "INSERT INTO TablaEjemplo VALUES(%s,%s,%s)" # en los % despues se pasan los valores al llamar metodo
                data= (nombre, telefono, direccion)

                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()
                
            except:
                print("no se puede conectar a la base de datos")