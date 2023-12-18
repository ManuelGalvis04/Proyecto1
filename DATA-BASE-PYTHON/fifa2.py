import mysql.connector

def menu():
    print("*"*34)
    print("* \tReader's Management\t*")
    print("*"*34)
    print("*1. Show Reader's \t\t*")
    print("*2. Insert Reader \t\t*")
    print("*3. Show Reader \t\t*")
    print("*4. Update Reader \t\t*")
    print("*5. Delete Reader \t\t*")
    print("*6. Exit \t\t\t*")
    print("*"*34)
    return inputInteger("Select an Option: ")

def inputInteger(message):
    try:
        integer = int(input(message))
        return integer
    except ValueError:
        print("Error, input an Integer Value!")
        return inputInteger(message)

def showReaders():
    cursor.execute("SELECT * FROM lector") 
    
    for registro in cursor:
        print(registro)  

def insertReader():
    tupla = ("identification", "name", "address", "phone number", "codCarrera", "sex", "birthdate")
    val = []

    for i in tupla:
        if (i == "codCarrera"):
            cursor.execute("SELECT * FROM carrera")
            for registro in cursor:
                print(registro)
        elif (i == "sex"):
            print(" 1. Masculino\n 2. Femenino.")

        val.append(input(f"imput the {i} of Reader: "))
        
    sql="INSERT INTO lector (identificacion, nombre, direccion, telefono, codCarrera, sexo, fechaNac) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,tuple(val))
    conexion.commit()

def Option3():
    ID = input("Type the ID you wish to consult: ")
    cursor.execute(f"SELECT * FROM lector WHERE identificacion = {ID}")
    for registro in cursor:
        print(registro)

def UpdateReader():
    ID = input("Type the ID you wish to consult: ")
    cursor.execute(f"SELECT * FROM lector WHERE identificacion = {ID}")
    result = cursor.fetchall()
    for i in result:
        print(i)

    Campo = int(input("1. Identificacion\n 2. Nombre\n 3. Dirección\n 4. Telefono\n 5. codCarrera\n 6. Sexo\n 7. fechaNac\n Digite el campo que desea actualizar: "))
    if (Campo==1):
        NewReader = input("Ingrese la nueva identificación: ")
        cursor.execute(f"UPDATE lector SET identificacion = {NewReader} WHERE identificacion ={ID}")
        for i in cursor:
            print(i)
        conexion.commit()
    
    elif (Campo==2):
        oldName = input("Escriba el nombre que quieres reemplazar: ")
        newName = input("Ingrese el nuevo nombre: ")

        cursor.execute("UPDATE lector SET nombre = %s WHERE nombre = %s")
        for i in cursor:
            print(i)
        conexion.commit()



def main():
    op = menu()
    if(op == 1):
        showReaders()
    elif(op == 2):
        insertReader()
    elif(op == 3):
        Option3()
    elif(op == 4):
        UpdateReader()
    elif(op == 5):
        print("Option five!")
    elif(op == 6):
        return 0
    else:
        print("Invalid Option, try again.")
    return main()

if __name__ == "__main__":
    conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="bdprestamo")
    cursor=conexion.cursor()
    main()
    

