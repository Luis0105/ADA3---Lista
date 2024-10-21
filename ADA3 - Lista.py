postres = {}
ingredientes_guardados = {}


def imprimir(postre):
    if postre in postres:
        print(f"Ingredientes del {postre}: {postres[postre]}")
    else:
        print(f"El postre {postre} no esta registrado.")
        
def insertar(postre, nuevo):
    if postre in postres:
        postres[postre].extend(nuevo)
        print(f"Ingredientes actualizados para {postre}: {postres[postre]}")
    else:
        print(f"El postre {postre} no esta registrado.")

def eliminar(postre, ingrediente):
    if postre in postres:
        if ingrediente in postres[postre]:
            postres[postre].remove(ingrediente)
            print(f"Ingrediente {ingrediente} eliminado de {postre}.")
            print(f"Ingredientes actuales de {postre}: {postres[postre]}")
        else: 
            print(f"El ingrediente {ingrediente} no está en la lista de {postre}.")
    else:
        print(f"El postre {postre} no esta registrado.")

def eliminar_todos_ingredientes(postre):
    if postre in postres:
        postres[postre].clear()
        print(f"Todos los ingredientes de {postre} han sido eliminados.")
    else:
        print(f"El postre {postre} no está registrado.")
        
def alta(postre, ingredientes):
    if postre not in postres:
        postres[postre] = ingredientes
        print(f"Postre {postre} dado de alta con ingredientes: {ingredientes}")
    else:
        print(f"El postre {postre} ya existe.")
        
def baja(postre):
    if postre in postres:
        ingredientes_guardados[postre] = postres[postre]
        del postres[postre]
        print(f"Postre {postre} dado de baja, pero los ingredientes han sido guardados.")
    else:
        print(f"El postre {postre} no está registrado.")
        
def listar_postres():
    if postres:
        print("Postres disponibles:")
        for postre in postres:
            print(f"- {postre}")
    else:
        print("No hay postres registrados.")
        
def eliminar_repetidos():
    for postre in postres:
        postres[postre] = list(set(postres[postre]))
        print(f"Ingredientes sin repetir para {postre}: {postres[postre]}")

def menu():
    while True:
        print("\n--- Menú de Postres ---")
        print("1. Alta de postre")
        print("2. Imprimir ingredientes")
        print("3. Insertar ingredientes")
        print("4. Eliminar ingrediente")
        print("5. Baja de postre")
        print("6. Eliminar todos los ingredientes de un postre")
        print("7. Lista de postres disponibles")
        print("8. Ver ingredientes guardados")
        print("9. Eliminar ingredientes repetidos")
        print("10. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            postre = input("Ingrese el nombre del postre: ")
            ingredientes = input("Ingrese los ingredientes separados por coma: ").split(",")
            alta(postre.strip(), [ingrediente.strip() for ingrediente in ingredientes])
        elif opcion == '2':
            postre = input("Ingrese el nombre del postre: ")
            imprimir(postre.strip())
        elif opcion == '3':
            postre = input("Ingrese el nombre del postre: ")
            nuevos = input("Ingrese los nuevos ingredientes separados por coma: ").split(",")
            insertar(postre.strip(), [nuevo.strip() for nuevo in nuevos])
        elif opcion == '4':
            postre = input("Ingrese el nombre del postre: ")
            ingrediente = input("Ingrese el ingrediente a eliminar: ")
            eliminar(postre.strip(), ingrediente.strip())
        elif opcion == '5':
            postre = input("Ingrese el nombre del postre: ")
            baja(postre.strip())
        elif opcion == '6':
            postre = input("Ingrese el nombre del postre: ")
            eliminar_todos_ingredientes(postre.strip())
        elif opcion == '7':
            listar_postres()
        elif opcion == '8':
            if ingredientes_guardados:
                print("Ingredientes guardados:")
                for postre, ingredientes in ingredientes_guardados.items():
                    print(f"{postre}: {ingredientes}")
            else:
                print("No hay ingredientes guardados.")
        elif opcion == '9':
            eliminar_repetidos()
        elif opcion == '10':
            print("\nSaliendo del programa....")
            break
        
menu()
print()
