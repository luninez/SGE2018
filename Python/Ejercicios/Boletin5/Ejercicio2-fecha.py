from datetime import datetime, date, time, timedelta

class Fecha():
    def __init__(self, dia, mes, anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes
    
    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio

    def __tc__(self):
        self.dia = input('Introduzca el dia: ')
        self.mes = input('Introduzca el mes: ')
        self.anio = input('Introduzca el año: ')
        return self.__init__(self.dia, self.mes, self.anio)

    def anio_bisiesto(self):
        if(a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
            return True

    def valida(self):
        if(self.anio >= 1900 and self.anio <= 2050):
            if(self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 8 or self.mes == 10 or self.mes ==12):
                if(self.dia >= 1 and self.dia <= 31):
                    return True
                else:
                    self.dia = 1
            elif(self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11):
                if(self.dia >= 1 and self.dia <= 30):
                    return True
                else:
                    self.dia = 1
            elif(self.mes == 2):
                if(self.anio_bisiesto(anio)):
                    if(self.dia >= 1 and self.dia <= 29):
                        return True
                    else:
                        self.dia = 1
                else:
                    if(self.dia >= 1 and self.dia <= 28):
                        return True
                    else:
                        self.dia = 1
            else:
                self.mes = 1
        else:
            self.anio = 1900

    def corta(self):
        return str(self.dia) + '-' + str(self.mes) + '-' + str(self.anio)

    def larga(self):
        return self.dia_semana() +' '+ str(self.dia) +' de '+ self.mes_anio() + ' de ' + str(self.anio)

    def sumar_dias(self, dia):
        dias = timedelta(days=dia)
        fecha = datetime.datetima(1900,1,1,0,0,0)
        return fecha+dias

    def dias_transcurridos(self):
        d1 = datetime.datetime(1900,1,1,0,0,0)
        return (self - d1).days

    def dia_semana(self):
        
        dicdias = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves', \
        'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}
        
        fecha = datetime.date(int(self.anio), int(self.mes), int(self.dia))
        return (dicdias[fecha.strftime('%A').upper()])

    def mes_anio(self):
        mes = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        
        return mes[self.month+1]

    def dia_mes(self, mes):
        if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes ==12):
           return 31
        elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
            return 30
        elif(mes == 2):
            if(self.anio_bisiesto(datetime.now().year)):
                return 29
            else:
                return 28
        else:
            print('Ese mes no existe.')
            mes = input('Por favor, introduzca uno valido (1-12): ')
            return self.dia_mes(mes)