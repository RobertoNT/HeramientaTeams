
def cargarArchivo(ruta):
    ##Carga el archivo de texto pasado en la ruta
        contenido=[]
        try:
            
            with open(ruta, encoding="ANSI") as lectura:
                for line in lectura:
                    contenido.append(line)

        except: print("La ruta no es correcta")
            
            
        return contenido


def filtrarDatos(lista:list,filtro):
   #Filtra los datos según lo que queremos extraer
    
    listaFinal=[]
    
    for linea in lista:
        
        if filtro=="equipo":
            
            if "teamAlias" in linea:
                listaFinal.append(linea)
            if "spaceThreadTopic" in linea:
                listaFinal.append(linea)
            if "visibility"in linea:
                listaFinal.append(linea)
            if "teamSmtpAddress" in lista:
                listaFinal.append(linea)
            if "8:orgid:"in linea:
                listaFinal.append(linea)
            if "8:live:.cid.":
                listaFinal.append(linea)
            if"friendlyName0":
                listaFinal.append(linea)
            if "19 :"in linea:
                listaFinal.append(linea)
            if"membersa"in linea:
                listaFinal.append(linea)
        if filtro=="usuarios":
            if "8:orgid:"in linea:
                listaFinal.append(linea)
            if "8:live:.cid.":
                listaFinal.append(linea)
            if"friendlyName0":
                listaFinal.append(linea)
            if"membersa"in linea:
                listaFinal.append(linea)
        if filtro=="grupos":
            if "G19:"in linea:
             listaFinal.append(linea)

        if filtro=="evento":
            if "no chat"in linea:
                listaFinal.append(linea)
            if "eventTimeZone"in linea:
                listaFinal.append(linea)
            if "categories"in linea:
                listaFinal.append(linea)
            if "organizerName"in linea:
                listaFinal.append(linea)
            if "isAppointmentT"in linea:
                listaFinal.append(linea)
            if "8:orgid:"in linea:
                listaFinal.append(linea)
            if "8:live:.cid.":
                listaFinal.append(linea)
            if"friendlyName0":
                listaFinal.append(linea)
            if "19 :"in linea:
                listaFinal.append(linea)
            if"membersa"in linea:
                listaFinal.append(linea)

                            
        if filtro=="mensaje":
            if "groupTemplate"in linea:
                listaFinal.append(linea)
            if "language"in linea:
                listaFinal.append(linea)
            if "messagetype"in linea:
                listaFinal.append(linea)
            if "imdisplayname"in linea:
                listaFinal.append(linea)
            if "friendlyName"in linea:
                listaFinal.append(linea)
            if "files"in linea:
                listaFinal.append(linea)
            if "8:orgid:"in linea:
                listaFinal.append(linea)
            if "8:live:.cid.":
                listaFinal.append(linea)
            if"friendlyName0":
                listaFinal.append(linea)
            if "19 :"in linea:
                listaFinal.append(linea)
            if"membersa"in linea:
                listaFinal.append(linea)

            
    exportar_archivo("C:\\Users\\rnoguera\\Desktop\\archivo.txt",listaFinal)

def exportar_archivo(ruta,lista):
    ##Crea un nuevo archivo con la información extraida
        
     file = open(ruta, "w",encoding="ANSI")
    
     for i in lista:##Lee cada dato extraido en el método anterior
            file.write(i)
    
     file.close()

def ejecutar():
    ##Almacenar
    
    Ruta=cargarArchivo("C:\\Users\\rnoguera\\AppData\Local\\Microsoft\\Edge\\User Data\\Default\IndexedDB\\https_teams.microsoft.com_0.indexeddb.leveldb\\000249.log")
    print("Indicame que filtro aplico, si no sabes cuales son pulsa help")
    filtro=input("El filtro es :")
    while filtro=="help":
        print ("Según la información que quieres buscar tienes que escribir:  \n mensaje \n evento \n usuarios \n equipo ")
        filtro=input("Introduce que filtro quiere ejecutar: ")
    filtrarDatos(Ruta,filtro)
  
    
ejecutar()