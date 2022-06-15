import doctores.doctor as modelo
import consultas.acciones 

class Acciones:

    def registro(self):
        print("### Ser realizara tu registro en el sistema ###")

        nombre = input("¿Cual es tu nombre? ")
        apellidos = input("¿Cuales son tus apellidos? ")
        consultorio = input("¿Cual es en numero de tu consultorio? ")
        correo = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        doctor = modelo.Doctor(nombre,apellidos,consultorio,correo,password)
        registro = doctor.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre}, te haz registrado con el email {registro[1].correo}")
        else:
            print("\nNo te haz registrado correctamnete !!!")


    def login(self):
        print("Identificate en el sistema")
        #try:
        correo = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
        doctor = modelo.Doctor('', '', '', correo, password)
        login = doctor.identificar()

        if correo == login[4]:
            print(f"Bienvenido {login[1]}, has ingresado con el correo {login[4]} en el sistema")
            self.proximasAcciones(login)

        """ except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print("\n Login incorrecto intentalo mas tarde ") """
        
    def proximasAcciones(self, doctor):
        print("""
Menu de acciones 

    1. Crear consulta
    2. Mostrar consultas
    3. Modificar consulta
    4. Eliminar consulta
    5. salir
""")
        
        accion = input("Ingresa el número de opcion: ")
        op = consultas.acciones.Acciones()

        if accion == "1":
            op.crear(doctor)
            self.proximasAcciones(doctor)
        elif accion == "2":
            op.listar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "3":
            op.actualizar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "4":
            op.eliminar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "5":
            print("Adios")
            exit()
