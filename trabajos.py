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
        self.resultado = ()

        """funcion que inicializa una variable registroAlumnoMateria"""
    

    def agregar_nota(self,numero)-> list:
        self.notas.append(numero)
        return self.notas

    def mostrar_notas(self):
        print(self.notas)

    def calcular_promedio(self)->float:
        return  sum(self.notas) / len(self.notas)

        

    def mostrar_estado(self)-> str: 
        if self.calcular_promedio() < 4 :
            return "Estas libre"
        elif self.calcular_promedio() >= 7:
            return "¡Promocion!"
        else: 
            return "Quedaste regular"
        
    def __str__(self):
        return (f"{self.nombre},{self.materia},{self.mostrar_estado()}")


a = RegistroAlumnoMateria ("Bety","Lengua")
a.agregar_nota(4)
a.agregar_nota(9)
a.agregar_nota(8)
a.agregar_nota(10)
a.mostrar_notas()
print(a)


assert a.mostrar_estado() == "¡Promocion!"

"""
2.a* A la clase punto vista en la materia agregarle 
el método Distancia al origen ()siendo el origen el punto (0,0). Crear un programa que 
use este método para imprimir en pantalla
 la distancia entre al origen de los puntos A, B y C.

class puntovista:
    def __init__ (self,punto):

    def distanciaalorigen(self):
        origen = (0,0)

A = Punto(2,3)
B = Punto(5,5)
C = Punto(1,5)

A.distancia(B)
assert A.distancia_origen() == 3.605551275463989
assert B.distancia_origen() == 7.0710678118654755
assert C.distancia_origen() == 5.0990195135927845"""
