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

"""1.b Implementar la clase registroAlumnoMateria() que guarde varias notas y diga si el alumno está regular, promocional o libre. Con las siguientes reglas.
    Constructor: (Nombre, Materia)
    Agregar nota: Agrega una nota al alumno en la materia (lista de notas)
    Promedio: Devuelve el promedio de notas que tiene el alumno
    Mostrar notas: imprime la lsita de notas
    Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)"""

class RegistroAlumnoMateria:
    promedio = ()
    def __init__(self, nombre, materia): # Agregar parámetros
        self.nombre = nombre
        self.materia = materia 
        self.notas = []

        """funcion que inicializa una variable registroAlumnoMateria"""
        
    def __str__(self)->None:
        print(str(self.nombre)+ ":" + str(self.materia))

    def agregar_nota(self,numero)-> list:
        self.notas.append(numero)
        return self.notas

    def mostrar_notas(self):
        print(self.notas)

    def calcular_promedio(self)->float:
        self.promedio = sum(self.notas) / len(self.notas)
        promedio = self.promedio
        return promedio
        

    def mostrar_estado(self): 
        if self.promedio < 4 :
            print("Estas libre")
        elif self.promedio >= 7:
            print("¡Promocion!")
        else: 
            print("Quedaste regular")


a = RegistroAlumnoMateria ("Bety", "Lengua")
a.agregar_nota(4)
a.agregar_nota(9)
a.agregar_nota(8)
a.agregar_nota(10)
a.mostrar_notas()
a.calcular_promedio()
a.__str__()
a.mostrar_estado()

"""assert alumno1.mostrar_estado() == "promocionado"
assert alumno1.__str__() == "Juan, Matemáticas, promocionado"""
