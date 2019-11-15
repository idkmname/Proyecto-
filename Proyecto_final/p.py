from tkinter import *
import random
from barco import *
from tablero import *
from functools import partial 
from json import * 


def inicializar_barcos():
    global tablero_usuario
    global tablero_maquina
    global matrices_maquina
    global matriz_matrices_maquina

    #barcos del jugador
    a4x = barco_4x.get()
    a3x = barco_3x.get()
    a2x = barco_2x.get()
    a1x = barco_1x.get()
    a5x = barco_5x.get()

    a4y = barco_4y.get()
    a3y = barco_3y.get()
    a2y = barco_2y.get()
    a1y = barco_1y.get()
    a5y = barco_5y.get()

    a4d = barco_4d.get()
    a3d = barco_3d.get()
    a2d = barco_2d.get()
    a1d = barco_1d.get()
    a5d = barco_5d.get()

    Barco1 = Barco(1,a1x,a1y,a1d)
    Barco2 = Barco(2,a2x,a2y,a2d)
    Barco3 = Barco(3,a3x,a3y,a3d)
    Barco4 = Barco(4,a4x,a4y,a4d)
    Barco5 = Barco(5,a5x,a5y,a5d)

    tablero_usuario = Tablero(Barco1,Barco2,Barco3,Barco4,Barco5)   

   
    salida_cruce_usuario = tablero_usuario.verificar_tablero_cruce()
    salida_tamano_usuario = tablero_usuario.verificar_tablero_tamano()
    tablero_usuario.mostrar_matriz()

    if salida_cruce_usuario == 1 :
        print("error, se cruzan los barcos")
    elif salida_tamano_usuario == 1:
        print("error, se sale de la matriz")
    else:
        # si el usuario no cometio errores, posiciona maquina
        b = random.randrange(0,2)   
        tablero_maquina = Tablero(matrices_maquina[b][0],matrices_maquina[b][1],matrices_maquina[b][2],matrices_maquina[b][3],matrices_maquina[b][4])
        tablero_maquina.verificar_tablero_cruce()
        actualizar_vista()        
        anuncio.config(text = "presione iniciar,juego")
        iniciar_juego()






def iniciar_juego():
    global estaddio
    global mat
    estaddio = 1
    barco_1x.place_forget()
    barco_2x.place_forget()
    barco_3x.place_forget()
    barco_4x.place_forget()
    barco_5x.place_forget()
    barco_1y.place_forget()
    barco_2y.place_forget()
    barco_3y.place_forget()
    barco_4y.place_forget()
    barco_5y.place_forget()
    barco_1d.place_forget()
    barco_2d.place_forget()
    barco_3d.place_forget()
    barco_4d.place_forget()
    barco_5d.place_forget()
    xyp.place_forget()
    iniciarbarcos.place_forget()
    cargar_barcos.place_forget()
    guardar_barcos.place_forget()
    reiniciar.place(x = 20, y = 600)
    anuncio.config(text = "su turno, dispare")

    for a in range(8):
        for b in range(8):
            mat2[a][b].config(command = partial(disparar_usuario, a,b))




def reiniciar():
    global tablero_usuario
    global tablero_maquina
    tablero_maquina = []
    tablero_usuario = []
    reiniciar.place_forget()
    iniciartab()
    







#modificar tablero
def actualizar_vista():
    global mat 
    global mat2
    c = tablero_usuario.mat
    for a in range(8):
        for b in range(8):
            d = c[a][b]
            contador = 0 
            if d == 6:
                mat[a][b].config(image = dio)
            elif d ==1 or d ==2 or d ==3 or d ==4 or d ==5:
                mat[a][b].config(image = barco)
                contador += 1
            elif estaddio == 0 and d == 0:
                mat[a][b].config(image = agua)



    m = tablero_maquina.mat
    for a in range(8):
        for b in range(8):
            d = m[a][b]
            if d == 6:
                mat2[a][b].config(image = dio)
            elif estaddio == 0 and d == 0:
                mat[a][b].config(image = agua)
    
        
    



