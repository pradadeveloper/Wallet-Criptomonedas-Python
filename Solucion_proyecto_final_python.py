import requests
from datetime import datetime

_ENDPOINT="https://api.binance.com"
almacenamientodatos="almacenamiento_datos.txt"

class Usuario(object):
    def __init__(self, codigo):
        self.codigo = codigo
        
    def mostrarcodigo(self):
        return self.codigo

class Criptomoneda(object):
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def Indicarcantidad(self,cantidad):
        self.cantidad = cantidad
    
    def mostrarnombre(self):
        return self.nombre
    
    def mostrarcantidad(self):
        return self.cantidad
    
    def calcularsaldo(self,cotizacion):
        return  self.cantidad*cotizacion 

#Definir la URL como variable
def _url(api):
    return _ENDPOINT+api

#Obtener el precio actual de la criptomoneda obtenido de la API.
def get_price(cripto):
    data = requests.get(_url("/api/v3/ticker/price?symbol="+cripto)).json()
    precio = float(data["price"])
    return precio

#Definición de la variable Criptomoneda dentro de un listado predefinido de 5 criptos.
def esmoneda(cripto):
    criptos= ["BTC","ETH","BCC","LTC"]
    if cripto in criptos:
        return True
    else:
        print("Moneda no valida.Monedas válidas:[BTC,ETH,BCC,LTC]")

#Validar código de transferencia (Se puede mejorar)
def ValidarCodigo(codigo):
    if codigo == usuario.codigo:
        print("¡Transacción Fallida!, El código es Inválido")
        return False
    else:
        return True
#Definición de la cantidad para transferencias
def cantidadSuficiente(moneda,cantidad):
    aux = True
    if(moneda=="BTC"):
        if(BTC.cantidad>=cantidad):
            return True
        else: 
            aux= False
    if(moneda == "ETH"):
        if(ETH.cantidad>=cantidad):
            return True
        else:
            aux= False
    if(moneda == "BCC"):
        if(BCC.cantidad>=cantidad):
            return True
        else:
            aux= False
    if(moneda== "LTC"):
        if(LTC.cantidad >= cantidad):
            return True
        else:
            aux= False
    if(aux== False):
        print(" ¡TRANSACCIÓN RECHAZADA!, SALDO "+moneda+" ES INSUFICIENTE")
    return False

#GUARDAR_REGISTRO
def GuardarRegistro(moneda, operacion, codigo, cantidad, cantTotal):
    archivo = open(almacenamientodatos,"a")
    dt = datetime.now()
    precio =  get_price(moneda+"USDT")
    archivo.write("\n"+"FECHA"+ ":" + dt.strftime("%A %d/%m/%Y %I:%M:%S%p") +",MONEDA " +":"+str(moneda)+", TRANSACCIÓN " +":"+ operacion+", CÓDIGO USUARIO "+ ":"+ str(codigo) + ",CANTIDAD "+ ":"+ str(cantidad) + ",TOTAL DE OPERACIÓN EN $ "+":"+ str(precio*cantidad) +", TOTAL ACUMULADO EN CUENTA EN $ " + ":"+ str(precio*cantTotal))
    archivo.close()
    return

#Valor de las variables
BTC = Criptomoneda("BTC",2.5)
ETH = Criptomoneda("ETH",1.5)
BCC = Criptomoneda("BCC",11.3)
LTC = Criptomoneda("LTC",9.0)

monedas = [BTC,ETH,BCC,LTC]
usuario = Usuario(1348)

while True:
    print("------------------------------------------------------------")
    print("<<<<<<<<<<<<<<< BILLETERA DIGITAL >>>>>>>>>>>>>>>")
    print("------------------------------------------------------------")
    print("CÓDIGO DE USUARIO: " + str(usuario.mostrarcodigo()))
    print("MENÚ DE OPCIONES: ")
    print(("1. RECIBIR CANTIDAD \n"
           "2. TRANSFERIR DINERO\n"
           "3. MOSTRAR BALANCE DE MONEDA\n"
           "4. MOSTRAR BALANCE GENERAL\n"
           "5. MOSTRAR HISTORIAL DE TRANSACCIONES\n"
           "6. SALIR DEL PROGRAMA"))
    seleccion = int(input("SELECCIONA UNA OPCIÓN PARA CONTINUAR: "))

