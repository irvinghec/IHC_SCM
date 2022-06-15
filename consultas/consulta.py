import doctores.conexion as conexion

connect = conexion.conect()
database = connect[0]
cursor = connect[1]

class Consulta:
    def __init__(self, doctor_id, paciente="", apellidos="", edad=None, telefono=None, consultorio=None, problema="", sexo="", nombre=""):
        self.doctor_id = doctor_id
        self.paciente = paciente
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono
        self.consultorio = consultorio
        self.problema = problema
        self.sexo = sexo
        self.nombre = nombre
        

    def guardar(self):
        sql = "INSERT INTO consultas VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s, NOW())"
        consulta = (self.doctor_id, self.paciente, self.apellidos, self.edad, self.telefono, self.consultorio, self.problema, self.sexo)
        
        cursor.execute(sql, consulta)
        database.commit()
        return [cursor.rowcount, self]
    def listar(self):
        sql = f"SELECT * FROM consultas WHERE doctor_id = {self.doctor_id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def validar(self):
        sql = f"SELECT * FROM consultas WHERE paciente = '{self.paciente}'"
        cursor.execute(sql)
        return [cursor.rowcount, self]
        
    def actualizar(self):
        sql = f"UPDATE consultas SET paciente = '{self.paciente}', apellidos = '{self.apellidos}', edad = {self.edad}, telefono = {self.telefono}, consultorio = {self.consultorio}, problema = '{self.problema}', sexo = '{self.sexo}' WHERE paciente = '{self.nombre}'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]
    
    def eliminar(self):
        sql = f"DELETE FROM consultas WHERE doctor_id = {self.doctor_id} AND paciente = '{self.paciente}'"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]
