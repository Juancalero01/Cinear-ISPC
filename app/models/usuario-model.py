from dataclasses import dataclass


@dataclass
class Usuario():
    id_usuario: int
    nombre_usuario: str
    apellido_usuario: str
    correo_electronico: str
    contrasenia: str
    pais: str

    def getNombreUsuario(self):
        return self.nombre_usuario

    def getApellidoUsuario(self):
        return self.apellido_usuario

    def getCorreoElectronico(self):
        return self.correo_electronico

    def getContrasenia(self):
        return self.contrasenia

    def getPais(self):
        return self.pais
