import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(['python', ruta_script], check=True)
        else:  # Linux/macOS
            subprocess.run(['python3', ruta_script], check=True)
    except Exception as e:
        print(f"Error al ejecutar el código: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    unidades = {'1': 'Unidad 1', '2': 'Unidad 2', '3': 'Unidad 3'}
    
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        for key, nombre in unidades.items():
            print(f"{key} - {nombre}")
        print("0 - Salir")
        
        eleccion = input("Elige una unidad o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo...")
            break
        elif eleccion in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion]))
        else:
            print("Opción no válida.")

def mostrar_sub_menu(ruta_unidad):
    if not os.path.exists(ruta_unidad):
        print("Unidad no encontrada.")
        return
    
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
    while True:
        print("\n=== SUBMENÚ ===")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Volver")
        
        eleccion = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion == '0':
            break
        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[idx]))
        except ValueError:
            print("Entrada no válida.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
    while True:
        print("\n=== SCRIPTS ===")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Volver")
        
        eleccion = input("Elige un script o '0' para regresar: ")
        if eleccion == '0':
            break
        try:
            idx = int(eleccion) - 1
            if 0 <= idx < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[idx])
                mostrar_codigo(ruta_script)
                if input("¿Ejecutar? (s/n): ").lower() == 's':
                    ejecutar_codigo(ruta_script)
        except ValueError:
            print("Entrada no válida.")

if __name__ == "__main__":
    mostrar_menu()
