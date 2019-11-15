import random
import json


class Tablero(object):
               

    def __init__(self,B1,B2,B3,B4,B5):
        
        #lista de barcos
        self.listabarcos = [B1,B2,B3,B4,B5]
        self.puntos = 15
        self.aciertos = 0
        self.total_fallos = 0
        self.puntajefinal = 0 
        #matriz tablero
        self.mat = []
        for a in range(8):
            c = []
            for b in range(8):
                c.append(0)
            self.mat.append(c)
        
        



    def verificar_tablero_cruce(self):       
        bandera  = 0 
        for a in (self.listabarcos):   
            if self.mat[int(a.coordenadaX)][int(a.coordenadaY)] == 0: 
                contador_interno = 0          
                for b in range(int(a.tamano)):  
                   
                   if  int(a.direccion) == 1:
                        if  self.mat[int(a.coordenadaX) - contador_interno][int(a.coordenadaY)] == 0:
                            self.mat[int(a.coordenadaX) - contador_interno][int(a.coordenadaY)] = int(a.tamano)
                        else:
                            bandera=1
                   elif int(a.direccion) == 2:  
                        print (a.coordenadaX)
                        if self.mat[int(a.coordenadaX) + contador_interno][int(a.coordenadaY)] == 0:
                           self.mat[int(a.coordenadaX) + contador_interno][int(a.coordenadaY)] = int(a.tamano)
                        else:
                            bandera=1      
                   elif  int(a.direccion) == 3:
                        print (a.coordenadaX)
                        if self.mat[int(a.coordenadaX)][int(a.coordenadaY) - contador_interno] == 0: 
                            self.mat[int(a.coordenadaX)][int(a.coordenadaY) - contador_interno] = int(a.tamano)
                        else:
                            bandera = 1
                   elif int(a.direccion) == 4:
                        print (a.coordenadaX)
                        if self.mat[int(a.coordenadaX)][int(a.coordenadaY) + contador_interno] == 0: 
                            self.mat[int(a.coordenadaX)][int(a.coordenadaY) + contador_interno] = int(a.tamano)
                        else:
                            bandera = 1
                   contador_interno += 1
            else:
                bandera=1 
            
        return bandera 



    #verificacion que no se salga de la matriz
    
    def verificar_tablero_tamano(self):
        bandera2 = 0
        for a in (self.listabarcos):
            if int(a.direccion) == 1:               
                if (int(a.coordenadaX) - int(a.tamano)) < 0:
                    bandera2 = 1
            elif int(a.direccion) == 2:
                if( int(a.coordenadaX) + int(a.tamano)) > 7 :
                    bandera2 = 1
            elif int(a.direccion) == 3:
                if (int(a.coordenadaY) - int(a.tamano)) < 0:
                    bandera2 = 1
            elif int(a.direccion) == 4:
                if (int(a.coordenadaY) + int(a.tamano)) > 7:
                    bandera2 = 1
            print (a.direccion)
        return bandera2



    def mostrar_matriz(self):
        print(self.mat)


    def recibir_disparo(self,X,Y):
        if self.mat[X][Y] != 0 and self.mat[X][Y] < 6:
            self.mat[X][Y] = 6
            self.puntos -= 1
            self.aciertos += 100
        if self.puntos == 0:
            return "Game Over"
        else:
            self.total_fallos += 1
            return "Continue Disparando"
        
        


