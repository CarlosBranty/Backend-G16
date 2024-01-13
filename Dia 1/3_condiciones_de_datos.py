# Segun el sexo y la estatura hacer lo siguiente
#si es masculino
    # si mide mas de 1.50 entonces indicar que no hay prendas
    #si mide entre 1.30 y 1.49 indicar que si hay ropa
    #si mide menos de 1.30 indicar que no hay prendas
#si es femenino
    #si mide masd de 1.40 indicar que no hay prendas
    #si mide entre 1.10 y 1.49 indicar que si hay
    #si mide menos de 1.10 indicar que no hay prendas

sexo = 'Masculino'
estatura = 1.35

if sexo == 'Masculino':
    if estatura > 1.30 and estatura<1.49:
        print('Si hay ropa')
    else :
        print('No hay ropa')

if sexo == 'Femenino':
    if estatura > 1.10 and estatura <1.14:
        print('No hay ropa')
    else :
        print('Si hay ropa')
        # o usamos el pass o colocamos la logica
        #pass> pasa no hace nada per nos permite dejar la condicional vacia
        pass

# Si el usuario es PERUANO pagara 5 soles si es EXTRANJERO pagara 8 soles
nacionalidad = 'Ecuador'

if nacionalidad == 'Peruano':
    print('Pagara 5 soles')
else :
    print('Pagara 8 soles')

resultado = 'Pagara 5 soles' if nacionalidad == 'Peruano' else 'Pagara 8 soles'
print(resultado)
    