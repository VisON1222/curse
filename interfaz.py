from tkinter import *
import tkinter.messagebox

class PrimerGUI(Tk):
    def __init__(self):
        super().__init__() #llama al constructor de la clase padre
        self.title("Encuesta de satisfaccion del curso Python")
        self.geometry("420x620+30+30")

        #------------
        #PREGUNTA1
        #------------
        self.pregunta1 = IntVar() #variable para el grupo de esta pregunta
        self.etiqueta1 = (Label(self, text="¿Estas satisfecho con el contenido del curso Python?")).place(x=15,y=30)
        self.botonP1Uno = Radiobutton(self,text="1", value=1, variable=self.pregunta1).place(x=75,y=50)
        self.botonP1Dos = Radiobutton(self, text="2", value=2, variable=self.pregunta1).place(x=140,y=50)
        self.botonP1Tres = Radiobutton(self, text="3", value=3, variable=self.pregunta1).place(x=195,y=50)
        self.botonP1Cuatro = Radiobutton(self, text="4", value=4, variable=self.pregunta1).place(x=250,y=50)
        self.botonP1Cinco = Radiobutton(self, text="5", value=5, variable=self.pregunta1).place(x=310,y=50)
        # ------------
        # PREGUNTA2
        # ------------
        self.pregunta2 = IntVar()  # variable para el grupo de esta pregunta
        self.etiqueta2 = (Label(self, text="¿Recomendaria el curso a otros compañeros?")).place(x=15, y=80)
        self.botonP2Uno = Radiobutton(self, text="1", value=1, variable=self.pregunta2).place(x=75, y=110)
        self.botonP2Dos = Radiobutton(self, text="2", value=2, variable=self.pregunta2).place(x=140, y=110)
        self.botonP2Tres = Radiobutton(self, text="3", value=3, variable=self.pregunta2).place(x=195, y=110)
        self.botonP2Cuatro = Radiobutton(self, text="4", value=4, variable=self.pregunta2).place(x=250, y=110)
        self.botonP2Cinco = Radiobutton(self, text="5", value=5, variable=self.pregunta2).place(x=310, y=110)
        # ------------
        # PREGUNTA3
        # ------------
        self.pregunta3 = IntVar()  # variable para el grupo de esta pregunta
        self.etiqueta3 = (Label(self, text="¿Le ha parecido adecuado el material y contenido del curso?")).place(x=15, y=140)
        self.botonP3Uno = Radiobutton(self, text="1", value=1, variable=self.pregunta3).place(x=75, y=170)
        self.botonP3Dos = Radiobutton(self, text="2", value=2, variable=self.pregunta3).place(x=140, y=170)
        self.botonP3Tres = Radiobutton(self, text="3", value=3, variable=self.pregunta3).place(x=195, y=170)
        self.botonP3Cuatro = Radiobutton(self, text="4", value=4, variable=self.pregunta3).place(x=250, y=170)
        self.botonP3Cinco = Radiobutton(self, text="5", value=5, variable=self.pregunta3).place(x=310, y=170)
        # ------------
        # PREGUNTA4
        # ------------
        self.etiquetaTextoObservaciones = Label(self, text="Observaciones sobre material, aulas, profesores...").place(x=15, y=200)
        self.campo_observaciones =  Text(self, width=45, height=10)
        self.campo_observaciones.place(x=15, y=230)

        # ------------
        # PREGUNTA5
        # ------------
        self.nombre = StringVar()
        self.apellidos = StringVar()
        self.subdireccion = StringVar()
        self.etiquetaTextoInputs = Label(self, text="Introduzca, si lo desea, sus datos personales").place(x=15, y=400)
        self.etiquetaInput1 = Label(self, text="Nombre").place(x=15, y=430)
        self.nombreInput = Entry(self, textvariable=self.nombre).place(x=100, y=430)
        self.etiquetaInput2 = Label(self, text="Apellidos").place(x=15, y=460)
        self.apellidosInput = Entry(self, textvariable=self.apellidos).place(x=100, y=460)
        self.etiquetaInput3 = Label(self, text="Subdireccion").place(x=15, y=490)
        self.subdireccionInput = Entry(self, textvariable=self.subdireccion).place(x=100, y=490)

        # ------------
        # BOTON
        # ------------
        self.boton = Button(self, text="Enviar comentarios", command=self.enviar).place(x=100, y=520)

    def obtener_valor1(self):
        #valor = self.pregunta1.get()
        #print(f"El valor 1 es {valor}")
        return self.pregunta1.get()

    def obtener_valor2(self):
        #valor = self.pregunta2.get()
        #print(f"El valor 2 es {valor}")
        return self.pregunta2.get()

    def obtener_valor3(self):
        #valor = self.pregunta3.get()
        #print(f"El valor 3 es {valor}")
        return self.pregunta3.get()

    def obtener_observaciones(self):
        return self.campo_observaciones.get("1.0", END) #desde la linea 1 caracter 0 hasta el final del texto

    def enviar(self):
        tkinter.messagebox.showinfo("Gracias por su tiempo","Gracias por su asistencia "+self.nombre.get()+" "+self.apellidos.get()+". Su valoracion media del curso es "+ str((self.obtener_valor1()+self.obtener_valor2()+self.obtener_valor3())/3)+"\n Observaciones: "+self.obtener_observaciones())

#Creación de una ventana:
ventana = PrimerGUI()
ventana.mainloop() #para mantener la ventana abierta
