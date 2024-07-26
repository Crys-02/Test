def switch_case(option):
    switch = {
        'a': "Opción A: Inicio",
        'b': "Opción B: Configuración",
        'c': "Opción C: Salir"
    }
    return switch.get(option, "Opción no válida")

opcion = input("Elija una opcion de a-c: ").lower()
print(switch_case(opcion))



