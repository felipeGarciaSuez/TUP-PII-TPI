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
    # Si hay libros disponibles para alquilar ejecutamos la gestion, sino el mismo mostrar_libros_disponibles() nos va a decir que no hay
    if res == True:
        opt = input("\nIngrese el codigo del libro que desea prestar:")
        for libro in libros:
            if libro['cod'] == opt:
                encontrado = True
                # Verificamos que el codigo exista y que tenga unidades disponibles para prestar, de caso contrario mostramos un mensaje
                if libro['cant_ej_ad'] < 1:
                    print(f'El libro {libro["titulo"]} no tiene ejemplares para prestar.')
                else:
                    # Pedimos la confirmacion si desea alquilar con un input
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
    # Declaro una variable hay libros por si no hay ningun libro disponible
    hayLibros = False
    print("COD - TITULO - AUTOR - CANTIDAD ADQUIRIDA - CANTIDAD ALQUILADA - ")

    # Primero recorro la lista con todos los libros
    for libro in libros:
        if libro["cant_ej_ad"] > 0:
            # Si el libro que recorremos tiene cantidad disponible para alquilar, mostramos el libro y seteamos el hayLibros en True
            hayLibros = True
            print(libro["cod"],"-", libro["titulo"],"-", libro["autor"],"-", libro["cant_ej_ad"],"-", libro["cant_ej_pr"])
    if hayLibros == False:
        print("No hay libros disponibles para alquilar")
    # Devolvemos el hayLibros por si cuando queremos ejecutar la funcion de prestar un libro no hay ninguno
    return hayLibros



