import mysql.connector

def menu():
  print("*"*34)
  print("*  \tSportsman's Management   \t *")
  print("*"*34)
  print("* 1. Show Sportsman's  \t\t *")
  print("* 2. Insert Sportsman  \t\t *")
  print("* 3. Show Sportsman \t\t *")
  print("* 4. Update Sportsman \t\t *")
  print("* 5. Delete Sportsman \t\t *")
  print("* 6. Exit \t\t\t *")
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
  cursor.execute("SELECT * FROM deportista")

  for registro in cursor:
    print(registro)

def showReader():
  codReader = []
  codReader.append(input("Input the code Sportsman: "))
  cursor.execute("SELECT * FROM deportista WHERE codDeportista = %s", tuple(codReader))

  for registro in cursor:
    print(registro)

  conexion.commit()


def insertReader():
  lisData = []
  data = ("identification", "names", "direction", "movil phone", "program code", "sex", "birthday day")
  for i in data:
    if(i == "program code"):
      cursor.execute("SELECT * FROM deporte")
      for registro in cursor:
        print(registro)
    lisData.append(input(f"Input the {i} of Sportsman: "))

  sql="INSERT INTO deportista (identificacion, nombres, direccion, telefono, codDeporte, sexo, fechNac) VALUES (%s,%s,%s,%s,%s,%s,%s)"
  cursor.execute(sql,tuple(lisData))
  conexion.commit()
  

def updateReader():
  codReader = input("Input the code Sportsman to update: ")
  lisData = []
  data = ("identification", "name", "direction", "movil phone", "program code", "sex", "birthday day")
  for i in data:
    if(i == "program code"):
      cursor.execute("SELECT * FROM deporte")
      for registro in cursor:
        print(registro)
    lisData.append(input(f"Input the new {i} of SportsMan: "))
  lisData.append(codReader)

  sql = "UPDATE deportista SET identificacion = %s, nombres = %s, direccion = %s, telefono = %s, codDeporte = %s, sexo = %s, fechNac = %s WHERE codDeportista = %s"
  cursor.execute(sql, tuple(lisData))
  conexion.commit()

def deleteReader():
  codReader = []
  codReader.append(input("Input the code Sportsman to delete: "))
  
  sql = "DELETE FROM deportista WHERE codDeportista = %s"
  cursor.execute(sql, tuple(codReader))
  conexion.commit()

def main():
  op = menu()
  if(op == 1):
    showReaders()
  elif(op == 2):
    insertReader()
  elif(op == 3):
    showReader()
  elif(op == 4):
    updateReader()
  elif(op == 5):
    deleteReader()
  elif(op == 6):
    return 0
  else:
    print("Invalid Option, try again")

  return main()

if __name__ == "__main__":
  conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="deportista_bd")
  cursor=conexion.cursor()
  main()