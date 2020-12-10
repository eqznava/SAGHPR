class HerramientasEspecializadas:
    def __init__(self):
        self.__ComponenteRelacionado = ''
    def GetComponenteRelacionado(self):
        return self.__ComponenteRelacionado
    def SetComponenteRelacionado(self, componenterelacionado):
        self.__ComponenteRelacionado = componenterelacionado
    def MostrarHerramientaEspecializada(self):
        print('■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  H E R R A M I E N T A  E S P E C I A L I Z A D A  ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■\n')
        print('Componente relacionado: ',self.GetComponenteRelacionado(),'\n')
        print('■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■\n')

class HerramientasMedicion:
    def __init__(self):
        self.__NombreMedicion = ''
        self.__Rango = ''
        self.__Precision = ''
        self.__UnidadesMedicion = ''
        self.__FechaCalibracion = ''
        self.__FechaRecalibracion = ''
        self.__IDCalibrador = ''
    def GetNombreMedicion(self):
        return self.__NombreMedicion
    def GetRango(self):
        return self.__Rango
    def GetPrecision(self):
        return self.__Precision
    def GetUnidadesMedicion(self):
        return self.__UnidadesMedicion
    def GetFechaCalibracion(self):
        return self.__FechaCalibracion
    def GetFechaRecalibracion(self):
        return self.__FechaRecalibracion
    def GetIDCalibrador(self):
        return self.__IDCalibrador
    def SetNombreMedicion(self, nombremedicion):
        self.__NombreMedicion = nombremedicion
    def SetRango(self, rango):
        self.__Rango = rango
    def SetPrecision(self, precision):
        self.__Precision = precision
    def SetUnidadesMedicion(self, unidadesmedicion):
        self.__UnidadesMedicion = unidadesmedicion
    def SetFechaCalibracion(self, fechacalibracion):
        self.__FechaCalibracion = fechacalibracion
    def SetFechaRecalibracion(self, fecharecalibracion):
        self.__FechaRecalibracion = fecharecalibracion
    def SetIDCalibrador(self, idcalibrador):
        self.__IDCalibrador = idcalibrador
    def MostrarHerramientaMedicion(self):
        print('­­­­­░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░  H E R R A M I E T A S  M E D I C I O N  ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░\n')
        print('Nombre: ',self.GetNombreMedicion())
        print('Rango: ',self.GetRango())
        print('Precision: ',self.GetPrecision())
        print('Unidades de Medicion: ',self.GetUnidadesMedicion())
        print('Fecha de Calibracion: ',self.GetFechaCalibracion())
        print('Fecha de Proxima Recalibracion: ',self.GetFechaRecalibracion())
        print('Id Encargado de Calibracion: ',self.GetIDCalibrador(),'\n')
        print('░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░\n')

class Herramientas(HerramientasEspecializadas,HerramientasMedicion):
    def __init__(self):
        self.__Nombre = ''
        self.__Marca = ''
        self.__DescripcionUso = ''
        self.__Medida = ''
        self.__Estado = ''
        self.__Cantidad = 0
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
    def GetCantidad(self):
        return self.__Cantidad
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
    def SetCantidad(self, cantidad):
        self.__Cantidad = cantidad
    def MostrarHerramienta(self):
        print('════════════════════════════════════ H E R R A M I E N T A S ════════════════════════════════════\n')
        print('Nombre: ',self.GetNombre())
        print('Marca: ',self.GetMarca())
        print('Descripcion: ',self.GetDescripcionUso())
        print('Medida: ',self.GetMedida())
        print('Unidades de Medicion: ',self.GetUnidadesMedicion())
        print('Cantidad a Usar: ',self.GetCantidad())
        print('Estado: ',self.GetEstado(),'\n')
        self.MostrarHerramientaEspecializada()
        self.MostrarHerramientaMedicion()
        print('══════════════════════════════════════════════════════════════════════════════════════════════════\n')

herramientas = Herramientas()
herramientas.SetNombre('Llave Mixta.')
herramientas.SetMarca('Husky.')
herramientas.SetDescripcionUso('Ajustar apriete en tuercas o tornillos.')
herramientas.SetMedida('3/4')
herramientas.SetUnidadesMedicion('Pulgadas.')
herramientas.SetCantidad(2)
herramientas.SetEstado('La herramienta se encuentra en buen estado.')
herramientas.SetComponenteRelacionado('Este no es un componente relacionado.')
herramientas.SetNombreMedicion('Vernier')
herramientas.SetRango('12')
herramientas.SetPrecision('1/32')
herramientas.SetFechaCalibracion('09/12/2020')
herramientas.SetFechaRecalibracion('01/01/2021')
herramientas.SetIDCalibrador('C-001')
herramientas.MostrarHerramienta()
