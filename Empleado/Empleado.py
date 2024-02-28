from fecha import Fecha 


class empleado: 

    # Aqui va el codigo del empleado
    # Atributos

    nombre= ""
    apellido= ""

    sexo= "masculino"
    #1= Masculino y 2= Femenino

    salario= 0

    #Asociaciones

    FechaNacimiento = Fecha()
    FechaIngreso = Fecha()

    # Metodos
    def CambiarSalario(self,nuevoSalario):
        #Aqui va el codigo del metodo
        return 0
    
    def CambiarEmpleado(self,nNombre,nApellido,nSexo,nSalario):
        #Aqui va el codigo el nuevo empleado
        return None 
    
    def ConsultarSalario(self):
        #Aqui va el codigo del metodo
        return self.salario 
    
    def ConsultarNombre(self):
        #Aqui va el codigo del metodo
        return self.nombre 
    
    def ConsultarApellido(self):
        # Aqui va el codigo del metodo
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        # Aqui va el codigo del metodo 
        return self.nombre+" "+self.apellido
    
    def AumentoSalario(self):
        nSalario= self.salario * 00.5
        nSalario= nSalario + self.salario
        self.salario=nSalario
        return "El nuevo salario es de:"+self.salario
    def DuplicarSalario(self):
        # Aquiva el codigo del metodo 
        # forma 1
        # self.salario = self
        # forma 2 pro 
        self.salario = 2
    def SalarioAnual(self):
        # Aqui va el codigo 
        # forma 1
        SalarioAnual = self.salario*12
        return SalarioAnual
        # forma 2
        # return self.salario*12
    
    def ConsultarDiaCumpleaños(self):
        return"El dia de su cumpleaños es:"+self.FechaNacimiento.ConsultarDia()
    
    def CalcularImpuesto(self):

        # forma 1
        total = self.CalcularSalarioAnual()
        return(total * 19.5)/100

    
    




    
