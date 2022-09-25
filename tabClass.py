class Tabla:
    #Constructor
    def __init__(self,tabla=[],name=""):
        self._name=name
        self._tabla=tabla
    
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