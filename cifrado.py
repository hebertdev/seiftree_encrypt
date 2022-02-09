"""Script para realizar un cifrado de texto.
Para este ejemplo utilizaremos dos librerias,
para ejecutar este codigo debes instalar un entorno virtual
e instalar las librerias.
1: CRYPTOGRAPHY
pip install cryptography
2: PASSLIB
pip install passlib
"""

#IMPORTAMOS LAS DOS LIBRERIAS
from passlib.context import CryptContext
from cryptography.fernet import Fernet

#Parametros de como se va a realizar nuestro cifrado
contexto = CryptContext(
	schemes=["pbkdf2_sha256"],
	default="pbkdf2_sha256",
	pbkdf2_sha256__default_rounds=20
	#pbkdf2_sha256__default_rounds=2000
	#pbkdf2_sha256__default_rounds=200000
	#dependiendo de como querramos configuramos para que se más seguro
)

def Cifrado():
	"""
	Primero generaremos una llave secreta , pero en nuestro sistema
	no lo guardaremos como texto plano
	"""
	llave_secreta = '153214' #Esto jamás guardamos en la base de datos


	"""
	Una vez que recibimos la llave secreta 
	pasamos a cifrarla para recien guardarlo en 
	nuesta base de datos
	"""
	llave_secreta_encriptada = contexto.hash(llave_secreta)
	print('')
	print('tu clave se ha encriptado: ' +  llave_secreta_encriptada)
	"""Ese resultado si lo guardamos en nuestra base de datos ,
	para despues validar con lo que nos envia el usuario
	"""
	print('')


	#key unico para cifrar 
	objecto_cifrado = Fernet(Fernet.generate_key())

	"""creamos las cadenas de texto que querramos cifrar"""
	email_a_cifrar = 'developer@gmail.com'
	password_a_cifrar = 'holamundo159@#A'

	"""cadenas de texto cifradas"""
	email_cifrado = objecto_cifrado.encrypt(str.encode(email_a_cifrar))
	password_cifrado = objecto_cifrado.encrypt(str.encode(password_a_cifrar))

	print('El email y la contraseña han sido cifradas')
	print('EMAIL: ')
	print(email_cifrado)
	print('PASSWORD: ')
	print(password_cifrado)
	print('')
	#esos resultados cifrados lo guardamos en la base de datos


	"""Paara descifrar los datos tenemos que mandarle nuestra llave secreta
	que generamos al inicio , y verificarla si es correcta"""

	#condicion para validar si la clave secreta es igual al cifrado
	if contexto.verify(llave_secreta, llave_secreta_encriptada):
		"""si nos da true vamos a desencriptar las cadenas"""
		print('Tu llave secreta es correcta:')
		email_desencriptado = objecto_cifrado.decrypt(email_cifrado).decode()
		password_desencriptado = objecto_cifrado.decrypt(password_cifrado).decode()
		print('EL EMAIL ES: ' + email_desencriptado)
		print('EL PASSWORD ES: ' + password_desencriptado)
	else:
		print('llave secreta incorrecta')



if __name__ == '__main__':
	Cifrado()


"""Estos resultados cambian de manera aleatoria.
OUTPUT:

tu clave se ha encriptado: $pbkdf2-sha256$30$gtAao1SqtdY6R4iR0jrH2A$U6S5JgLzdUxpLVWxfb9h5lKv1fWSu.7WJot/gQn3nuI

El email y la contraseña han sido cifradas
EMAIL: 
b'gAAAAABhuPHCrP8BZhJlz1Od8CIl6z8aC_dafKP6RELzShtR5Y8FB1SnGID27Tw3JJBbtFtbmnTmgfrCYRq6OoHNs641JDlriqk9trsQu4hf1TujqvxpJTw='
PASSWORD: 
b'gAAAAABhuPHCeAIIraa20bA5_nXok6nDjMJDsYAWZZTYXa9J2yuLhbxodu1RRwUk8VD103pSpaT6vvj0SSnOsdoJfSuPkl9z7w=='

Tu llave secreta es correcta:
EL EMAIL ES: developer@gmail.com
EL PASSWORD ES: holamundo159@#A
"""