def disparar_usuario(X,Y):
    global mat2
    if tablero_maquina.recibir_disparo(X,Y) == "Game Over":
        pf = tablero_maquina.aciertos // tablero_maquina.total_fallos
        anuncio.config(text = "Jugador Gano a la maquina \n su puntaje fue: " + str(pf)+ "\n la cantidad de disparos fallidos fue: " + str(tablero_maquina.total_fallos) + "\n su puntaje por aciertos fue: " + str(tablero_maquina.aciertos))
        #tablero_usuario.calcular_puntaje


        
    else:
        if tablero_maquina.mat[X][Y] != 0 and tablero_maquina.mat[X][Y] < 6:
            m = "El jugador acerto, dispare de nuevo"
            
        else:
            m = "El jugador fallo"
            mat2[X][Y].config(image = fallo)
        anuncio.config(text = "Su Turno \n" + (m))
        disparo_maquina()
    actualizar_vista()





def disparo_maquina():
    global mat
    a = random.randrange(0,8) 
    b = random.randrange(0,8) 
    try:
        if tablero_usuario.recibir_disparo(a,b) == "Game Over":
            pf = tablero_maquina.aciertos // tablero_maquina.total_fallos
            anuncio.config(text = "gano la maquina \n su puntaje fue:  " + str(pf) + "\n la cantidad de disparos fallidos fue: " + str(tablero_maquina.total_fallos) + "\n su puntaje por aciertos fue: " + str(tablero_maquina.aciertos))
            #tablero_usuario.calcular_puntaje
        else:
            if tablero_usuario.mat[a][b] != 0 and tablero_usuario.mat[a][b] < 6:
                m = "la maquina acerto, le toca" 

            else:
                m = "la maquina fallo"
                mat[a][b].config(image = fallo)
    except: 
        print(":p") 



def paso():
    pass




def cargar_tablero():
    global tablero_usuario
    try:
        x = open("guardado.txt", "r")
        tablero_usuario.listabarcos = x
        x.close()
    except:
        anuncio.config(text = "No se ha guardado ningun configuracion de barcos") 




def guardar_tablero():
    global tablero_usuario
    global guardados
    try:
        x = open("guardado.txt","w")
        x.write(tablero_usuario.listabarcos)
        x.close()
    except:
        anuncio.config(text = "Aun no existe ninguna posicion en el tablero que guardar") 





#comandos mapa
def iniciartab():
    global mat
    global mat2

    #pintar tablero usuario vacio
    mat = []
    for a in range(1,9):
        m = []
        for b in range(1,9):
           m.append(Label(ventana, width = 40, height = 48, borderwidth = 3, relief = FLAT, image = agua )) 
        mat.append(m)

    n = 80
    h = 200
    for j in range(8):
        n += 53
        for k in range(8):
            mat[j][k].place(x = h , y = n)
            h += 45
        h = 200


    #tablero enemigo vacio
    mat2 = []
    for a in range(8):
        m = []
        for b in range(8):
           m.append(Button(ventana, width = 40, height = 48, borderwidth = 3, relief = FLAT, image = agua, command = paso())) 
        mat2.append(m)

    n = 80
    h = 600
    for j in range(8):
        n += 53
        for k in range(8):
            mat2[j][k].place(x = h , y = n)
            h += 45
        h = 600
    


    xyp.place(x = 15, y = 110)
    barco_1x.place(x = 15 ,y = 133)  
    barco_2x.place(x = 15 ,y = 213)  
    barco_3x.place(x = 15 ,y = 293)  
    barco_4x.place(x = 15 ,y = 373)
    barco_5x.place(x = 15 ,y = 459)
    barco_1y.place(x = 35 ,y = 133)  
    barco_2y.place(x = 35 ,y = 213)  
    barco_3y.place(x = 35 ,y = 293)  
    barco_4y.place(x = 35 ,y = 373)
    barco_5y.place(x = 35 ,y = 459)
    barco_1d.place(x = 55 ,y = 133)  
    barco_2d.place(x = 55 ,y = 213)  
    barco_3d.place(x = 55 ,y = 293)  
    barco_4d.place(x = 55 ,y = 373)
    barco_5d.place(x = 55 ,y = 459)
    iniciarbarcos.place(x = 20, y = 600)
    anuncio.place(x = 575, y = 600)
    anuncio.config(text = "Ordene sus barcos por favor") 
    tablero_usuarionom.place(x = 350 , y = 100)
    tablero_maquinanom.place(x = 750 , y = 100)
    cargar_barcos.place(x = 20, y = 500)
    guardar_barcos.place(x = 20, y = 550)

