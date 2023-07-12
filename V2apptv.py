import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from tkinter import simpledialog
import win32print
import win32ui
import tempfile
import os
import win32api
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Missionary Technology")

        # Estilos
        self.estilo = ttk.Style()
        self.estilo.configure("TLabel", font=("Arial", 10), foreground="#333333")
        self.estilo.configure("TButton", font=("Arial", 10), foreground="#000000", background="#007bff")
        self.estilo.configure("Treeview", font=("Arial", 10), background="#ffffff")
        
        # Crear la base de datos y la tabla si no existen
        self.conexion = sqlite3.connect("datos.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS registros (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, run TEXT, direccion TEXT, correo TEXT, num_celular TEXT, n_familiares TEXT, comunidad TEXT)")
        self.conexion.commit()

        # Color fondo
        self.ventana.configure(bg="#d3e9f8")
        
        # Crear los widgets
        self.etiqueta_nombre = ttk.Label(ventana, text="Nombre:")
        self.etiqueta_nombre.pack()
        self.etiqueta_nombre.place(x=10,y=10)

        self.entrada_nombre = ttk.Entry(ventana)
        self.entrada_nombre.pack()
        self.entrada_nombre.place(x=90,y=10, width=200)
        

        
        self.etiqueta_run = ttk.Label(ventana, text="Fecha:")
        self.etiqueta_run.pack()
        self.etiqueta_run.place(x=10,y=40)

        self.entrada_run = ttk.Entry(ventana)
        self.entrada_run.pack()
        self.entrada_run.place(x=90,y=40, width=200)
        
        self.etiqueta_direccion = ttk.Label(ventana, text="Dirección:")
        self.etiqueta_direccion.pack()
        self.etiqueta_direccion.place(x=320,y=10)

        self.entrada_direccion = ttk.Entry(ventana)
        self.entrada_direccion.pack()
        self.entrada_direccion.place(x=400,y=10, width=200)
        
        self.etiqueta_correo = ttk.Label(ventana, text="Individuo:")
        self.etiqueta_correo.pack()
        self.etiqueta_correo.place(x=320,y=40)

        self.entrada_correo = ttk.Entry(ventana)
        self.entrada_correo.pack()
        self.entrada_correo.place(x=400,y=40, width=200)
        
        self.etiqueta_num_celular = ttk.Label(ventana, text="Número de Celular:")
        self.etiqueta_num_celular.pack()
        self.etiqueta_num_celular.place(x=610,y=10)

        self.entrada_num_celular = ttk.Entry(ventana)
        self.entrada_num_celular.pack()
        self.entrada_num_celular.place(x=760,y=10, width=200)
        
        self.etiqueta_n_familiares = ttk.Label(ventana, text="Número de Familiares:")
        self.etiqueta_n_familiares.pack()
        self.etiqueta_n_familiares.place(x=610,y=40)

        self.entrada_n_familiares = ttk.Entry(ventana)
        self.entrada_n_familiares.pack()
        self.entrada_n_familiares.place(x=760,y=40, width=200)
        
        self.etiqueta_comunidad = ttk.Label(ventana, text="Comunidad:")
        self.etiqueta_comunidad.pack()
        self.etiqueta_comunidad.place(x=970,y=10)

        self.entrada_comunidad = ttk.Entry(ventana)
        self.entrada_comunidad.pack()
        self.entrada_comunidad.place(x=1050,y=10, width=200)

        self.boton_agregar = ttk.Button(ventana, text="Agregar", command=self.agregar_registro)
        self.boton_agregar.pack()
        self.boton_agregar.place(x=10, y=80)
        
        self.etiqueta_filtro_comunidad = ttk.Label(ventana, text="Filtro por Comunidad:")
        self.etiqueta_filtro_comunidad.pack()
        self.etiqueta_filtro_comunidad.place(x=110, y=80)

        self.combo_filtro_comunidad = ttk.Combobox(ventana, values=["Divina Providencia", "Sagrado Corazon", "Nuestra Señora Del Rosario", "Cristo Rey", "Cristo Redentor", "San Alberto Hurtado", "Jesús Amigo De Todos", "Maria Madre Admirable", "San Damuian De Molokai", "Jesús Agua Viva"])
        self.combo_filtro_comunidad.pack()
        self.combo_filtro_comunidad.place(x=260, y=80)
        
        self.etiqueta_filtro_correo = ttk.Label(ventana, text="Filtro Natural/Pastoral:")
        self.etiqueta_filtro_correo.pack()
        self.etiqueta_filtro_correo.place(x=110, y=100)

        self.combo_filtro_correo = ttk.Combobox(ventana, values=["Pastoral Social", "Persona Natural"])
        self.combo_filtro_correo.pack()
        self.combo_filtro_correo.place(x=260, y=100)
        
        self.boton_filtrar = ttk.Button(ventana, text="Filtrar", command=self.filtrar_registros)
        self.boton_filtrar.pack()
        self.boton_filtrar.place(x=410, y=80)
        
        self.tabla = ttk.Treeview(ventana, columns=("id", "nombre", "run", "direccion", "correo", "num_celular", "n_familiares", "comunidad"), show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("run", text="Fecha")
        self.tabla.heading("direccion", text="Dirección")
        self.tabla.heading("correo", text="Pastoral/Natural")
        self.tabla.heading("num_celular", text="Num.Celular")
        self.tabla.heading("n_familiares", text="N.Familiares")
        self.tabla.heading("comunidad", text="Comunidad")
        self.tabla.pack(fill=tk.BOTH, expand=True)
        self.tabla.place(x=30, y=150, width=1460, height=600)

        #tamaño de las columnas de la tabla
        self.tabla.column("id", width=0, stretch=tk.NO)
        self.tabla.column("nombre", width=150)
        self.tabla.column("run", width=100)
        self.tabla.column("direccion", width=200)
        self.tabla.column("correo", width=150)
        self.tabla.column("num_celular", width=120)
        self.tabla.column("n_familiares", width=120)
        self.tabla.column("comunidad", width=150)

        #scrollbar
        self.scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollbar.set)
        
        self.boton_modificar = ttk.Button(ventana, text="Modificar", command=self.modificar_registro)
        self.boton_modificar.pack()
        self.boton_modificar.place(x=640,y=80)
        
        self.boton_eliminar = ttk.Button(ventana, text="Eliminar", command=self.eliminar_registro)
        self.boton_eliminar.pack()
        self.boton_eliminar.place(x=790,y=80)
        
        self.boton_imprimir = ttk.Button(ventana, text="DOC", command=self.imprimir_registros)
        self.boton_imprimir.pack()
        self.boton_imprimir.place(x=940,y=80)
        
        # Cargar los registros existentes
        self.cargar_registros()


    def ajustar_tabla(self, event):
        self.tabla.pack_configure(fill=tk.BOTH, expand=True)


    def agregar_registro(self):
        nombre = self.entrada_nombre.get()
        run = self.entrada_run.get()
        direccion = self.entrada_direccion.get()
        correo = self.entrada_correo.get()
        num_celular = self.entrada_num_celular.get()
        n_familiares = self.entrada_n_familiares.get()
        comunidad = self.entrada_comunidad.get()
        
        self.cursor.execute("INSERT INTO registros (nombre, run, direccion, correo, num_celular, n_familiares, comunidad) VALUES (?, ?, ?, ?, ?, ?, ?)", (nombre, run, direccion, correo, num_celular, n_familiares, comunidad))
        self.conexion.commit()
        
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_run.delete(0, tk.END)
        self.entrada_direccion.delete(0, tk.END)
        self.entrada_correo.delete(0, tk.END)
        self.entrada_num_celular.delete(0, tk.END)
        self.entrada_n_familiares.delete(0, tk.END)
        self.entrada_comunidad.delete(0, tk.END)
        
        self.cargar_registros()


    def modificar_registro(self):
        seleccionado = self.tabla.selection()
        if len(seleccionado) > 0:
            registro_id = self.tabla.item(seleccionado)["values"][0]

            # Obtener los valores actuales del registro seleccionado
            valores_actuales = self.tabla.item(seleccionado)["values"]

            # Mostrar cuadros de diálogo para solicitar la nueva información al usuario
            nuevo_nombre = simpledialog.askstring("Modificar registro", "Nuevo nombre:", initialvalue=valores_actuales[1])
            nuevo_run = simpledialog.askstring("Modificar registro", "Nueva Fecha:", initialvalue=valores_actuales[2])
            nueva_direccion = simpledialog.askstring("Modificar registro", "Nueva dirección:", initialvalue=valores_actuales[3])
            nuevo_correo = simpledialog.askstring("Modificar registro", "Tipo Individuo:", initialvalue=valores_actuales[4])
            nuevo_num_celular = simpledialog.askstring("Modificar registro", "Nuevo número de celular:", initialvalue=valores_actuales[5])
            nuevo_n_familiares = simpledialog.askstring("Modificar registro", "Nuevo número de familiares:", initialvalue=valores_actuales[6])
            nueva_comunidad = simpledialog.askstring("Modificar registro", "Nueva comunidad:", initialvalue=valores_actuales[7])

            # Verificar si los campos de entrada están vacíos o si el usuario canceló la modificación
            if nuevo_nombre is None:
                nuevo_nombre = valores_actuales[1]
            if nuevo_run is None:
                nuevo_run = valores_actuales[2]
            if nueva_direccion is None:
                nueva_direccion = valores_actuales[3]
            if nuevo_correo is None:
                nuevo_correo = valores_actuales[4]
            if nuevo_num_celular is None:
                nuevo_num_celular = valores_actuales[5]
            if nuevo_n_familiares is None:
                nuevo_n_familiares = valores_actuales[6]
            if nueva_comunidad is None:
                nueva_comunidad = valores_actuales[7]

            # Actualizar el registro con los nuevos valores
            self.cursor.execute("UPDATE registros SET nombre=?, run=?, direccion=?, correo=?, num_celular=?, n_familiares=?, comunidad=? WHERE id=?", (nuevo_nombre, nuevo_run, nueva_direccion, nuevo_correo, nuevo_num_celular, nuevo_n_familiares, nueva_comunidad, registro_id))
            self.conexion.commit()

            self.cargar_registros()


    def eliminar_registro(self):
        seleccionado = self.tabla.selection()
        if len(seleccionado) > 0:
            registro_id = self.tabla.item(seleccionado)["values"][0]
            
            self.cursor.execute("DELETE FROM registros WHERE id=?", (registro_id,))
            self.conexion.commit()

            self.entrada_nombre.delete(0, tk.END)
            self.entrada_run.delete(0, tk.END)
            self.entrada_direccion.delete(0, tk.END)
            self.entrada_correo.delete(0, tk.END)
            self.entrada_num_celular.delete(0, tk.END)
            self.entrada_n_familiares.delete(0, tk.END)
            self.entrada_comunidad.delete(0, tk.END)
            
            self.cargar_registros()


    def filtrar_registros(self):
        self.tabla.delete(*self.tabla.get_children())

        comunidad_filtro = self.combo_filtro_comunidad.get()
        correo_filtro = self.combo_filtro_correo.get()

        consulta = "SELECT * FROM registros WHERE 1=1"
        parametros = ()

        if comunidad_filtro != "":
            consulta += " AND comunidad LIKE ?"
            parametros += ('%' + comunidad_filtro + '%',)

        if correo_filtro != "":
            consulta += " AND correo LIKE ?"
            parametros += ('%' + correo_filtro + '%',)

        self.cursor.execute(consulta, parametros)
        registros = self.cursor.fetchall()

        for registro in registros:
            self.tabla.insert("", tk.END, values=registro)


    def imprimir_registros(self):
        registros = self.tabla.get_children()

        if registros:
            contenido_impresion = []

            # Obtener los nombres de las columnas
            nombres_columnas = [self.tabla.heading(col)["text"] for col in self.tabla["columns"] if col != "id"]


            # Agregar los nombres de las columnas como primera fila en el contenido de impresión
            contenido_impresion.append(nombres_columnas)

            for registro in registros:
                valores = [self.tabla.item(registro)["values"][col_index] for col_index, col in enumerate(self.tabla["columns"]) if col != "id"]
                contenido_impresion.append(valores)

            # Obtener la ruta absoluta del directorio actual del script
            carpeta_actual = os.path.abspath(os.path.dirname(__file__))

            
            nombre_archivo = os.path.join(carpeta_actual, "archivo.pdf")

            try:
                # Crear el documento PDF
                doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)

                # Crear la tabla con los datos de la tabla
                tabla = Table(contenido_impresion)

                # Estilo de la tabla...

                estilo = TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), '#007bff'),  # Color de fondo del encabezado
                        ('TEXTCOLOR', (0, 0), (-1, 0), '#ffffff'),  # Color de texto del encabezado
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación del contenido
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fuente y estilo del encabezado
                        ('FONTSIZE', (0, 0), (-1, 0), 13),  # Tamaño de fuente del encabezado
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),  # Espaciado inferior del encabezado
                        ('BACKGROUND', (0, 1), (-1, -1), '#f7f7f7'),  # Color de fondo de las filas
                        ('TEXTCOLOR', (0, 1), (-1, -1), '#333333'),  # Color de texto de las filas
                        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Fuente y estilo del contenido
                        ('FONTSIZE', (0, 1), (-1, -1), 7),  # Tamaño de fuente del contenido
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alineación izquierda del contenido
                        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Alineación vertical centrada del contenido
                        ('GRID', (0, 0), (-1, -1), 1, '#cccccc'),  # Líneas de rejilla
                ])

                tabla.setStyle(estilo)

                # Ajustar el tamaño de las columnas según el contenido
                tabla._argW[1] = 70  # Ajustar el tamaño de la primera columna
                tabla.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                           ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Cambiar el color del texto de los encabezados
                                           ('BACKGROUND', (0, 0), (-1, 0), colors.gray),  # Cambiar el color de fondo de los encabezados
                                           ]))

                # Crear la lista de elementos para el documento PDF
                elementos = [tabla]

                # Generar el PDF
                doc.build(elementos)

                print("PDF generado y guardado correctamente.")

            except Exception as e:
                print("Error al generar el PDF:", str(e))

        else:
            print("No hay registros para generar el PDF.")
        

    def cargar_registros(self):
        self.tabla.delete(*self.tabla.get_children())
        
        self.cursor.execute("SELECT * FROM registros")
        registros = self.cursor.fetchall()
        
        for registro in registros:
            self.tabla.insert("", tk.END, values=registro)

        # Actualizar la barra de desplazamiento
        self.tabla.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.tabla.yview)
        

ventana = tk.Tk()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
app = Aplicacion(ventana)
ventana.mainloop()
