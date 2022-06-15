import consultas.consulta as modelo

class Acciones:
    def crear(self, doctor):
        print(f"OK, {doctor[1]}. Ingrese datos de consulta ")
        
        paciente = input("Ingrese nombre del paciente: ")
        apellidos = input("Ingrese apellidos del paciente: ")
        edad = input("Ingrese la edad del paciente: ")
        telefono = input("Ingrese telefono del paciente: ")
        consultorio = input("Ingrese consultorio: ")
        problema = input("Ingrese problema del paciente: ")
        sexo = input("Ingrese genero del paciente(m/h): ")

        consulta = modelo.Consulta(doctor[0], paciente, apellidos, edad, telefono, consultorio, problema, sexo)
        guardar = consulta.guardar()
        if guardar[0] >= 1:
            print(f"\n Perfecto! has guardado la consulta de: {consulta.paciente}")
        else:
            print(f"\nNo se guardo tu consulta {doctor[1]}!!!")

    def listar(self, doctor):
        print(f"\n{doctor[1]}, {doctor[0]}!! Estas son tus consultas: ")
        consulta = modelo.Consulta(doctor[0])
        consultas = consulta.listar()

        #print(consultas)
        for consulta in consultas:
            print("\n***********")
            print(f"Nombre del paciente: {consulta[2]}")
            print(f"Fecha de la consulta: {consulta[9]}")
            print(f"Problema: {consulta[7]}")
            print(f"consultorio: {consulta[6]}")
            print("\n***********")

    def actualizar(self, doctor):
        print(f"\n[{doctor[0]}]Dr. {doctor[1]}. Modificar una consulta")

        paciente = input("Introduce el nombre del paciente para modificar sus datos: ")

        consulta = modelo.Consulta(doctor[0], paciente)
        validar = consulta.validar()
        if validar[0] != 0:
            self.modificar(doctor, paciente)
        else:
            print(f"\nNo se encontró ninguna consulta con el nombre del paciente {paciente}")

    def modificar(self, doctor, nombre):
        print(f"\n[{doctor[0]}]Dr. {doctor[1]} Escriba los nuevos datos del paciente {nombre}")

        paciente = input("Ingrese nombre del paciente: ")
        apellidos = input("Ingrese apellidos del paciente: ")
        edad = input("Ingrese la edad del paciente: ")
        telefono = input("Ingrese telefono del paciente: ")
        consultorio = input("Ingrese consultorio: ")
        problema = input("Ingrese problema del paciente: ")
        sexo = input("Ingrese genero del paciente(m/h): ")

        consulta = modelo.Consulta(doctor[0], paciente, apellidos, edad, telefono, consultorio, problema, sexo, nombre)
        guardar = consulta.actualizar()
        if guardar[0] >= 1:
            print(f"\nSe han modificado los datos del paciente: {consulta.paciente}.\n")
        else:
            print(f"\nNo se pudo modificar la consulta agendada del paciente, intente más tarde: {doctor[1]}")


    def eliminar(self, doctor):
        print(f"\n[{doctor[1]}] {doctor[1]} {doctor[2]}. Eliminar una consulta")
        paciente = input("Introduce el nombre del paciente para eliminar su consulta: ")

        nota = modelo.Consulta(doctor[0], paciente)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"\nSe eliminó la consulta de {nota.paciente}")
        else:
            print("\nNo se puedo eliminar la consulta, intenta más tarde...")
