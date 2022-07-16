from tabulate import tabulate 
import numpy
import os, sys
import time
import math
import calendar
from datetime import timedelta
from datetime import datetime
from email.errors import MessageError





# esta va a ser la base del sistema
salario=()
prestamo=int()
tasainteres= float(0.10)
plazocuotas= int

def solicitar(): 
    print("Solicitud de Prestamos")

    archivo= open('solicitudes.csv', 'a')
    #se creo un archivo para guardar los prestamos
    archiprestamos = open('prestamos.csv', 'a')

    nombre= input('Escriba su nombre completo: ')
    numerocuenta= input('Indique su numero de cuenta: ')
    cedula= (input('Escriba su cedula: '))
    edad= input('Ingrese su edad: ')
    trabajo= input('Lugar de trabajo: ')
    tiempotrabajando= input('Ingrese los años que tiene trabajando: ')
    salario= (input('Escriba su salario actual (mensual): '))
    prestamo= (input('Escriba el monto a solicitar: '))
    plazocuotas = (input ('Ingresa el valor de plazo de cuotas (mensuales): '))
    tasadeinteres = (input('Introduzca la tasa de interes a aplicar: '))

    archivo.write('Nombre: ')
    archivo.write(nombre)
    archivo.write(', ')
    archivo.write('Numero de Cuenta: ')
    archivo.write(numerocuenta)
    archivo.write('\n ')
    archivo.write('Cedula: ')
    archivo.write(cedula)
    archivo.write(', ')
    archivo.write('Edad: ')
    archivo.write(edad)
    archivo.write('\n ')
    archivo.write('Trabajo:')
    archivo.write(trabajo)
    archivo.write(', ')
    archivo.write(tiempotrabajando)
    archivo.write('años')
    archivo.write('\n ')
    archivo.write('Salario: ')
    archivo.write(salario)
    archivo.write('\n')
    archivo.write('PrestamoMonto')
    archivo.write(prestamo)
    archivo.write(', ')
    archivo.write(plazocuotas)
    archivo.write('meses')
    archivo.write(', ')
    archivo.write(tasadeinteres)
    archivo.write(' %')
    archivo.write('\n')
    archivo.write('\n')

    archivo.close()
    
    archiprestamos.write(prestamo)
    archiprestamos.write('\n')
    archiprestamos.close()

    prestamos= int(prestamo)
    plazocuota= int(plazocuotas)
    edad1= int(edad)
    salarioo=int(salario)
    tiempotrabajando1= int(tiempotrabajando)
    
     
    if plazocuota >= 3:
        if plazocuota <= 84:
           if edad1 >= 20 and edad1 <= 79:
                if tiempotrabajando1 >= 1:
                    #prueba
                    prestamos= int(prestamo)
                    otras_propiedades = int (input ('Ingresa el valor de otras propiedades: '))
                    salario_anual = salarioo*12
                    print ('Selecciona el valor de historia crediticia.')
                    print ('\t1.- buena')
                    print ('\t2.- mala')
                    sys.stdout.write ('\t')
                    historia_crediticia = 0

                    while historia_crediticia<1 or historia_crediticia>2:
                        historia_crediticia = int (input (': '))
                    if historia_crediticia<1 or historia_crediticia>2:
                        sys.stdout.write ('Valor incorrecto. Ingr\u00E9salo nuevamente.')
                            
                    puntos=0
                    if salario_anual>=prestamos*int(0.5):
                        puntos=puntos+5
                    if salario_anual>=prestamos*int(0.25) and salario_anual<prestamos*int(0.5):
                        puntos=puntos+3
                    if salario_anual>=prestamos*int(0.1) and salario_anual<prestamos*int(0.25):
                        puntos=puntos+1
                    if otras_propiedades>=prestamos*2:
                        puntos=puntos+5
                    if otras_propiedades>=prestamos and otras_propiedades<prestamos*2:
                        puntos=puntos+3
                    if historia_crediticia==1 and puntos>6:
                        print ('Pr\u00E9stamo aprobado')
                            
                    else:
                        print ('Pr\u00E9stamo rechazado')
                        print ('Nombre: ' + nombre)
                        print ('Valor de puntos: ' + repr (puntos))
                        print ()
                        os.system ('pause')

                            #hasta aqui


def tabla():

    numero = int(input("Digite su cedula: "))

    print(f"Es correcto {numero}")
    print("prestamo Bancario")
    prestamo = float(input("Digite el monto del prestamo: "))
    tiempo = int(input("Plazo del prestamo (meses): "))
    interesAnual = float(input("Interes a aplicar al prestamo: "))
    #formula para la cuota fija
    interesMensual = (interesAnual/12)/100
    cuota = ((prestamo* interesMensual)/(1-(math.pow((1+interesMensual),(tiempo*-1)))))
    pagototal= cuota * tiempo
    interestotales=cuota*tiempo
            
    fecha= "2022-04-22"
    ahora = datetime.strptime(fecha, '%Y-%m-%d')
    fechadepago= ahora + timedelta(days=25)
    print("")
    print("   Interes Anual: ",interesAnual,"%","\t\t","Monto: $", prestamo,  )
    print("   Plazo Meses: ",tiempo,"\t\t" ,"Pago Total", pagototal)
    print("Monto Total Intereses: ", interestotales)
    print("{:^10}{:^10}{:^10}{:^12}{:^10}{:^15}" . format("N°", "Cuota","Interes","Amortizacion", "saldo", "Fecha de Pago"))
    nuevosaldo= prestamo 
    
    mes= 1
    for i in range (tiempo+1):
        if(i==0):
            print("{:^10}{:^10}{:^10}{:^12}{:^10}{:}" . format(mes," "," "," ",prestamo,fechadepago))
        else:
            # desde aqui empezo la prueba
            while mes >= tiempo:
                print(mes+1)
            pagoInteres = nuevosaldo*interesMensual
            Amortizacion = cuota-pagoInteres
            nuevosaldo = nuevosaldo-Amortizacion
            fecha= "2022-04-22"
            ahora = datetime.strptime(fecha, '%Y-%m-%d')
            fechadepago= ahora + timedelta(days=25)
            
            print("{:^10d}{:^10.2f}{:^10.2f}{:^12.2f}{:^10.2f}{}" . format(mes,cuota,pagoInteres,Amortizacion,nuevosaldo, fechadepago))
        
            

