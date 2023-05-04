class AlumnoMateria:
    def __init__(self, nombre, materia, nota): # Agregar parámetros
        """funcion que inicializa una variable AlumnoMateria
        tener en cuenta las condiciones del TAD (texto e int)
        """
        
        self.nombre = nombre
        self.nota = nota
        nota = int
        self.materia = materia

    def imprimir_datos(self)->str:
        print(f'{self.nombre},{self.materia},{self.nota}')

    def __str__(self):
        return str(self.nombre)+ ", " + str(self.materia)+ ", " + str(self.nota) 
        

    def mostrar_estado(self)->str: 
        """calcula si esta regular, promocionado, o libre"""
        nota = self.nota
        if nota<4:
            estado = "libre"
        elif nota >= 4 and nota < 7:
            estado = "regular"
        else:
            estado = "promocionado"
        return estado
        
        assert type(nombre) == str, "Esto no es un string"
        assert type(materia) == str, "Esto no es un string"
        assert type(nota) == int, f"Esto no es un entero es {type(nota)}"
        assert nota >= 0 and nota <= 10, "nota no esta entre 0 y 10"



# Test
alumno1 = AlumnoMateria ("Juan", "Matematicas", 4)
assert alumno1.__str__() == "Juan, Matematicas, 4"
assert alumno1.mostrar_estado() == "regular"