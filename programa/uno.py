from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
from tkinter import ttk

import pickle
from pickle import *
import math

class Estudiante():
    def __init__(self,nombre,lista_notas):
        self.n=nombre
        self.ln=lista_notas

    def estado(self):
        pass

class Lista():
    estudiantes=[]
    def __init__(self):
        print("hhh")
        try:
            listaEst=open("Curso","ab+")
            
        except:
            
            print(" no se creo archivo")
        listaEst.seek(0)
        try:
            
            self.estudiantes=pickle.load(listaEst)
        except:
            print("curso vacio,no se puede modificar ni eliminar datos")
        finally:
            listaEst.close()
            del(listaEst)

    def insertar_estudiante(self,e):
        self.estudiantes.append(e)
        self.estudiante_a_fichero()

    def estudiante_a_fichero(self):
        listaEst=open("Curso","wb")
        pickle.dump(self.estudiantes,listaEst)
        listaEst.close()
        del(listaEst)
    
    def mostrar_estudiantes(self):
        for e in self.estudiantes:
            print("\n")
            listbox.insert(END,e.n)

    def buscar_estudiante(self,i):
        
        for b in self.estudiantes:
            if i==b.n:
                return b

    def estadisticas_estudiante(self):
        for e in self.estudiantes:
            pass

    def eliminar_estudiante(self, b):
    
        try:
            self.estudiantes.remove(b)
            self.estudiante_a_fichero()
        except:
            print("no se pudo eliminar")

    def modificar_estudiante(self,b):
        
        i = self.estudiantes.index(b)
        self.estudiantes[i].n=textbox31.get()
        self.estudiante_a_fichero()
    
    def ingreso_notas_estudiante(self,e,n1,n2,n3,n4):
        i = self.estudiantes.index(e)
        self.estudiantes[i].ln[0]=n1
        self.estudiantes[i].ln[1]=n2
        self.estudiantes[i].ln[2]=n3
        self.estudiantes[i].ln[3]=n4
        self.estudiante_a_fichero()



curso=Lista()

def crear_form1():

    ventana1 =Tk()
    ventana1.geometry("500x500")
    ventana1.resizable(False,False)
    ventana1.title("Notas")

    miFrame1=Frame(ventana1,width="500", height="500")
    miFrame1.pack()

    global listbox
    listbox = Listbox(miFrame1, selectmode="SINGLE") 
    listbox.pack()
    

    boton11 = Button(miFrame1, text="ingresar estudiante", command=crear_form2, width=13)
    boton11.pack()
    boton12 = Button(miFrame1, text="modificar estudiante", command=crear_form3, width=13)
    boton12.pack()
    boton13 = Button(miFrame1, text="eliminar estudiante", command=el_est, width=13)
    boton13.pack()

    boton14 = Button(miFrame1, text="ingresar notas", command=crear_form4, width=13)
    boton14.pack()
    boton15 = Button(miFrame1, text="estadisticas", command=crear_form5, width=13)
    boton15.pack()

    curso.mostrar_estudiantes()

    ventana1.mainloop()

def ing_est():
    #print("dklwoiwdn")
    print(textbox.get())
    
    lista=[1.0,1.0,1.0,1.0]
    estudiante=Estudiante(textbox.get(),lista)

    curso.insertar_estudiante(estudiante)
    listbox.insert(END, estudiante.n)
    ventana2.destroy()

def crear_form2():
    global ventana2
    ventana2 =Tk()
    ventana2.geometry("500x500")
    ventana2.resizable(False,False)
    ventana2.title("Estudiante")

    miFrame2=Frame(ventana2,width="500", height="500")
    miFrame2.pack()

    lbl = Label(miFrame2,text="Nuevo Estudiante")
    lbl.pack()
    global textbox
    textbox=ttk.Entry(miFrame2, width=20)
    textbox.pack()

    boton21 = Button(miFrame2, text="Ingresar", command=ing_est, width=13)
    boton21.pack()

    
    ventana2.mainloop()

    
