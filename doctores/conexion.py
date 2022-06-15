import mysql.connector

def conect():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "ihc_scm",
    )
    cursor = database.cursor(buffered = True)
    return [database, cursor]