#declarando variables duras
#La fecha de pago sera cada 25 dias despues de aceptar el prestamo

    # ponerle un while
    

  #Pago de prestamo
# declarando la belleza de funcion pago de prestamo
def pagoprestamo():
    archivito = open('prestamos.csv','r')
    contenido= archivito.readlines()
    print("Pago de prestamos")
    

    prestamo= int(contenido[1])
    print('El monto del prestamo es: ' + str(prestamo)+ '/n' )
    print('')

    time.sleep(2)
    os.system('cls')
    
    tasainteres= int(input("Introduzca la tasa de interes del prestamo  "))
    interestasa= float(tasainteres/100)
    intereses= prestamo*interestasa
    pagocancelprestamo= intereses + prestamo
    time.sleep(2)
    os.system('cls')
    print("Debe de pagar este monto: "+ str(pagocancelprestamo))
                   

#Consulta de clientes
def consulta():
    print("Consulta de clientes \n")
    archivo= open("solicitudes.csv", "r")
    print(archivo.read())

    archivo.close()
    
#cancelacion de prestamo
def cancelacion():
    print("Cancelacion de prestamos")
    monto_prestamo= int(input("Introduzca el monto del prestamo a cancelar"))
    tasainteres= int(input("Introduzca la tasa de interes"))
    interestasa= float(tasainteres/100)
    intereses= monto_prestamo*interestasa
    pagocancelprestamo= intereses + monto_prestamo
    print("Debe de pagar este monto"+ str(pagocancelprestamo))

    #se debe conocer el  monto del prestamo
    #se debe calcular el interes 
    #conocer la tasa de interes

    print("Su cancelación ha sido exitosa")


def historial():
    datos =[["N°","Fecha","Prestamo ","Amortizacion","Saldo"],
    ["1","20/Noviembre/2008","50,000 RD$","","50,000"],
    ["2","21/Junio/2009","","4,000 RD$","46,000"],
    ["3","05/Julio/2009","","2,000 RD$","44,000"],
    ["4","18/Julio/2009","","1,500 RD$","42,500"],
    ["5","16/Septiembre/2009","","700 RD$","41,800"],
    ["6","20/Septiembre/2009","","600 RD$","41,200"],
    ["7","04/Octubre/2009","","1,300","39,900"],
    ["8","24/Octubre/2009","","1,000 RD$","38,900"],
    ["9","26/Diciembre/2009","","1,500 RD$","37,400"],
    ["10","01/Enero/2010","","1,500","35,900"],
    ["11","21/Mayo 10/2010","","1,200 RD$","34,700"],
    ["12","23/Agosto/2010","","1,500","33,200"],
    ["13","26/Septiembre/2010","1,500","","34,700"],
    ["14","02/Enero/2011",""," 2,500RD$","32,200"],
    ["15","22/Abril/2011","","2,000 RD$","30,200"],
    ["16","02/Mayp/2011","","1,500 RD$","28,700"],
    ["17","12/Mayo/2012","","2,500 RD$","26,200"],
    ["18","01/Mayo/2012","","500 RD$","25,000"],
    ["19","17/Sep/2011","","700 RD$","25,000"],
    ["20","14/Octubre/2012","","2,000 RD$","23,000"],
    ["21","14/Octubre/2012","4,000","","27,000"],
    ["","Total","55,500","28,500",""]
    ]
    print(tabulate(datos))

def estado():
    archivito = open('prestamos.csv','r')
    contenido= archivito.readlines()
    print("Pago de prestamos")
    print(contenido)
    
def exit():
    print('Gracias por usar nuestros servicios: ')

#Desde aqui la base...

print('''
      1- Solicitar Prestamo
      2- Imprimir Tabla de Amortizacion
      3- Pago de Prestamo
      4- Cancelación de Prestamo
      5- Consulta de Clientes
      6- Estado de Cuenta de Prestamo
      7- Historial de Pago
      0- salir
      ''')

# Imprime la Tabla de Amortizacion si se valida el prestamo



opcion = int(input('Por favor seleccione la opcion: \n'))

if(opcion == 1):
    solicitar()  

if(opcion == 2):
    tabla()  

if(opcion == 3):
    pagoprestamo()  

if(opcion == 4):
    cancelacion()

if(opcion == 5):
    consulta()

if(opcion == 6):
    estado()

if(opcion == 7):
    historial()

if(opcion == 0):
    exit()
    


