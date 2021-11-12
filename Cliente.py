#Abigail Chávez
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

class Cliente(tk.Frame):
    #Constructor
    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
    def __str__(self):
        return "ID: "+self.id+" Nombre: "+self.nombre+" Teléfono: "+self.telefono
    #listClientes.insert(0, )
    #listClientes.place(x=100, y=120)

if __name__ == '__main__':
    #VENTANA
    ventana = Tk()
    ventana.geometry("470x450+0+0")
    ventana.config(bg = "white")
    ventana.title("Lista de clientes")
    lblTitulo = Label(ventana, text="REGISTRO DE CLIENTES", bg="white", fg="#EACFBE", font="Helvetica 15 bold")
    lblTitulo.place(x=115, y=40)

    #Tabla
    tabla = ttk.Treeview(ventana, columns = ("1", "2"), height=10, selectmode="extended")
    tabla.heading("#0", text="ID")
    tabla.heading("#1", text="NOMBRE")
    tabla.heading("#2", text="TELEFONO")
    tabla.column("#0", stretch= tk.NO, width=50)
    tabla.column("#1", stretch=tk.NO, width=110)
    tabla.column("#2", stretch=tk.NO, width=110)
    tabla.grid(row=0, column=0, columnspan=2, padx=8, pady=8)
    tabla.place(x=100, y=125)

    #VENTANA AÑADIR
    def ventanaA():
        ventanaA = Toplevel(ventana)
        ventanaA.title("Añadir cliente")
        ventanaA.geometry("300x250")
        ventanaA.config(bg="white")

        #LABEL
        Label(ventanaA, text="AÑADIR CLIENTE", font="Helvetica 12 bold", bg="white", fg="#EACFBE").place(x=85, y= 20)
        lblID = Label(ventanaA, text="ID: ", font="Helvetica 10 bold", bg="white", fg="#EACFBE").place(x=70, y=60)
        lblnombre=Label(ventanaA, text= "Nombre: ", font="Helvetica 10 bold", bg="white", fg="#EACFBE").place(x=34, y=90)
        lblTlf = Label(ventanaA, text="Telefono: ", font="Helvetica 10 bold", bg="white", fg="#EACFBE").place(x=28, y=120)

        # TextFields
        id = ttk.Entry(ventanaA)
        id.place(x=93, y=63)
        nombre = ttk.Entry(ventanaA)
        nombre.place(x=93, y=93)
        tlf = ttk.Entry(ventanaA)
        tlf.place(x=93, y=123)

        # BOTONES
        # Método cerrar ventana.
        def cerrarA():
            ventanaA.destroy()
        #Método insertar cliente
        def insertar():
            try:
                Label(ventanaA, text="EL CLIENTE YA EXISTE", font="Helvetica 10 bold", bg="white", fg="white").place(x=80, y=155)
                Label(ventanaA, text="CLIENTE "+ str(id.get())+ " AÑADIDO", font="Helvetica 10 bold", bg="white", fg="#EACFBE").place(x=80, y=155)
                tabla.insert("", "end", text=id.get(), values=(nombre.get(), tlf.get()), iid=id.get())
            except:
                Label(ventanaA, text="EL CLIENTE YA EXISTE", font="Helvetica 10 bold", bg="white", fg="#EACFBE").place(x=80, y=155)

        andir = Button(ventanaA, text="Añadir", bg="#EACFBE", fg="grey", font="Helvetica 10 bold" ,command= insertar).place(x=190, y=190)
        cancelar = Button(ventanaA, text="Cancelar", bg="#EACFBE", fg="grey", font="Helvetica 10 bold" ,command=cerrarA).place(x=43, y=190)
        ventanaA.mainloop()

    #MÉTODO MODIFICAR
    def ventanaMod():
        ventanaMod = Toplevel(ventana)
        ventanaMod.title("Modificar datos")
        ventanaMod.geometry("300x250")
        ventanaMod.config(bg="white")

        # LABEL
        Label(ventanaMod, text="MODIFICAR DATOS", font="Helvetica 12 bold", bg="white", fg="#EACFBE").place(x=85, y=20)
        lblID = Label(ventanaMod, text="ID: ", font="Helvetica 10 bold", bg="white", fg="#EACFBE").place(x=70, y=60)
        lblnombre = Label(ventanaMod, text="Nombre: ", font="Helvetica 10 bold", bg="white", fg="#EACFBE").place(x=34, y=90)
        lblTlf = Label(ventanaMod, text="Telefono: ", font="Helvetica 10 bold", bg="white", fg="#EACFBE").place(x=28, y=120)

        # TextFields
        id = ttk.Entry(ventanaMod)
        id.place(x=93, y=63)
        nombre = ttk.Entry(ventanaMod)
        nombre.place(x=93, y=93)
        tlf = ttk.Entry(ventanaMod)
        tlf.place(x=93, y=123)

        def cerrarMod():
            ventanaMod.destroy()

        def modificar():
            try:
                mod = tabla.selection()[0] #item seleccionado
                tabla.item(mod, text=id.get(), values=(nombre.get(), tlf.get())) #CAMBIO DE DATOS
            except:
                Label(ventanaMod, text="SELECCIONA UN REGISTRO PARA MODIFICAR")

        modif = Button(ventanaMod, text="Aceptar",  bg="#EACFBE", fg="grey", font="Helvetica 10 bold",command=modificar).place(x=190, y=170)
        cancelar = Button(ventanaMod, text="Cancelar",  bg="#EACFBE", fg="grey", font="Helvetica 10 bold",command=cerrarMod).place(x=43, y=170)
        ventanaMod.mainloop()


    #Método borrar
    def borrarItem():
        try:
            Label(ventana, text="SELECCIONA UN REGISTRO PARA BORRAR", bg="white", fg="white",font="Helvetica 8 bold").place(x=100, y=80)
            item = tabla.selection()[0] #Item seleccionado
            tabla.delete(item)
        except:
            Label(ventana, text="SELECCIONA UN REGISTRO PARA BORRAR", bg="#EACFBE", fg="grey", font="Helvetica 8 bold").place(x=100, y=80)

    #Método buscar
    def buscarItem():
        #VENTANA BUSCAR
        ventanaBuscar = Toplevel(ventana)
        ventanaBuscar.title("Modificar datos")
        ventanaBuscar.geometry("300x200")
        ventanaBuscar.config(bg="white")

        benc = ttk.Entry(ventanaBuscar)
        benc.place(x=125, y=60)

        Label(ventanaBuscar, text="BUSCAR", font="Helvetica 12 bold", bg="white", fg="#EACFBE").place(x=120, y=10)
        Label(ventanaBuscar, text="Ingrese ID: ", font="Helvetica 10 bold", bg="white", fg="#EACFBE").place(x=45, y=60)

        def cerrarBusc():
            ventanaBuscar.destroy()
        def busqueda():
            try:
                compr=int(benc.get())
                clnt= tabla.item(compr, option="values") #Obtenemos datos de búsqueda
                inf = "Cliente " +str(compr)+ " : "+str(clnt)
                Label(ventanaBuscar, text=inf, bg="white", fg="#EACFBE", font="Helvetica 10 bold").place(x=40, y=100)
            except:
                Label(ventanaBuscar, text="  EL CLIENTE NO EXISTE  ", bg="white", fg="#EACFBE", font="Helvetica 12 bold").place(x=40, y=100)

        cancel = Button(ventanaBuscar, text="Cancelar", bg="#EACFBE", fg="grey", font="Helvetica 10 bold",
                        command=cerrarBusc).place(x=43, y=140)
        bbuscar = Button(ventanaBuscar, text="Buscar", bg="#EACFBE", fg="grey", font="Helvetica 10 bold",
                         command=busqueda).place(x=190, y=140)

        ventanaBuscar.mainloop()


    #GUARDAR TABLA COMO FICHERO
    def guardarTxt():
        registros = ""
        for fila in tabla.get_children(): #RECORRE TABLA #EXTRAE TEXT Y VALUES
            contenido1 = tabla.item(fila, option="text")
            contenido2=tabla.item(fila, option="values")
            contenido = "CLIENTE " +str(contenido1)+ " : " +str(contenido2)+"\n"
            registros= registros+""+contenido
            fichero = open('Clientes.txt', 'w')  # ESCRIBE EN EL FICHERO(ABRE FICHERO)
            fichero.writelines(registros)  # ESCRIBE EN EL FICHERO
            fichero.close() #CIERRA FICHERO

    #BOTONES
    aniadir = Button(ventana, text = "Añadir", bg="#EACFBE", fg="grey", font="Helvetica 10 bold", height= 1, width=8, command=ventanaA).place(x=98, y=100)
    mod = Button(ventana, text="Modificar", bg="#EACFBE", fg="grey", font="Helvetica 10 bold", command=ventanaMod).place(x=170, y=100)
    borrar= Button(ventana, text="Borrar", bg="#EACFBE", fg="grey", font="Helvetica 10 bold",height= 1, width=8, command=borrarItem).place(x=241, y=100)
    buscar= Button(ventana, text="Buscar", bg="#EACFBE", fg="grey", font="Helvetica 10 bold", width=6,command=buscarItem).place(x=315, y=100)
    guardar = Button(ventana, text="Guardar", bg="#EACFBE", fg="grey", font="Helvetica 10 bold", command=guardarTxt).place(x=200, y=370)
    ventana.mainloop()