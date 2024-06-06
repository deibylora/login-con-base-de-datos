

def register (user, password):
    datos = open("Basedatos.txt", "r")
    for line in datos:
        stored_user, stored_password =line.split(" , ")
        if user == stored_user and password == stored_password:
            datos.close()
            print("Usuario registrado, intente nuevamente\n")
            return True
        else:
            datos = open("Basedatos.txt", "a")
            datos.write(f"{user} , {password}\n")
            datos.close()
            Resultado = ("Informacion almacenada exitosamente!!!\n")
            return False

"""def login (user, password):
    usuariologin = input("Cual es su usuario? ")
    contrasenalogin = input("Cual es su contrasena? ")
    if  usuariologin == user and contrasenalogin == password:
        return True
    else:
        return False
    """

