#puedo agrupar varias valores en una variable

#Listas
#Se puede modificarm es ordenada(maneja indices)

alumnos = ["Juan", "Pedro", "Maria","Carlos","Akainu"]

#Las listas empiezan con la posicion 0

print(alumnos[0])
print(alumnos[4])

# Para saber el contenido longitu nde datos 

print(len(alumnos))

#si queremos recorrer la lista de derecha a uzq utilizaremos numeros negativos
print(alumnos[-2])
print(alumnos[-1])

print(alumnos[len(alumnos)-1])

# agregar elemento a una lista ya creada
alumnos.append("Juan")

print(alumnos)

alumnoEliminado = alumnos.pop(3)
print(alumnos)
print(alumnoEliminado)

#del > podemos eliminar variables, eliminar posisiones de la ista y otras cosas
del alumnos[0]

alumnos[0] = 'Carlos El mejor'
print(alumnos)

alumnos.clear()
print(alumnos)

# las listas pueden contener varios tipos de datos
mixto = ['lunes', 10, False, 80.5,[1,2,3]]
print(mixto)

ejercicio = [1,2,3,[4,5,6]]

#Devolver como puedo devolver el valor nd ela posion 3
print("Posicion Nª", ejercicio[2])

#Devolver como puedo devolver el valor de 5

print("Posicion Nª",ejercicio[3][1])