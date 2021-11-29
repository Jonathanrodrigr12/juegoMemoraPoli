from project.utilidad.ventana.ventana import Ventana
from project.iniciarJuego.moduloJuego.modulosJuego import ModulosJuego
from tkinter import *

'''
Clase donde se inicializa la ventana de bienvenida del juego
'''
class PantallaInicial(Ventana):
    
    '''
    Constructor donde se incializa las clases y propiedades para la creación del tercer nivel
    '''
    def __init__(self):
        super().__init__("855x483")
        self.imagen = PhotoImage(file="./images/background/pantallaInicial/Memora.gif")
        Label(self.ventana, image=self.imagen).place(x=0,y=0)
        Button(self.ventana, text="Start",command=self.iniciar_niveles,
        font=("lucida calligraphy",13),background="navajowhite").place(x=710,y=280)
        Button(self.ventana,text="Instructions",command=self.mostrar_instrucciones,
        font=("lucida calligraphy",11),background="navajowhite").place(x=699,y=365)

    '''
    Función la cual da lugar al inicio del juego
    '''
    def iniciar_niveles(self):
        self.ventana.destroy()
        ModulosJuego().crear_venta()

    '''
    Función la mostrara las instrucciones
    '''
    def mostrar_instrucciones(self):
        print("sigue las instrucciones")  