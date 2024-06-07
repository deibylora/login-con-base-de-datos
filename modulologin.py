
def login (user, password):
    with open ("Base_datos.txt", "r") as datos:
        for line in datos:
            stored_user, stored_password = line.strip().split()
            if user == stored_user and password == stored_password:
                return f"Bienvenido: {user}"
        if user != stored_user and password != stored_password:
            return F"Usuario o contraseña incorrecta, intente nuevamente"
            
def registro (user, password):
    with open ("Base_datos.txt", "a+") as datos:
        for line in datos:
            
            stored_user, _ = line.strip().split()
            if user == stored_user:
                return ("Usuario ya existe, intente otro")
        datos.write(f"{user},{password}\n")
        return f"Gracias por registrarse {user}"

    

         

