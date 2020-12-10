class HerramientasEspecializadas:
    def __init__(self):
        self.__ComponenteRelacionado = ''
    def GetComponenteRelacionado(self):
        return self.__ComponenteRelacionado
    def SetComponenteRelacionado(self, componenterelacionado):
        self.__ComponenteRelacionado = componenterelacionado
    def MostrarHerramientaEspecializada(self):
        print('■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  E S P E C I A L I D A D  ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■\n')
        print('Componente relacionado: ',self.componenterelacionado(),'\n')
        print('■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■\n')

class Herramientas(HerramientasEspecializadas):
    def __init__(self):
        self.__Nombre = ''
        self.__Marca = ''
        self.__DescripcionUso = ''
        self.__Medida = ''
        self.__Estado = ''
    def GetNombre(self):
        return self.__Nombre
    def GetMarca(self):
        return self.__Marca
    def GetDescripcionUso(self):
        return self.__DescripcionUso
    def GetMedida(self):
        return self.__Medida
    def GetEstado(self):
        return self.__Estado
    def SetNombre(self, nombre):
        self.__Nombre = nombre
    def SetMarca(self, marca):
        self.__Marca = marca
    def SetDescripcionUso(self, uso):
        self.__DescripcionUso = uso
    def SetMedida(self, medida):
        self.__Medida = medida
    def SetEstado(self, estado):
        self.__Estado = estado
    def MostrarHerramienta(self):
        print('════════════════════════════════════ H E R R A M I E N T A S ════════════════════════════════════\n')
        print('Nombre: ',self.GetNombre())
        print('Marca: ',self.GetMarca())
        print('Descripcion: ',self.GetDescripcionUso())
        print('Medida: ',self.GetMedida())
        print('Estado: ',self.GetEstado(),'\n')
        self.MostrarHerramientaEspecializada()
        print('══════════════════════════════════════════════════════════════════════════════════════════════════\n')