def quitartab():
    global mat
    global mat2

    for j in range(8):
        for k in range(8):
            mat[j][k].place_forget()

    for j in range(8):
        for k in range(8):
            mat2[j][k].place_forget()


    barco_1x.place_forget()
    barco_2x.place_forget()
    barco_3x.place_forget()
    barco_4x.place_forget()
    barco_5x.place_forget()
    barco_1y.place_forget()
    barco_2y.place_forget()
    barco_3y.place_forget()
    barco_4y.place_forget()
    barco_5y.place_forget()
    barco_1d.place_forget()
    barco_2d.place_forget()
    barco_3d.place_forget()
    barco_4d.place_forget()
    barco_5d.place_forget()
    xyp.place_forget()
    iniciarbarcos.place_forget()
    anuncio.place_forget()
    cargar_barcos.place_forget()
    guardar_barcos.place_forget()
    iniciarbarcos.place_forget()
    anuncio.place_forget()
    tablero_maquinanom.place_forget()
    tablero_usuarionom.place_forget()
    reiniciar.place_forget()

    

#commandos menu 
def atras():
    inicio.place(x=400 , y=300)
    dificultad.place(x=400 , y=375)
    salir.place(x=400 , y=450)
    atras.place_forget()
    facil.place_forget()
    normal.place_forget()
    dificil.place_forget()


def alPrincipal():
    global matriz_machine
    global matriz_barcos
    global estaddio
    estaddio = 0 
    inicio.place(x=400 , y=300)
    dificultad.place(x=400 , y=375)
    salir.place(x=400 , y=450)
    titulo.config(text = "BATALLA NAVAL")
    menu_principalS.place_forget()
    quitartab()
    matriz_machine = []
    matriz_barcos = []


def iniciar():
    global matriz_usuario
    global matriz_machine
    inicio.place_forget()
    dificultad.place_forget()
    salir.place_forget()
    menu_principalS.place(x=900 , y=600)
    titulo.config( text = "Fase de preparacion")
    estaddio = 1
    iniciartab()

    

def dificultad():
    inicio.place_forget()
    dificultad.place_forget()
    salir.place_forget()
    facil.place(x=400 , y=300)
    normal.place(x=400 , y=375)
    dificil.place(x=400 , y=450)
    atras.place(x=400 , y=525)


def facil():
    inicio.place(x=400 , y=300)
    dificultad.place(x=400 , y=375)
    salir.place(x=400 , y=450)
    atras.place_forget()
    facil.place_forget()
    normal.place_forget()
    dificil.place_forget()
    dificiultad = "facil"
    dific.config(text = "Dificultad facil")
    

def normal():
    inicio.place(x=400 , y=300)
    dificultad.place(x=400 , y=375)
    salir.place(x=400 , y=450)
    atras.place_forget()
    facil.place_forget()
    normal.place_forget()
    dificil.place_forget()
    dificiultad = "normal"
    dific.config(text = "Dificultad normal")


def dificil():
    inicio.place(x=400 , y=300)
    dificultad.place(x=400 , y=375)
    salir.place(x=400 , y=450)
    atras.place_forget()
    facil.place_forget()
    normal.place_forget()
    dificil.place_forget()
    dificiultad = "dificil"
    dific.config(text = "Dificultad dificil")


def salir():
    ventana.destroy()











#variables
dificiultad = "normal"
estaddio = 0
mat = []
mat2 = []
tablero_usuario = 0
tablero_maquina = 0


matrices_maquina = []

barco1_e1 = Barco(1,0,0,2)
barco2_e1 = Barco(2,0,2,2)
barco3_e1 = Barco(3,3,0,4)
barco4_e1 = Barco(4,5,0,4)
barco5_e1 = Barco(5,7,7,1)

barco1_e2 = Barco(1,1,1,2)
barco2_e2 = Barco(2,0,3,2)
barco3_e2 = Barco(3,3,0,4)
barco4_e2 = Barco(4,5,0,4)
barco5_e2 = Barco(5,7,7,1)

