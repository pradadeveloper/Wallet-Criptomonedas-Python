# Wallet-Criptomonedas-Python
Trabajo final de Wallet de Criptomonedas en Python Next U
Mi Billetera Digital de Criptomonedas 
Una de las tendencias actuales que están teniendo las personas en todo el mundo consiste en llevar cada vez menos dinero en efectivo en sus billeteras o monederos. Las causas son diversas, entre éstas podemos citar: seguridad, comodidad, falta de tiempo para sacar efectivo, entre otros.
Adicionalmente, la tecnología ha jugado un papel fundamental en este contexto, ya que ofrece la plataforma necesaria para realizar los pagos sin necesidad de contar con dinero en efectivo, lo cual es factible a través del uso tradicional de tarjetas de crédito o débito; pero además, cada vez más popularizado, a través del uso de billeteras o monederos digitales.
Un monedero o billetera digital, también se conoce como e-wallet por su nombre en inglés, es un software que permite almacenar fondos en plataformas electrónicas; así como realizar transacciones de pago de bienes y servicios, y recibir pagos de otras fuentes; todo esto es posible realizarlo en línea, a través de Internet. Estos monederos o billeteras digitales funcionan como cuentas de custodia electrónica que actúan como depositarios de fondos en distintos tipos de monedas o hasta cupones electrónicos.
Uno de los usos más comunes de estos monederos son la gestión de las criptomonedas; en tal sentido, se utilizan para guardar, recibir y enviar criptomonedas. Una de las principales características que debe cumplir una billetera digital es la seguridad que proporcione a sus usuario.
En general, las billeteras digitales pueden trabajar con divisas digitales (dólar, euro, pesos) y/o con criptomonedas (bitcoin, etherium, entre otras). Cuando se trabaja con divisas, comúnmente se utiliza la dirección de correo electrónico para realizar una transferencia. Mientras que al trabajar con criptomonedas es necesario el uso de claves y direcciones encriptadas. Además, una billetera puede ser compatible con una sola criptomoneda o también puede ser multicriptomonedas.
Hay distintos tipos de billeteras y diferentes formas de guardar y acceder a las criptomonedas. Aunque se pueden establecer tres tipos de categorías básicas: software, hardware y papel. A su vez las billeteras de software pueden dividirse en desktop, móvil u online. A continuación te describimos brevemente cada uno de estos tipos:
Tipo	Descripción
Desktop	Estas billeteras son descargadas e instaladas en un computador. Son accesibles desde la computadora donde fueron descargadas. Ofrecen un alto nivel de seguridad; sin embargo, si tu computadora es hackeada o se instala un virus hay una gran posibilidad de que pierdas todos tus fondos.
Móvil	A diferencia de las billeteras desktop, éstas se ejecutan en un dispositivo móvil. Pueden ser utilizadas en cualquier lugar, por ejemplo en una tienda en donde quieras hacer un pago.
Online	Se ejecutan en algún servidor y son accedidas por cualquier dispositivo en cualquier lugar. Puedes consultarlas en todo momento pero al estar almacenadas las claves privadas por un tercero, son más vulnerables ante un ataque.
Hardware	Este tipo de billetera almacena las claves privadas en un dispositivo hardware como una memoria USB. Las billeteras hardware pueden hacer transacciones online, pero se almacenan de forma offline lo que incrementa su seguridad. Estas son compatibles con muchas interfaces web y pueden soportar diferentes monedas.
Papel	Estas son las más fáciles de utilizar y proveen la mayor seguridad de todas. Las billeteras de papel pueden consistir en una copia escrita a mano o impresa de la clave privada o un software que se utiliza para generar de forma segura un par de claves que luego se imprimen. La transferencia de moneda a tu billetera de papel se realiza mediante la transferencia de fondos desde una billeteras de software a la dirección pública que se muestra en su billetera de papel.

Alternativamente, si se desea retirar o gastar dinero, todo lo que se necesita hacer es transferir fondos de tu billetera de papel a tu billetera de software. Este proceso a menudo se denomina “barrido”, que se puede hacer manualmente ingresando tu clave privada o escaneando el código QR en la billetera de papel.
Para que puedas revisar algunos ejemplos de billeteras digitales existentes, como referencia, te ofrecemos www.binance.com y www.blockchain.com/es/wallet.
 
1.	Luego de esta introducción al mundo de las criptomonedas y las billeteras digitales, te proponemos como proyecto final del curso Fundamentos de Programación Python que desarrolles tu propia billetera digital de tipo Desktop con interfaz de texto, que soporte monedas registradas en coinmarketcap.com, y que permita:
1.	Enviar un monto en USD de alguna de las criptomonedas a un destinatario indicado (identificado por un código)
2.	Recibir de un enviador (identificado por un código) una cantidad de alguna criptomoneda
3.	Consultar el balance de cada una de las criptomonedas en USD
4.	Consultar el balance general del usuario en USD usando el precio de la criptomoneda provisto por las APIs de coinmarketcap.com
5.	Emitir un histórico de transacciones del usuario indicando fecha, moneda, cantidad y monto en USD para el momento de la transacción
6.	Todas las transacciones realizadas por el usuario deben ser almacenadas y mantenidas, así como las cantidades de cada una de las criptomonedas que posea
Colocar un menú de opciones con:
7.	Recibir cantidad:
	Solicitar moneda, cantidad a recibir, así como el código.
	Validar moneda, cantidad y código, éste debe ser diferente al propio.
	Sumar cantidad de monedas al saldo.
8.	Transferir monto:
	Solicitar moneda, monto y código del destinatario a enviar.
	Validar.
	Restar cantidad de monedas al saldo.
9.	Mostrar balance una moneda:
	Solicitar la moneda a mostrar
	Validar existencia de la moneda.
	Mostrar nombre de la moneda, cantidad y monto en USD para ese momento.
10.	Mostrar balance general:
	Mostrar nombre de cada moneda, cantidad y monto en USD para ese momento.
	Mostrar monto total en USD de todas las monedas.
11.	Mostrar histórico de transacciones:
	Mostrar todas las transacciones indicando fecha, moneda, tipo de operación, código del usuario, cantidad y monto para el momento.
12.	Salir del programa
Recuerda hacer las validaciones de las monedas, de los montos, del saldo y de los códigos.
Consideraciones especiales:
13.	Para hacer uso de las APIs de coinmarketcap.com se debe usar un API key, que se obtiene al registrase en: https://coinmarketcap.com/api/ usando el plan Basic que es gratuito.
14.	Luego de registrase ingresar a https://pro.coinmarketcap.com/account, colocar el ratón  sobre la sección API Key (Asteriscos) y dar click en el botón COPY KEY.
15.	En el código Python usar una variable headers, para pasar los parametros de autenticación con el API Key. Por ejemplo:
headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  'COLOCAR API KEY COPIADA'}
JavaScript
16.	En la invocación del método get además del URL se deben pasar el headers y los parametros que sean necesarios. Por ejemplo:
parametros = {'symbol': symbol}
requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros)
JavaScript
En esta experiencia podrás aplicar todos los conceptos vistos en el curso y, además , podrás reutilizar la mayoría de las soluciones que has incorporado en tu portafolio a lo largo de todo este camino de aprendizaje que has recorrido en este curso ¡Éxito!

