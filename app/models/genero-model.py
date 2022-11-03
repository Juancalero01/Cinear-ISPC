from dataclasses import dataclass


@dataclass
class Genero():
    id_genero: int
    nombre_genero: str

    def getGenero(self):
        return self.nombre_genero

    def setGenero(self,nombre_genero):
        self.nombre_genero = nombre_genero
        
        