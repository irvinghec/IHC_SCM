import hashlib
import doctores.conexion as conexion

connect = conexion.conect()
database = connect[0]
cursor = connect[1]

class Doctor:
    def __init__(self, nombre, apellidos, consultorio, correo, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.consultorio = consultorio
        self.correo = correo
        self.password = password
    
    def registrar(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO doctores VALUES(null, %s, %s, %s, %s, %s)"
        doctor = (self.nombre, self.apellidos, self.consultorio, self.correo, cifrado.hexdigest())
        try:
            cursor.execute(sql, doctor)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result 

    def identificar(self):
        sql = "SELECT * FROM doctores WHERE correo = %s AND password = %s"

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) 

        doctor = (self.correo, cifrado.hexdigest())

        cursor.execute(sql, doctor)
        result = cursor.fetchone()
        
        return result
