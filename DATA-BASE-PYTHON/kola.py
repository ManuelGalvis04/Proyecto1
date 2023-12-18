import mysql.connector
import datetime
import pandas as pd

def main():
    fechaUM = input("Ingrese la fecha del mantenimiento del equipo: ")
    data= pd.read_excel("data.xlsx")
    fech = datetime.datetime.strptime(fechaUM, '%Y-%m-%d')
    dia_delta = datetime.timedelta(days=181)
    fecha_Mant = fech + dia_delta
    
    serialBus = fechaUM

    resultado = data[data["fecUMCBF"] == serialBus]

    if not resultado.empty:
        for i in resultado.index:
            resultado.fecUMCBF[i] = fecha_Mant #fecUMCBF se le va a agregar al resultado recorriendo la i.
        print(resultado[["srCBF", "ID", "PACIENTE", "DIRECCION", "MUNICIPIO", "TELEFONO", "fecUMCBF"]])
        
        lista_resultante = data.values.tolist()
        lisDataequipo = []
        data_2 = ("cod", "srCAF")
        for i in data_2:
            if(i == "cod"):
                cursor.execute("SELECT * FROM equipo")
                for registro in cursor:
                    print(registro)
            lisDataequipo.append(registro)
        lisDataequipo.append(fecha_Mant)
 
        sql = "INSERT INTO equipo (cod,srCAF,fecUMCBF) VALUES(%s, %s, %s)"
        cursor.execute(sql, tuple(lisDataequipo))
        conexion.commit()

        # sql = "UPDATE equipo SET cod = %s , srCAF = %s, fecUMCBF = %s"
        # cursor.execute(sql, tuple(lisDataequipo))
        # conexion.commit()
    
        lisData = []
        for fila in range(len(lista_resultante)):
            print(fila)
        data_1 = ("Departamento","Municipio", "Tipo", "Id", "Paciente", "Telefono", "Direccion", "cod_equipo")
        for i in data_1:
            cursor.execute("SELECT * FROM usuario")
            if(i=="Id"):
                for registro in cursor:
                    lisData.append(registro)
            lisData.append(input(f"Ingrese el {i}: "))
        lisData.append(serialBus)
        

        sql = "INSERT INTO usuario (Departamento, Municipio, Tipo, Id, Paciente, Telefono, Direccion, cod_equipo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(lisData))
        conexion.commit()

    else:
        print(f"El equipo con el serial {serialBus} no se encontró en la tabla de Excel.")

if __name__ == "__main__":
    conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="dbclinica_mantenimiento")
    cursor=conexion.cursor()
    main()
    
def insertequipo():
        lisDataequipo = []
        data_2 = ("cod", "srCAF", "fecUMCBF")
        for i in data_2:
            cursor.execute("SELECT * FROM equipo")
            for registros in cursor:
                print(registros)
            lisDataequipo.append(i)
                # lisData[0] = None

        sql = "INSERT INTO equipo (cod , srCAF, fecUMCBF) VALUES (%s,%s,%s)"
        cursor.execute(sql, tuple(lisDataequipo))
        conexion.commit()
    