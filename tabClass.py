class Tabla:
    #Constructor
    def __init__(self,name="",cantidad=None,tabla=[]):
        self._name=name
        self._tabla=tabla
        self._cantidad=cantidad

    #Metodos setter y getter cantidad
    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self,value):
        self._cantidad=value
    @cantidad.deleter
    def cantidad(self):
        del self._cantidad

    #Metodos setter y getter Name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
    @name.deleter
    def name(self):
        del self._name

    #Metodos setter y getter Tabla
    @property
    def tabla(self):
        return self._tabla

    @tabla.setter
    def tabla(self,value):
        self._tabla=value

    @tabla.deleter
    def tabla(self):
        del self._tabla

    #print data
    def printTab(self):
        return(f'''Tabla: {self._name}:
 {self.tabla}''')