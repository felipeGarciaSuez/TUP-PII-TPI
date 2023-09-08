import cod_generator as generator

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    datos = True
    while datos == True:
        
        nombre = input("Ingrese el nombre del libro que desea ingresar: \n")
        autor = input("Ingrese el autor del libro: \n")
        unidades = int(input("CUantas unidades de este libro posee:"))
        codigo = generar_codigo()
        
        nuevo_libro = {'cod': codigo, 'cant_ej_ad': unidades, 'cant_ej_pr': 0, "titulo": nombre, "autor": autor}
        
        print(nuevo_libro)
        
        datos = False
        res = input("\nLos datos ingresados son correctos? \n\nPresione cualquier letra para continuar o escriba NO para volver a ingresar los datos\n")
        
        if res.upper() == "NO":
            datos = True

    return nuevo_libro

def generar_codigo():
    code = generator.generar()
    return code