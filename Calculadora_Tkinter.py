import sys
import tkinter as tk
from tkinter import messagebox, Menu


class Calculadora(tk.Tk):
    """Instanciamos"""
    def __init__(self):
        super().__init__()
        self.geometry('340x380')
        self.resizable(0, 0)
        self.title('Calculadora')
        #self.iconbitmap('Calculadora.ico')
        self.config(background='aquamarine')
        # Atributos de clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        # StringVar Lo utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # Creamos Menu
        self._crear_menu()
        # Creamos componentes
        self._creacion_componentes()

    """METODOS DE CLASE"""

    '''Metodo crear Menu'''
    def _crear_menu(self):
        menu_principal = Menu(self)
        submenu_archivo = Menu(menu_principal, tearoff=0)
        submenu_archivo.add_command(label='Borrar', command=self._evento_limpiar)
        submenu_archivo.add_separator()
        submenu_archivo.add_command(label='Salir', command=self._salir)
        menu_principal.add_cascade(menu=submenu_archivo, label='Ver')
        submenu_ayuda = Menu(menu_principal, tearoff=0)
        submenu_ayuda.add_command(label='Acerca De', command=self._acerca_de)
        menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
        self.config(menu=menu_principal)

    '''Metodo crear Componentes'''
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=150, bg='aquamarine')
        entrada_frame.pack(side=tk.TOP)
        # Caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'),
                           textvariable=self.entrada_texto, width=25, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, columnspan=4, padx=3, pady=5, ipadx=1, ipady=10)

        # Creamos frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=530, bg='aquamarine')
        botones_frame.pack()

        # Primer renglon
        boton_limpiar = tk.Button(botones_frame, text='C', width=10, height=3,
                                  bd=1, bg='#CCCCFF', cursor='hand2',
                                  command=self._evento_limpiar).grid(row=0, column=0, padx=3, pady=2)
        boton_paretesis = tk.Button(botones_frame, text='( )', width=10, height=3,
                                    bd=1, bg='#CCCCFF', cursor='hand2',
                                    command=self._evento_parentesis).grid(row=0, column=1, padx=3, pady=2)
        boton_porcentaje = tk.Button(botones_frame, text='%', width=10, height=3,
                                     bd=1, bg='#CCCCFF', cursor='hand2',
                                     command=lambda: self._evento_click('%')).grid(row=0, column=2, padx=3, pady=2)
        boton_division = tk.Button(botones_frame, text='\u00F7', width=10, height=3,
                                   bd=1, bg='#CCCCFF', cursor='hand2',
                                   command=lambda: self._evento_click('/')).grid(row=0, column=3, padx=3, pady=2)

        # Segundo renglon
        boton_siete = tk.Button(botones_frame, text='7', width=10, height=3,
                                bd=1, bg='#CCCCFF', cursor='hand2',
                                command=lambda: self._evento_click('7')).grid(row=1, column=0, padx=3, pady=2)
        boton_ocho = tk.Button(botones_frame, text='8', width=10, height=3,
                               bd=1, bg='#CCCCFF', cursor='hand2',
                               command=lambda: self._evento_click('8')).grid(row=1, column=1, padx=3, pady=2)
        boton_nueve = tk.Button(botones_frame, text='9', width=10, height=3,
                                bd=1, bg='#CCCCFF', cursor='hand2',
                                command=lambda: self._evento_click('9')).grid(row=1, column=2, padx=3, pady=2)
        boton_multiplicacion = tk.Button(botones_frame, text='\u00D7', width=10, height=3,
                                         bd=1, bg='#CCCCFF', cursor='hand2',
                                         command=lambda: self._evento_click('*')).grid(row=1, column=3, padx=3, pady=2)

        # Tercer renglon
        boton_cuatro = tk.Button(botones_frame, text='4', width=10, height=3,
                                 bd=1, bg='#CCCCFF', cursor='hand2',
                                 command=lambda: self._evento_click('4')).grid(row=2, column=0, padx=3, pady=2)
        boton_cinco = tk.Button(botones_frame, text='5', width=10, height=3,
                                bd=1, bg='#CCCCFF', cursor='hand2',
                                command=lambda: self._evento_click('5')).grid(row=2, column=1, padx=3, pady=2)
        boton_seis = tk.Button(botones_frame, text='6', width=10, height=3,
                               bd=1, bg='#CCCCFF', cursor='hand2',
                               command=lambda: self._evento_click('6')).grid(row=2, column=2, padx=3, pady=2)
        boton_resta = tk.Button(botones_frame, text='-', width=10, height=3,
                                bd=1, bg='#CCCCFF', cursor='hand2',
                                command=lambda: self._evento_click('-')).grid(row=2, column=3, padx=3, pady=2)

        # Cuarto renglon
        boton_uno = tk.Button(botones_frame, text='1', width=10, height=3,
                              bd=1, bg='#CCCCFF', cursor='hand2',
                              command=lambda: self._evento_click('1')).grid(row=3, column=0, padx=3, pady=2)
        boton_dos = tk.Button(botones_frame, text='2', width=10, height=3,
                              bd=1, bg='#CCCCFF', cursor='hand2',
                              command=lambda: self._evento_click('2')).grid(row=3, column=1, padx=3, pady=2)
        boton_tres = tk.Button(botones_frame, text='3', width=10, height=3,
                               bd=1, bg='#CCCCFF', cursor='hand2',
                               command=lambda: self._evento_click('3')).grid(row=3, column=2, padx=3, pady=2)
        boton_suma = tk.Button(botones_frame, text='+', width=10, height=3,
                               bd=1, bg='#CCCCFF', cursor='hand2',
                               command=lambda: self._evento_click('+')).grid(row=3, column=3, padx=3, pady=2)

        # Quinto renglon
        boton_cero = tk.Button(botones_frame, text='0', width=10, height=3,
                               bd=1, bg='#CCCCFF', cursor='hand2',
                               command=lambda: self._evento_click('0')).grid(row=4, column=0, padx=3, pady=2)
        boton_punto = tk.Button(botones_frame, text='.', width=10, height=3,
                                bd=1, bg='#CCCCFF', cursor='hand2',
                                command=lambda: self._evento_click('.')).grid(row=4, column=1, padx=3, pady=2)
        boton_corrregir = tk.Button(botones_frame, text='\U0001F814', width=10, height=3,
                                    bd=1, bg='#CCCCFF', cursor='hand2',
                                    command=self._evento_corregir).grid(row=4, column=2, padx=3, pady=2)
        boton_igual = tk.Button(botones_frame, text='=', width=10, height=3,
                                bd=1, bg='#CCCCFF', cursor='hand2',
                                command=self._evento_igual).grid(row=4, column=3, padx=3, pady=2)

    '''Metodo salir'''
    def _salir(self):
        self.quit()
        self.destroy()
        print('Salimos...')
        sys.exit()

    '''Metodo salir'''
    def _acerca_de(self):
        messagebox.showinfo('Acerca de calculadora', 'Calculadora en proceso de mejora')

    '''Metodo limpiar'''
    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    '''Metodo Click'''
    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento a la expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)

    '''Metodo igual'''
    def _evento_igual(self):
        # eval evalua la expresion str como una expresion aritmetica
        try:
            if self.expresion:
                self._evento_porcentaje()
                resultado = str(eval(self.expresion))
                
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.entrada_texto.set(resultado)
            # self.expresion = ''

    '''Metodo porcentaje'''
    def _evento_porcentaje(self):
        lista = list(self.expresion)
        if lista[-1] == '%':
            if '+' in lista:
                lista = self.expresion.split('+')
                self.expresion = f'({lista[0]})*({lista[1].replace('%', '/100)')}+({lista[0]})'
            if '-' in lista:
                lista = self.expresion.split('-')
                self.expresion = f'({lista[0]})-({lista[0]})*({lista[1].replace('%', '/100')})'
            
    '''Metodo parentesis'''
    def _evento_parentesis(self):
        pass


    '''Metodo corregir'''
    def _evento_corregir(self):
        if self.expresion == '':
            self.entrada_texto.set('')
        else:
            lista = list(self.expresion)
            lista.remove(lista[-1])
            self.expresion = ''.join(lista)
            self.entrada_texto.set(self.expresion)

if __name__ == '__main__':
    caculadora = Calculadora()
    caculadora.mainloop()