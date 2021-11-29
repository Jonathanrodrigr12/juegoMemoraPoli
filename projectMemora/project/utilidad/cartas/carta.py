from tkinter import *

'''
Clase Carta donde se realiza la definición de las funciones y propiedades
que ayudan a realizar creación de las cartas para el juego memora
'''
class Carta:
    
    '''
    Constructor donde se incializa las clases y propiedades para la creación de las cartas
    '''
    def __init__(self, path:str):
        self.valor = 0
        self.posicon = 0
        self.oculto = True
        self.foto = PhotoImage(file=path)
