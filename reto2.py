"""
Sistema de autentificación que permite registrar, autenticar y gestionar usuarios con diferentes roles:

Usuarios: Pueden:
                    -Ingresar Usuario 
                    -Ingresar Contraseña (Tanto si el user o la clave son incorrectas "Mandar mensaje de Error para cada una de ellas")
                    -Crear nuevo usuario
                    -Salir

(Super usuario)Administradores: Pueden:
                                        -Crear usuarios
                                        -Eliminar usuario
                                        -Ver listado de usuarios
                                        -Cerrar sesión 
                                        -Salir
(Usuario base)Clientes: Pueden:
                                -Ver productos 
                                -Comprar productos
                                -Cerrar Sesion 
                                -Salir

>>>>>>REQUISITOS<<<<<
-USO DE CLASES PARA USUARIOS(USUARIO) Y ROLES ESPECÍFICOS(ADMIN Y CLIENTE)
-ALMACENAR USUARIOS EN DICCIONARIO INTERNO DEL SISTEMA ({username: objeto_usuario})
-USO DE CONDICIONES PARA CONTROLAR EL FLUJO DE AUTENTIFICACION Y LOS MENÚS POR ROL
-USO DE MÉTODOS POLIMÓRFICOS(MENÚ DIFERENTE SEGÚN TIPO DE USUARIO)
-VALIDACIÓN DE ENTRADA POR PARTE DEL USUARIO(VERIFICAR SI YA EXISTE O SI LA CONTRASEÑA ES INCORRECTA[Lanzar error diferente si hay un usuario con esa key pero la clave es incorrecta] )


EL MENÚ DEBE VERSE ASÍ:

----Sistema de Autenticación----
1. Registrar nuevo usuario (>>Tengo que mirar como hacer que un usuario sea admin o cliente<<)
2. Iniciar sesión (Mandá a menú de usuario y contraseña)
3. Salir
"""
class Usuario:
    def __init__(self, username, password, rol):
        self.username = username
        self.password = password
        self.rol = rol
    
    def menu(self):
        pass

                

                 

class Admin(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def menu(self,opcion):

        while True:
            print("----Menú de Admin----\n1. Ver Usuarios\n2. Eliminar Usuarios\n3. Cerrar Sesión")
            choose = input("Por favor, seleccione su opción usando '1, 2 o 3': ")

            if choose == "1":
                opcion.mostrar_usuarios()

            elif choose == "2":
                user = input("¿Qué usuario desea eliminar?: ")
                opcion.eliminar_usuarios(user)
            elif choose == "3":
                print("Hasta pronto!")
                break
            else:
                print("Valor incorrecto")

class Cliente(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password, "Cliente")

    def menu(self,opcion=None):
        while True:
            print("----Menú de Usuario----\n1. Ver Productos\n2. Realizar Compra\n3. Cerrar sesión")

            choose = input("Por favor, seleccione su opción usando '1, 2 o 3': ")
            
            if choose == "1":
                print("----Catálogo----\n1.Street Fighter II  40€\n2.Plants vs Zombies 10€ \n3.Sonic and Knuckles 45€")

            elif choose == "2":
                print("Compra realizada")
            elif choose == "3":
                print("Gracias por usar nuestros servicios!")
                break
            else:
                print("Valor incorrecto")

class SistemaAutenticacion:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self):
        print("Registro de nuevo usuario")
        username = input("Ingrese el nombre de usuario: ")

        if username in self.usuarios:
            print("Este usuario ya ha sido registrado")
            return
        print("Ingrese su contraseña")
        password = input("Contraseña: ")
        rol = input("Rol (admin/cliente): ").lower()

        if rol == "admin":
            self.usuarios[username] = Admin(username, password)
        elif rol == "cliente":
            self.usuarios[username] = Cliente(username, password)
        else:
            print("No ha seleccionado un Rol válido")
            return

        print("Usuario registrado correctamente.")

    def iniciar_sesion(self):
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        usuario = self.usuarios.get(username)

        if not usuario:
            print("Este usuario no existe")
            return

        if usuario.password != password:
            print("Contraseña incorrecta.")
            return

        print(f"Bienvenido, {usuario.username} ({usuario.rol})")
        usuario.menu(self)

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return

        print("\nUsuarios registrados:")
        for username, usuario in self.usuarios.items():
            print(f"- {username} ({usuario.rol})")

    def eliminar_usuario(self, username):
        if username in self.usuarios:
            del self.usuarios[username]
            print("Usuario eliminado.")
        else:
            print("El usuario no existe.")

    def menu_principal(self):
        while True:
            print("\n---- Sistema de Autenticación ----")
            print("1. Registrar nuevo usuario")
            print("2. Iniciar sesión")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.iniciar_sesion()
            elif opcion == "3":
                print("Saliendo del sistema.")
                break
            else:
                print("Opción inválida.")


sistema = SistemaAutenticacion()
sistema.menu_principal()