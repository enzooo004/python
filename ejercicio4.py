### Strings o cadenas de texto
nombre="Tu nombre"
apellido="Tu apellido"
print(nombre + ""+ apellido)
texto= "Este texto \n tiene slato de linea y \t tabulacion"
print(texto)
# formateo
user, password, email = "fer   ", 54321, "fer@fer.com"
print("Su usuario y contraseña son {}{} y su email {}". format(user, password, email))
print("Su usuario y contraseña son %s %d y su email es %s"%(    user, password,email))
print("Su usuario y contraseña son " + user + "" + str(password)+ "y su email es"+ email)
print(f"Su usuario y su contraseña  {user}{password}y email{email}son")