#1.RECIBIR CANTIDAD Y ESCRIBIR CODIGO BENEFICIARIO
    if(seleccion==1):
        moneda = input("INGRESE LA MONEDA A RECIBIR: ")
        while not esmoneda(moneda):
            moneda = input("INGRESE LA MONEDA A RECIBIR: ")
            cantidad = float(input("INGRESE LA CANTIDAD DE "+moneda+" A RECIBIR:"))
            codigo = int(input("INGRESE CÓDIGO DEL BENEFICIARIO: "))
        while not ValidarCodigo(codigo):
            codigo = int(input("INGRESE CÓDIGO DEL EMISOR: "))
        if(moneda=="BTC"):
            BTC.Indicarcantidad(BTC.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad, BTC.mostrarcantidad())
        elif(moneda=="ETH"):
            ETH.Indicarcantidad(ETH.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad,ETH.mostrarcantidad())
        elif(moneda=="BCC"):
            BCC.Indicarcantidad(BCC.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad,BCC.mostrarcantidad())
        elif(moneda=="LTC"):
            LTC.Indicarcantidad(LTC.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad,LTC.mostrarcantidad())
        print("¡TRANSACCIÓN EXITOSA!, EL SALDO FUE AÑADIDO CORRECTAMENTE")
#2.TRANSFERIR DINERO
    elif(seleccion==2):
        moneda = input("INGRESE LA MONEDA A TRANSFERIR: ")
        cantidad=float(input("INGRESE LA CANTIDAD A TRANSFERIR DE "+moneda+": "))
        while not cantidadSuficiente(moneda,cantidad):
            cantidad = float(input("INGRESE LA CANTIDAD A TRANSFERIR DE "+moneda+": "))
            codigo = int(input("INGRESE EL CÓDIGO DEL BENEFICIARIO: "))
        if(moneda=="BTC"):
            BTC.Indicarcantidad(BTC.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad, BTC.mostrarcantidad())
        elif(moneda=="ETH"):
            ETH.Indicarcantidad(ETH.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad, ETH.mostrarcantidad())
        elif(moneda=="BCC"):
            BCC.Indicarcantidad(BCC.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad, BCC.mostrarcantidad())
        elif(moneda=="LTC"):
            LTC.Indicarcantidad (LTC.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad, LTC.mostrarcantidad())
        print("¡TRANSACCIÓN EXITOSA!, El saldo fue descontado correctamente de su billetera")
        
#3.MOSTRAR BALANCE DE LA MONEDA:
    elif(seleccion == 3):
        moneda = input("INGRESE LA MONEDA A CONSULTAR: ")
        while not esmoneda(moneda):
            moneda = input(" INGRESE LA MONEDA A CONSULTAR: ")
        precio= get_price(moneda+"USDT")
        if(moneda=="BTC"):
            print("Moneda: "+ moneda+ " Cantidad: "+ str(BTC.mostrarcantidad()) + " Saldo Disponible: $"+ str(BTC.calcularsaldo(precio)))
        elif(moneda=="ETH"):
            print("Moneda: " + moneda + " Cantidad: "+str(ETH.mostrarcantidad()) +" Saldo disponible: $"+str(ETH.calcularsaldo(precio)))
        elif(moneda=="BCC"):
            print("Moneda: " + moneda + " Cantidad: "+str(BCC.mostrarcantidad()) + " Saldo disponible: $"+str(BCC.calcularsaldo(precio)))
        elif(moneda=="LTC"):
            print("Moneda: " + moneda + " Cantidad: "+ str(LTC.mostrarcantidad()) +" Saldo disponible: $"+str(LTC.calcularsaldo(precio)))
#4.MOSTRAR BALANCE GENERAL
    elif(seleccion==4):
        moneda = ""
        totalUSD = 0
        for moneda in monedas:
            precio = get_price(moneda.mostrarnombre()+"USDT")
            totalUSD += moneda.calcularsaldo(precio)
            print("Moneda: " + moneda.mostrarnombre() + " Cantidad: "+ str(moneda.mostrarcantidad()) +" Saldo disponible: $."+ str(moneda.calcularsaldo(precio)) +"\n")
        print("EL MONTO ACUMULADO TOTAL DE TODAS LAS CRIPTOMONEDAS SON $." + str(totalUSD))
#5.MOSTRAR HISTORIAL DE LAS TRANSACCIONES
    elif(seleccion==5):
        archivo = open(almacenamientodatos,"r")
        texto = archivo.read()
        archivo.close()
        lineas = texto.splitlines()
        print(texto)
    elif(seleccion==6):
        print("\nFELIZ DIA, GRACIAS POR SU PREFERENCIA")
        break
    else:
        print("\nPOR FAVOR, SELECCIONE UNA OPCIÓN VÁLIDA")