import tkinter as tk
from tkinter import filedialog
import os

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        nombre_archivo = os.path.basename(archivo)
        etiqueta_archivo.config(text="Archivo seleccionado: " + nombre_archivo)
        mostrar_contenido(archivo)

def mostrar_contenido(archivo):
    try:
        with open(archivo, 'r') as file:
            contenido = file.read()
            panel_lectura.delete("1.0", tk.END)  # Limpiar el contenido existente
            panel_lectura.insert(tk.END, contenido)
    except Exception as e:
        print("Error al leer el archivo:", str(e))

def validar_repetidos():
    contenido = panel_lectura.get("1.0", tk.END)
    lineas = contenido.split('\n')
    objetos = set()

    for i, linea in enumerate(lineas):
        # Ignorar líneas vacías
        if not linea.strip():
            continue    

        # Ignorar líneas con "--> PLUGINS \PreliminardeCobro"
        if "--> PLUGINS \\PreliminardeCobro" in linea:
            continue

        # Ignorar líneas con "EXISTENTES:"
        if "--> CUERPO DE VARIABLES" in linea or "--> PLUGINS/ReporteEscaneoInventario" in linea or "IntelisisTmp" in linea or "MODIFICADOS" in linea or "ServicioAndroid:"in linea or "--> SQL" in linea or "OBJETOS CONTENIDOS" in linea or "-------------------------------------------------------" in linea or "EXISTENTES:" in linea or "--> SDK" in linea or "--> TITULO" in linea or "NUEVOS:" in linea or "MODIFICADOS:" in linea or "A INTEGRAR:" in linea or "A INTEGRAR MODIFICADO:" in linea or "A ELIMIMAR:" in linea or "NUEVAS:" in linea or "MODIFICADAS:" in linea or "A ELIMINAR:" in linea or "--> VARIABLES" in linea or "--> VARIABLES(CUERPO)" in linea:
            continue

        extensiones_validas = [".sql",".dll", ".Data.xml", ".exe.config", ".Data.dll", ".exe", ".dlg",".Data.xml"]
        if not any(linea.endswith(extension) for extension in extensiones_validas) or linea in objetos:
            panel_lectura.tag_add("rojo", f"{i + 1}.0", f"{i + 1}.end")
        else:
            objetos.add(linea)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Input File con Tkinter")
ventana.geometry("800x400")  # Ajustar el tamaño de la ventana

# Frame para la parte izquierda (botón, etiqueta y validación)
frame_izquierda = tk.Frame(ventana)
frame_izquierda.pack(side=tk.LEFT, padx=20, pady=20)

# Botón para abrir el cuadro de diálogo
boton_seleccionar = tk.Button(frame_izquierda, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack(pady=10)

# Etiqueta para mostrar el nombre del archivo seleccionado
etiqueta_archivo = tk.Label(frame_izquierda, text="Ningún archivo seleccionado")
etiqueta_archivo.pack()

# Botón de validación
boton_validar = tk.Button(frame_izquierda, text="Validar", command=validar_repetidos)
boton_validar.pack(pady=10)

# Frame para la parte derecha (panel de lectura)
frame_derecha = tk.Frame(ventana)
frame_derecha.pack(side=tk.RIGHT, padx=5, pady=5)

# Panel de lectura para mostrar el contenido del archivo
panel_lectura = tk.Text(frame_derecha, wrap="word", height=100, width=100)
panel_lectura.pack()

# Configuración del tag para resaltar en rojo
panel_lectura.tag_configure("rojo", foreground="red")

# Iniciar el bucle principal
ventana.mainloop()
