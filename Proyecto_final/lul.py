g = open("supp","w")


n = 80
h = 230
for a in range(1,9):
    n += 53
        
    for b in range(1,9):
        #print("posicionusuario" + str(a)+ "_"+ str(b)+" = Label(ventana, width = 40, height = 48, borderwidth = 3, relief = FLAT, image = agua) \nposicionusuario" + str(a)+ "_"+ str(b)+".place(x=300 , y= 200) \nposicionusuario" + str(a)+ "_"+ str(b)+".place_forget() \n \n") 
        #print("posicionusuario" + str(a)+ "_"+ str(b)+".place(x="+str(h)+", y= "+str(n)+")")
        h += 45
        print ("    posicionusuario" + str(a)+ "_"+ str(b)+ ".place_forget()")
    h = 230
  
'''
n = 80
h = 15

for c in range (1,5):
    if c == 1:
        for d in range(2):
            print("global barco_" + str(c) + "_" + str(d) + " = Entry(ventana,) ")
          #  print("barco_" + str(c) + "_" + str(d) + ".place(x = 15 ,y = " + str(n)+ ") ")
         #   print("barco_" + str(c) + "_" + str(d) + ".place_forget() \n")
            n += 50
            
    if c == 2:
        for d in range(3):
            print("global barco_" + str(c) + "_" + str(d) + " = Entry(ventana,) ")
            #print("barco_" + str(c) + "_" + str(d) + ".place(x = 15 ,y = " + str(n)+ ") ")
            #print("barco_" + str(c) + "_" + str(d) + ".place_forget() \n")
            n += 50
            
    if c == 3:
        for d in range(3):
            print("global barco_" + str(c) + "_" + str(d) + " = Entry(ventana,) ")
           # print("barco_" + str(c) + "_" + str(d) + ".place(x = 15 ,y = " + str(n)+ ") ")
            #print("barco_" + str(c) + "_" + str(d) + ".place_forget() \n")
            n += 50
            
    if c == 4:
        print("global barco_" + str(c) + "_" + str(d) + " = Entry(ventana,) ")
 #       print("barco_" + str(c) + "_" + str(d) + ".place(x = 15 ,y = " + str(n)+ ") ")
  #      print("barco_" + str(c) + "_" + str(d) + ".place_forget() \n")
        n += 50



\nposicion" + str(a)+ "_"+ str(b)+".config(background = agua )


'''
        