def crear_form3():
    
    global ventana3
    ventana3 =Tk()
    ventana3.geometry("500x500")
    ventana3.resizable(False,False)
    ventana3.title("Estudiante modificar")

    miFrame3=Frame(ventana3,width="500", height="500")
    miFrame3.pack()

    lbl = Label(miFrame3,text="Modificar Estudiante")
    lbl.pack()
    global textbox31
    textbox31=ttk.Entry(miFrame3, width=20)
    textbox31.pack()

    boton31 = Button(miFrame3, text="Modificar", command=mod_est, width=13)
    boton31.pack()

    
    ventana3.mainloop()

def crear_form4():
    global ventana4
    ventana4 =Tk()
    ventana4.geometry("500x500")
    ventana4.resizable(False,False)
    ventana4.title("notas")

    miFrame4=Frame(ventana4,width="500", height="500")
    miFrame4.pack()

    if verificar!=False:
        try:
            index=listbox.curselection()[0]
        except:
            print("seleccione a alguien")
        
        value = listbox.get(index)
        lbln = Label(miFrame4,text=value)
        lbln.pack()

        est= curso.buscar_estudiante(value)
        
        global tb1
        tb1=ttk.Entry(miFrame4, width=10)
        tb1.insert(END,est.ln[0])
        tb1.pack()
        global tb2
        tb2=ttk.Entry(miFrame4, width=10)
        tb2.insert(END,est.ln[1])
        tb2.pack()
        global tb3
        tb3=ttk.Entry(miFrame4, width=10)
        tb3.insert(END,est.ln[2])
        tb3.pack()
        global tb4
        tb4=ttk.Entry(miFrame4, width=10)
        tb4.insert(END,est.ln[3])
        tb4.pack()

    boton41 = Button(miFrame4, text="Ingresar notas", command=ingresar_notas, width=13)
    boton41.pack()

    
    ventana4.mainloop()

def crear_form5():
    global ventana5
    ventana5 =Tk()
    ventana5.geometry("500x500")
    ventana5.resizable(False,False)
    ventana5.title("Estadisticas")

    miFrame5=Frame(ventana5,width="500", height="500")
    miFrame5.pack()

    lbl51 = Label(miFrame5,text="nota minima")
    lbl51.pack()
    lbl512 = Label(miFrame5,text="")
    lbl512.pack()
    lbl52 = Label(miFrame5,text="nota maxima")
    lbl52.pack()
    lbl522 = Label(miFrame5,text="")
    lbl522.pack()
    lbl53 = Label(miFrame5,text="promedio")
    lbl53.pack()
    lbl532 = Label(miFrame5,text="")
    lbl532.pack()
    lbl4 = Label(miFrame5,text="cantidad")
    lbl4.pack()
    lbl42 = Label(miFrame5,text="")
    lbl42.pack()
    

    
    ventana5.mainloop()

def mod_est():
    
    if verificar()!=False:
        
        index=listbox.curselection()[0]
        text=textbox31.get()
        value = listbox.get(index)
        listbox.delete(index)
        listbox.insert(index,text)
        #listbox.delete(index)
        
        
        curso.modificar_estudiante(curso.buscar_estudiante(value))


def el_est():
    if verificar()!=False:
       
        index=listbox.curselection()[0]
        listbox.delete(index)
        value = listbox.get(index)
        curso.eliminar_estudiante(curso.buscar_estudiante(value))
        

def is_empty(datastructure):
    if datastructure:
        print("No está vacía")
        return False
    else:
        print("Está vacía")
        return True

def verificar():
	
    if is_empty(listbox.curselection()):
	    return False
    else:
        return listbox.curselection()


def ingresar_notas():
    
    index=listbox.curselection()[0]
    text1=tb1.get()
    text2=tb2.get()
    text3=tb3.get()
    text4=tb4.get()
    '''
    comprobar=[text1,text2,text3,text4]
    while True:
        for i in comprobar:
            i=float(i)
            
            if i==0 or i==None:
                i==1
            if i>1 and i<7:
                break
            
    '''
    value = listbox.get(index)

    
    
    curso.ingreso_notas_estudiante(curso.buscar_estudiante(value),text1,text2,text3,text4)

def nota_minima():
    index=listbox.curselection()[0]
    value = listbox.get(index)
    est=curso.buscar_estudiante(value)
    


crear_form1()



