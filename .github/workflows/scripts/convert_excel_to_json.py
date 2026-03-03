import pandas as pd
import json
import os

def cargar_excel():
    ruta_data = 'data/'
    archivos = {
        'clientes': 'Lista_Clientes.xlsx',
        'divisa': 'Divisa.xlsx',
        'categoria': 'Categoría.xlsx',
        'sector': 'Sector.xlsx',
        'zona': 'Zona.xlsx'
    }
    
    resultado = {}

    for clave, nombre in archivos.items():
        ruta_completa = os.path.join(ruta_data, nombre)
        if os.path.exists(ruta_completa):
            # Lee desde la fila 3 (índice 2) porque las primeras son títulos
            df = pd.read_excel(ruta_completa, skiprows=2)
            resultado[clave] = df.to_dict(orient='records')
        else:
            print(f"Advertencia: No se encontró {nombre}")

    # Guarda el resultado en un JSON
    with open('data/datos_consolidados.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=4, ensure_ascii=False)
    
    print("¡Datos convertidos con éxito!")

if __name__ == "__main__":
    cargar_excel()
