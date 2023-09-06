import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    # completar
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    res = mostrar_libros_disponibles()
    encontrado = False
    if res == True:
        print()
        opt = input("\nIngrese el codigo del libro que desea prestar:")
        for libro in libros:

            if libro['cod'] == opt:
                encontrado = True
                if libro['cant_ej_ad'] < 1:
                    print(f'El libro {libro["titulo"]} no tiene ejemplares para prestar.')
                else:
                    confirmacion = input(f'\nEl libro ingresado {libro["titulo"]} - {libro["autor"]} - {libro["cant_ej_ad"]}\n Escriba CANCELAR para volver atras, para confirmar presione Enter')
                    if confirmacion != 'CANCELAR':
                        libro['cant_ej_ad'] -= 1
                        libro['cant_ej_pr'] += 1
                        print(f'CONFIRMADO!! El libro {libro["titulo"]} a sido prestado!')
        if encontrado == False:
            print('ERROR!! No se han encontrado libros con ese codigo')
    return None

def devolver_ejemplar_libro():

    return None

def nuevo_libro():
    #completar
    return None

def mostrar_libros_disponibles():
    hayLibros = False
    print("COD - TITULO - AUTOR - CANTIDAD ADQUIRIDA - CANTIDAD ALQUILADA - ")
    for libro in libros:
        if libro["cant_ej_ad"] > 0:
            hayLibros = True
            print(libro["cod"],"-", libro["titulo"],"-", libro["autor"],"-", libro["cant_ej_ad"],"-", libro["cant_ej_pr"])
    if hayLibros == False:
        print("No hay libros disponibles para alquilar")
    return hayLibros



