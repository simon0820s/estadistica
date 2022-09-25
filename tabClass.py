class Tabla:
    #Constructor
    def __init__(self,tabla=[]):
        self._tabla=tabla

    #Metodos setter y getter
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
        return(f'''Tabla: {self.tabla}''')