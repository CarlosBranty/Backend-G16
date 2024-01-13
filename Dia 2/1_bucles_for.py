#

alumnos = ['Angel','Brayan','Carlos','Hiroito','Claudia','Samael','Marco']

for alumno in alumnos:
    print(alumno)

# for se puede utilizar con string textos
frase = 'No ay mal que por bien no venga'

for letra in frase:
#     if letra != ' ':
#         print(letra)
#     else:
#         pass
    #imprimir el texto pero sin espacios
# Forma 2
# for letra in frase:
#     if letra != ' ':
#         print(letra)

# Forma 3
# continue > termina el ciclo actual la iteracion en camino y  no permite nada mas lueo
# continue solo se puede utilizar dentro de un ciclo o loop
#

    # if letra == ' ':
    #     continue
    # print(letra)
#Forma 4
    None if letra == ' ' else print(letra)
print('---------------------')
edad = None

# range > si quiero realizar un for manual sin uso de listas, tuplas, set o textos
for numero in range(4):
    print(numero)
print('---------------------')

#Range inicio y limite
for numero in range(1,4):
    print(numero)

#Range inicio, limite y incrementa decrementa
print('---------------------')
for numero in range(1,10,2):
    print(numero)

print('---------------------')
#Iterar la variable texto y ver cuantas vocales hay
texto = 'Hola me llamo eduardo'
vocales = ['a','e','i','o','u']

contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1
        
#Formas de imprimir un texto combinado con variables
print('Hay',contador, 'vocales en total')
print('Hay {} vocales'.format(contador))
print(f'Hay {contador} vocales')
print('Hay %s vocales' %contador)

print('---------------------')
print(99/5)
print(99%5)
print(99//5)

#Como saber si un numero es par o impar
#utilizando range quiero saber cuantos numero pares tengo
print('---------------------')
rango  = range(1, 56)

contadorNumeros = 0

for numero in range(1,56):
    if numero % 2 == 0:
        contadorNumeros = contadorNumeros +1
print(f'Hay {contadorNumeros} números pares')