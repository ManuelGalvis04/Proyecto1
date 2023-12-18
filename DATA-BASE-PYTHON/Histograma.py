import pandas as pd

data = pd.read_excel('data.xlsx')
serial = "2023-07-06"
serial_buscado = serial

resultado = data[data["fecUMCBF"] == serial_buscado]
if not resultado.empty:
    print("El equipo se encontró en la tabla de Excel:")

    for i in resultado.index:
        resultado.fecUMCBF[i]="2024-01-07"
        fech= resultado[["serial_CAF", "ID", "fecUMCBF"]]
    print(fech)
    df = pd.DataFrame(data, columns=[fech])
    df.to_excel("data.xlsx", index=False)
else:
    print(f"El equipo con el serial {serial_buscado} no se encontró en la tabla de Excel.")