barco1_e3 = Barco(1,0,0,2)
barco2_e3 = Barco(2,0,2,2)
barco3_e3 = Barco(3,3,0,4)
barco4_e3 = Barco(4,5,0,4)
barco5_e3 = Barco(5,6,6,1)

matriz_maquina1 = [barco1_e1,barco2_e1,barco3_e1,barco4_e1,barco5_e1]

matriz_maquina2 = [barco1_e2,barco2_e2,barco3_e2,barco4_e2,barco5_e2]

matriz_maquina3 = [barco1_e3,barco2_e3,barco3_e3,barco4_e3,barco5_e3]

matrices_maquina.append(matriz_maquina1)
matrices_maquina.append(matriz_maquina2)
matrices_maquina.append(matriz_maquina3)

color1 = "#d1a956"















#Visual
ventana = Tk()
ventana.geometry("1100x700")
ventana.title("Batalla naval")
ventana.config(background = "white" )
ventana.resizable(0,0)


barco_1x = Entry(ventana,borderwidth = 3, width = 2) 
barco_1x.place(x = 15 ,y = 80) 
barco_1x.place_forget() 


barco_2x = Entry(ventana,borderwidth = 3, width = 2) 
barco_2x.place(x = 15 ,y = 180) 
barco_2x.place_forget() 


barco_3x = Entry(ventana,borderwidth = 3, width = 2) 
barco_3x.place(x = 15 ,y = 330) 
barco_3x.place_forget() 

barco_4x = Entry(ventana,borderwidth = 3, width = 2) 
barco_4x.place(x = 15 ,y = 480) 
barco_4x.place_forget() 

barco_5x = Entry(ventana,borderwidth = 3, width = 2) 
barco_5x.place(x = 15 ,y = 480) 
barco_5x.place_forget() 

barco_1y = Entry(ventana,borderwidth = 3, width = 2) 
barco_1y.place(x = 15 ,y = 80) 
barco_1y.place_forget() 


barco_2y = Entry(ventana,borderwidth = 3, width = 2) 
barco_2y.place(x = 15 ,y = 180) 
barco_2y.place_forget() 


barco_3y = Entry(ventana,borderwidth = 3, width = 2) 
barco_3y.place(x = 15 ,y = 330) 
barco_3y.place_forget() 

barco_4y = Entry(ventana,borderwidth = 3, width = 2) 
barco_4y.place(x = 15 ,y = 480) 
barco_4y.place_forget() 

barco_5y = Entry(ventana,borderwidth = 3, width = 2) 
barco_5y.place(x = 15 ,y = 480) 
barco_5y.place_forget() 

barco_1d = Entry(ventana,borderwidth = 3, width = 2) 
barco_1d.place(x = 15 ,y = 80) 
barco_1d.place_forget() 


barco_2d = Entry(ventana,borderwidth = 3, width = 2) 
barco_2d.place(x = 15 ,y = 180) 
barco_2d.place_forget() 


barco_3d = Entry(ventana,borderwidth = 3, width = 2) 
barco_3d.place(x = 15 ,y = 330) 
barco_3d.place_forget() 

barco_4d = Entry(ventana,borderwidth = 3, width = 2) 
barco_4d.place(x = 15 ,y = 480) 
barco_4d.place_forget() 

barco_5d = Entry(ventana,borderwidth = 3, width = 2) 
barco_5d.place(x = 15 ,y = 480) 
barco_5d.place_forget() 



#imagenes

barco = PhotoImage(file = "barco.png")
agua = PhotoImage(file = "oceano.png")
dio = PhotoImage(file = "dio.png")
fallo = PhotoImage(file = "fallo.png")




#compedio de textos 
titulo = Label(ventana, text = "BATALLA NAVAL", font = ("Imperfecta Rough",30),
             fg = color1 )
titulo.pack()
titulo.config(background = "white", )

dific = Label(ventana, text = "Dificultad normal", font = ("Imperfecta Rough",10),
              fg = color1)
dific.place(x=980, y=1)
dific.config(background = "white")

ver = Label(ventana, text="ver 0.36")
ver.place(x=0,y=680)

xyp = Label(ventana, text = "X    Y    D", font = (10))
xyp.config(background = "white")
xyp.place(x = 1, y = 1)
xyp.place_forget()


