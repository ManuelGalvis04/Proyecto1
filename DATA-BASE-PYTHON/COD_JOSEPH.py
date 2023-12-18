import pandas as pd
import mysql.connector

class equipo:

  def _init_(self):
    self.fechaUM = input("Ingrese la fecha del Matenimiento del Equipo: ")
    self.mesAumentar = input("Ingrese los meses para el siguiente mantenimiento: ")

def aumentoFecha(fecha,mesAumentar):
  dia = fecha[8:10]
  mes = fecha[5:7]
  año = fecha[0:4]
  mesNuevo = int(mes) + int(mesAumentar)

  if mesNuevo > 12 :
    mesNuevo = (mesNuevo - 12)
  dia = int(dia) - 1
  año = int(año) + 1
  if mesNuevo < 10:
    mesNuevo = f"0{mesNuevo}"
  if dia < 10:
    dia = f"0{dia}"

  fechaNueva = f"{año}-{mesNuevo}-{dia}"

  return fechaNueva
  
def main():
  maquina = equipo()
  data = pd.read_excel("data.xlsx")
  serial = maquina.fechaUM
  mesAumentar = maquina.mesAumentar
  fechaUM = maquina.fechaUM
  
  fecNueva = aumentoFecha(fechaUM,mesAumentar)
  print(fecNueva)

  resultado = data[data["FechaUCAF"] == serial]

  if not resultado.empty:
    for i in resultado.index:
      resultado.FechaUCAF[i] = fecNueva
    print(resultado[["srCAF", "ID", "PACIENTE", "DIRECCION", "MUNICIPIO", "TELEFONO", "FechaUCAF"]])

    df=resultado[["srCAF", "ID", "PACIENTE", "DIRECCION", "MUNICIPIO", "TELEFONO", "FechaUCAF"]]
    lista= df.to_numpy().tolist()
    #print(lista)
    
    for fila in range(len(lista)):
        listaUsuario=[]
        listaEquipo=[]
        listaEquipo.append(fila+1)
        for columna in range(len(lista[fila])):
          serial=str(lista[fila][0])
                  
          
          if(columna==0 or columna==6):
            
            if(columna==0 and len(str(lista[fila][columna]))<4):
              nuevoSerial=input(f"El serial del equipo fila #{fila+1}, está vacio!!\nDIGITE SERIAL DEL EQUIPO: ")
              listaEquipo.append(nuevoSerial)
            else: listaEquipo.append(str(lista[fila][columna]))
          else: listaUsuario.append(lista[fila][columna])

        #print(lista)
        #print(listaUsuario)
        #print(listaEquipo)
        listaEquipo[0] = None
        listae = []

        consulta = "Select * from equipo"
        equipos.execute(consulta)
        for registro in equipos:
          listae.append(registro)
        print(listae)
        temp = listae[0]
        temp1 = listae[1]
        listae[2] = listae[1]
        listae[2] = temp
        listae[0] = temp1

        print(listae)
        if listae == []:
          sql = "Insert into equipo (cod,srCAF, FechaUCAF) values (%s,%s,%s)"
          cursor.execute(sql, tuple(listaEquipo))
          conexion.commit()
        else: 
          sql = "UPDATE equipo SET srCAF = %s, FechaUCAF = %s WHERE cod= %s"
          cursor.execute(sql, tuple(listae))
          conexion.commit()
        
        listaUsuario.append(fila+1)  
        sql = "Insert into usuario(Id, Paciente,Direccion, Municipio,Telefono, cod_equipo) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(listaUsuario))
        conexion.commit() 
    print("FUE ALMACENADO LOS REGISTROS EN LA BASE DE DATOS CON NUEVA FECHA DE MANTENIMIENTO!!")  

if __name__ == "__main__":
    conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="dbclinica_mantenimiento")
    cursor=conexion.cursor()
    equipos = conexion.cursor()
    main()
 
  
