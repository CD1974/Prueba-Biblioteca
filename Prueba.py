class Autor:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
    def GetNombre(self):
        return self.__Nombre
    def GetApellidos(self):
        return self.__Apellidos
    def SetNombre(self,nombre):
        self.__Nombre = nombre
    def SetApellidos(self,apellidos):
        self.__Apellidos = apellidos

class Libro:
    def __init__(self):
        self.__Titulo = ""
        self.__ISBN = ""
    def GetTitulo(self):
        return self.__Titulo
    def GetISBN(self):
        return self.__ISBN
    def SetTitulo(self,titulo):
        self.__Titulo = titulo
    def SetISBN(self,ISBN):
        self.__ISBN = ISBN

class Componentes(Autor,Libro):
    def __init__(self):
        self.__Libro = ""

    def MostrarLibro(self):
        print("-----LIBRO-----")
        print("Nombre:",self.GetNombre())
        print("Apellidos:",self.GetApellidos())
        print("Título:",self.GetTitulo())
        print("----------")

class Biblioteca:
    def __init__(self,path):
        self.__ListaLibros = []
        self.__Path = path
    def NumeroLibros(self):
        return len(self.__ListaLibros)

    def CargarLibro(self):
        try:
            fichero = open(r"C:\Users\mjcd1\OneDrive\Escritorio\Biblioteca.txt","r")
        except:
            print("ERROR: No existe el Libro en la Biblioteca")
        else:
            libros = fichero.readlines()
            fichero.close()
            if(len(libros)>0):
                for libro in libros:
                    datos = libro.split("#")
                    if(len(datos)==4):
                        nuevolibro = Componentes()
                        nuevolibro.SetNombre(datos[0])
                        nuevolibro.SetApellidos(datos[1])
                        nuevolibro.SetTitulo(datos[2])
                        nuevolibro.SetISBN(datos[3])
                        self.__ListaLibros = self.__ListaLibros + [nuevolibro]
                print("INFO: Se han cargado un total de ",len(self.__ListaLibros),"libros")

    def IngresoNuevoLibro(self,nuevolibro):
        self.__ListaLibros = self.__ListaLibros + [nuevolibro]

    def GuardarLibros(self):
        try:
            fichero = open(r"C:\Users\mjcd1\OneDrive\Escritorio\Biblioteca.txt","w")
        except:
            print("ERROR: No se puede guardar.")
        else:
            for libro in self.__ListaLibros:
                texto = libro.GetNombre() + "#"
                texto = texto + libro.GetApellidos() + "#"
                texto = texto + libro.GetTitulo() + "#"
                texto = texto + libro.GetISBN() + "#"
                fichero.write(texto)
            fichero.close()

    def MostrarBiblioteca(self):
        print("########## BIBLIOTECA #############")
        for item in self.__ListaLibros:
            item.MostrarLibro()
        print("##################################")

    def BuscarLibroPorNombre(self,nombre):
        listaencontrados = []
        for libro in self.__ListaLibros:
            if libro.GetNombre() == nombre:
                listaencontrados = listaencontrados + [libro]
        return listaencontrados
    def BuscarContactoPorISBN(self,ISBN):
        listaencontrados = []
        for libro in self.__ListaLibros:
            if libro.GetISBN() == ISBN:
                listaencontrados = listaencontrados + [libro]
        return listaencontrados

    def BorrarLibroPorNombre(self,nombre):
        listafinal = []
        for libro in self.__ListaLibros:
            if libro.GetNombre() != nombre:
                listafinal = listafinal + [libro]
        print("Info: ", len(self.__ListaLibros) - len(listafinal)," libros han sido borrados")
        self.__ListaLibros = listafinal

    def BorrarLibroPorISBN(self,ISBN):
        listafinal = []
        for libro in self.__ListaLibros:
            if libro.GetISBN() != ISBN:
                listafinal = listafinal + [libro]
        print("Info: ", len(self.__ListaContactos) - len(listafinal)," libros han sido borrados")
        self.__ListaLibros = listafinal

def ObtenerOpcion(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print("Error: Tienes que introducir un número.")
        else:
            leido = True
        return numero

def MostrarMenu():
    print(""" Menu
1) Mostrar Biblioteca
2) Buscar Libro
3) Añadir Libro a la biblioteca
4) Borrar libro
5) Guardar libro
6) ¿Numero de libros?
7) Salir """)

def BuscarLibros(biblioteca):
    print("""Buscar Contactos:
1)Nombre
2)ISBN
3)Volver""")
    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion("Opción:")
        if opcbuscar == 1:
            encontrados = biblioteca.BuscarLibroPorNombre(input((">Introduce el nombre a buscar:")))
            if len(encontrados) > 0:
                print("########## LIBROS ENCONTRADOS ##########")
                for item in encontrados:
                    item.MostrarLibro()
                print("#######################################")
            else:
                print("INFO: No se han encontrado libros.")
            finbuscar = True
        elif opcbuscar == 2:
            encontrados = biblioteca.BuscarLibroPorISBN(input((">Introduce el ISBN a buscar:")))
            if len(encontrados) > 0:
                print("########## LIBROS ENCONTRADOS ##########")
                for item in encontrados:
                    item.MostrarLibro()
                print("########################################")
            else:
                print("INFO: No se han encontrado libros.")
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True

def ProcesoCrearLibro(biblioteca):
    nuevolibro = Componentes()
    nuevolibro.SetNombre(input((">Introduce el nombre del autor: ")))
    nuevolibro.SetApellidos(input((">Introduce los apellidos del autor:")))
    nuevolibro.SetTitulo(input((">Introduce el título del libro:")))
    nuevolibro.SetISBN(input((">Introduce el ISBN del libro:")))
    biblioteca.IngresoNuevoLibro(nuevolibro)

def BorrarLibro(biblioteca):
    print("""Buscar contactos a borrar por:
1)Nombre
2)ISBN
3)Volver""")
    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion("Opción:")
        if opcbuscar == 1:
            biblioteca.BorrarLibroPorNombre(input((">Introduce el nombre a borrar:")))
            finbuscar = True
        elif opcbuscar == 2:
            biblioteca.BorrarLibroPorISBN(input((">Introduce el ISBN a borrar:")))
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True

def NumeroLibros(biblioteca):
    print("El número de libros en la biblioteca es: ", biblioteca.NumeroLibros())

def Main():
    biblioteca = Biblioteca(r"C:\Users\mjcd1\OneDrive\Escritorio\Biblioteca.txt")
    biblioteca.CargarLibro()
    fin = False
    while not (fin):
        MostrarMenu()
        opc = ObtenerOpcion("Opción:")
        if opc == 1:
            biblioteca.MostrarBiblioteca()
        elif opc == 2:
            BuscarLibros(biblioteca)
        elif opc == 3:
            ProcesoCrearLibro(biblioteca)
        elif opc == 4:
            BorrarLibro(biblioteca)
        elif opc == 5:
            biblioteca.GuardarLibros()
        elif opc == 6:
            NumeroLibros(biblioteca)
        elif opc == 7:
            fin = 1
Main()
