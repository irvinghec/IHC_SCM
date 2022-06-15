import doctores.acciones
print("Irving Hernandez Carlos 9°A")
print("""
Accede al sistema:
    1. Iniciar sesión
    2. Registrarse
""")

opcion = doctores.acciones.Acciones()
accion = input("Ingresa no. de opción: ")

if accion == "1":
    opcion.login()
elif accion == "2":
    opcion.registro()
