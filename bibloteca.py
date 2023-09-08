import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def registrar_nuevo_libro():
    cant_a_agregar = int(input("Cuantos libros desea agregar?\n"))
    
    for i in range(cant_a_agregar):
        
        nuevo_libro = l.nuevo_libro()
        libros.append(nuevo_libro)
    
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    res = mostrar_libros_disponibles()
    # Si hay libros disponibles para alquilar ejecutamos la gestion, sino el mismo mostrar_libros_disponibles() nos va a decir que no hay
    if res == True:
        opt = input("\nIngrese el codigo del libro que desea prestar:\n")
        busqueda = buscar_libro(opt)
        
        if busqueda != -1:
            # Verificamos que el codigo exista y que tenga unidades disponibles para prestar, de caso contrario mostramos un mensaje
            if libros[busqueda]['cant_ej_ad'] < 1:
                print(f'El libro {libros[busqueda]["titulo"]} no tiene ejemplares para prestar.')
            else:
                # Pedimos la confirmacion si desea alquilar con un input
                confirmacion = input(f'\nEl libro ingresado {libros[busqueda]["titulo"]} - {libros[busqueda]["autor"]} - {libros[busqueda]["cant_ej_ad"]}\n Escriba CANCELAR para volver atras, para confirmar presione Enter\n')
                confirmacion = confirmacion.upper()
                
                if confirmacion != 'CANCELAR':
                    libros[busqueda]['cant_ej_ad'] -= 1
                    libros[busqueda]['cant_ej_pr'] += 1
                    print(f'CONFIRMADO!! El libro {libros[busqueda]["titulo"]} a sido prestado!')
                else:
                    print("ALQUILER CANCELADO CON EXITO.")
    return None

def devolver_ejemplar_libro():
    
    mostrar_libros_prestados()

    codigo = input("Ingrese el codigo del libro que desea devolver: \n")
    index = buscar_libro(codigo)
    
    if index != -1:
        if libros[index]['cant_ej_pr'] > 0:
            confirmacion = input(f'\nEl libro ingresado {libros[index]["titulo"]} - {libros[index]["autor"]} - {libros[index]["cant_ej_pr"]} cantidades prestadas.\n Escriba CANCELAR para volver atras, para confirmar presione Enter\n')
            confirmacion = confirmacion.upper()
            
            if confirmacion != 'CANCELAR':
                libros[index]['cant_ej_pr'] -= 1
                libros[index]['cant_ej_ad'] += 1
                print(f'CONFIRMADO!! El libro {libros[index]["titulo"]} a sido devuelto!')
            else:
                print("DEVOLUCION CANCELADO CON EXITO.")
                aux_rta=input("Pulse cualquier tecla para continuar...")
        else:
            print(f'El libro {libros[index]["titulo"]} no tiene ejemplares en prestamo.')

    return None

def mostrar_libros_disponibles():
    # Declaro una variable hay libros por si no hay ningun libro disponible
    hayLibros = False
    
    print("_________________________________________________________________")
    print("|COD - TITULO - AUTOR - CANTIDAD ADQUIRIDA - CANTIDAD ALQUILADA - |")
    print("------------------------------------------------------------------")

    # Primero recorro la lista con todos los libros
    for libro in libros:
        if libro["cant_ej_ad"] > 0:
            # Si el libro que recorremos tiene cantidad disponible para alquilar, mostramos el libro y seteamos el hayLibros en True
            hayLibros = True
            print()
            print(libro["cod"],"-", libro["titulo"],"-", libro["autor"],"-", libro["cant_ej_ad"],"-", libro["cant_ej_pr"])
    if hayLibros == False:
        print("No hay libros disponibles para alquilar")
    # Devolvemos el hayLibros por si cuando queremos ejecutar la funcion de prestar un libro no hay ninguno
    return hayLibros


def buscar_libro(codigo):
    libro_actual = -1
    contador = 0
    
    for libro in libros:
        if libro['cod'] == codigo:
            libro_actual = contador
        else:
            contador += 1
    
    if libro_actual == -1:
        print('ERROR!! No se han encontrado libros con ese codigo')
    return libro_actual


def mostrar_libros_prestados(): 
    # Declaro una variable hay libros por si no hay ningun libro disponible
    hayLibros = False
    print("_________________________________________________________________")
    print("|COD - TITULO - AUTOR - CANTIDAD ADQUIRIDA - CANTIDAD ALQUILADA - |")
    print("------------------------------------------------------------------")

    # Recorro la lista con todos los libros
    for libro in libros:
        if libro["cant_ej_pr"] > 0:
            # Si la posicion del libro en la que estamos posee una cantidad mayor a 0 de ejemplares prestados mostramos y cambiamos la bandera
            hayLibros = True
            print(libro["cod"],"-", libro["titulo"],"-", libro["autor"],"-", libro["cant_ej_ad"],"-", libro["cant_ej_pr"])
    if hayLibros == False:
        print("No hay ejemplares prestados de ningun libro")
    # Devolvemos el hayLibros por si cuando queremos ejecutar la funcion de prestar un libro no hay ninguno
    return None