anuncio = Label (ventana, text = "", font = 10, fg = color1)
anuncio.config(background = "white")
anuncio.place(x = 0 , y = 0)
anuncio.place_forget()


tablero_usuarionom = Label (ventana, text = "Tu tablero", font = 10, fg = color1)
tablero_usuarionom.config(background = "white")
tablero_usuarionom.place(x = 0 , y = 0)
tablero_usuarionom.place_forget()

tablero_maquinanom = Label (ventana, text = "Tablero enemigo", font = 10, fg = color1)
tablero_maquinanom.config(background = "white")
tablero_maquinanom.place(x = 0 , y = 0)
tablero_maquinanom.place_forget()










#compedio de botones
inicio = Button(ventana, text = "Iniciar juego",font = ("Imperfecta Rough",20),
                fg = "white", width = 19,borderwidth = 3, relief = "groove",
                command = iniciar)
inicio.place(x=400 , y=300)
inicio.config(background = color1 )


dificultad = Button(ventana, text = "Dificultad",font = ("Imperfecta Rough",20),
                    fg = "white", width = 19, borderwidth = 3, relief = "groove"
                    ,command = dificultad)
dificultad.place(x=400 , y=375)
dificultad.config(background = color1)

salir = Button(ventana, text = "Salir del juego",font = ("Imperfecta Rough",20),
               fg = "white", width = 19, borderwidth = 3, relief = "groove",
               command = salir)
salir.place(x=400 , y=450)
salir.config(background = color1)

atras = Button(ventana, text = "Atras",font = ("Imperfecta Rough",20),
               fg = "white", width = 19, borderwidth = 3, relief = "groove",
               command = atras)
atras.place(x=400 , y=525)
atras.config(background = color1)
atras.place_forget()

facil = Button(ventana, text = "Facil",font = ("Imperfecta Rough",20),
               fg = "white", width = 19, borderwidth = 3, relief = "groove",
               command = facil)
facil.place(x=400 , y=300)
facil.config(background = color1)
facil.place_forget()

normal = Button(ventana, text = "Normal",font = ("Imperfecta Rough",20),
               fg = "white", width = 19, borderwidth = 3, relief = "groove",
               command = normal)
normal.place(x=400 , y=375)
normal.config(background = color1)
normal.place_forget()

dificil = Button(ventana, text = "Dificil",font = ("Imperfecta Rough",20),
               fg = "white", width = 19, borderwidth = 3, relief = "groove",
               command = dificil)
dificil.place(x=400 , y=450)
dificil.config(background = color1)
dificil.place_forget()

menu_principalS = Button(ventana, text = "Salir al menu principal", font = (6),
                    fg = "white", width = 17, borderwidth = 2, relief = "groove",
                    command = alPrincipal)
menu_principalS.place(x=1000 , y=580)
menu_principalS.config(background = color1)
menu_principalS.place_forget()

iniciarbarcos = Button(ventana, text="Dibujar barcos e iniciar juego", font = (6),
                       fg = "white", width = 17, borderwidth = 2, relief = "groove",
                       command = inicializar_barcos)
iniciarbarcos.place(x = 1 , y = 1)
iniciarbarcos.config(background = color1)
iniciarbarcos.place_forget()

cargar_barcos = Button(ventana, text="cargar barcos", font = (6),
                       fg = "white", width = 17, borderwidth = 2, relief = "groove",
                       command = cargar_tablero)
cargar_barcos.place(x = 1 , y = 1)
cargar_barcos.config(background = color1)
cargar_barcos.place_forget()

guardar_barcos = Button(ventana, text="guardar barcos", font = (6),
                       fg = "white", width = 17, borderwidth = 2, relief = "groove",
                       command = guardar_tablero)
guardar_barcos.place(x = 1 , y = 1)
guardar_barcos.config(background = color1)
guardar_barcos.place_forget()


reiniciar = Button(ventana, text="Reiniciar", font = (6),
                       fg = "white", width = 17, borderwidth = 2, relief = "groove",
                       command = reiniciar)
reiniciar.place(x = 1 , y = 1)
reiniciar.config(background = color1)
reiniciar.place_forget()


ventana.mainloop()

