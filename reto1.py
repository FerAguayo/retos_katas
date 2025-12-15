"""

Desarrolla un programa en python que permita registrar y gestionar las notas de varios estudiantes.

El sistema debe cumplir las siguientes funcionalidades básicas:
    -Agregar estudiantes: El usuario puede ingresar el nombre de un estudiante y 3 notas (Valores entre 0 y 10)
    -Quitar estudiantes: El usuario podrá eliminar un registro de un estudiante dado el nombre
    -Mostrar estudiantes aprobados: Mostrar solo los estudiantes cuyo promedio sea mayor o igual a 6
    -Buscar estudiante por nombre y mostrar su promedio
    -Mostrar todos los estudiantes 
    -Salir del programa
    -Subirlo a tu GIT

"""
#student_db= [{"name":"name","grades":[grade1,grade2,grade3]}]
student_db=[{"name":"Pepe","grades":[5.0,4.0,3.0]},{"name":"Lucia","grades":[8.0,7.0,10.0]}]


#Agregar estudiantes
def add_student():
    adding = "s" 
    while adding == "s" or adding == "S":
        student = input("Ingresa el nombre del estudiante: ")
        while True:
            try:
                n1 = float (input ("Ingresa la primera nota: "))
                if 0 <= n1 <= 10:
                    break
                else:
                    print("Debes ingresar una nota con valores entre 0 y 10")
            except ValueError:
                print ("Debes introducir números")
        while True:
            try:
                n2 = float (input ("Ingresa la primera nota: "))
                if 0 <= n2 <= 10:
                    break
                else:
                    print("Debes ingresar una nota con valores entre 0 y 10")
            except ValueError:
                print ("Debes introducir números")

        while True:
            try:
                n3 = float (input ("Ingresa la primera nota: "))
                if 0 <= n3 <= 10:
                    break
                else:
                    print("Debes ingresar una nota con valores entre 0 y 10")
            except ValueError:
                print ("Debes introducir números")

        grades = [n1,n2,n3]

        new_student = {"name": student,"grades":grades}

        student_db.append(new_student)

        adding = input ("¿Desea añadir otro alumno?: (s/n) ")

#mostrar todos
def show_all():
    for student in student_db:

        print (student["name"]," ", student["grades"]," Media ponderada: " ,avg_grades(student["grades"]))

#media de las notas

def avg_grades(grades):
    average = round(sum(grades) / len(grades),2)
    return average

#mostrar estudiantes aprobados
def show_approved():
    for student in student_db:
        avg = avg_grades(student["grades"])
        if avg >= 6:
            print (student["name"]," ", student["grades"]," Media ponderada: " ,avg)

#buscar estudiantes
def find_student():
    name = input("Ingrese el nombre a buscar: ")
    found = False

    for student in student_db:
        if student["name"] == name:
            found = True
            print (student["name"]," ",avg_grades(student["grades"]))

    if found == False:
        print("Estudiante no encotrado")

#borrar estudiante
def remove_student():
    name = input("Ingrese el nombre del estudiante a eliminar: ")
    found = False

    for i in range(len(student_db)):
        if student_db[i]["name"] == name:
            found = True
            student_db.pop(i)
            print("Estudiante eliminado")
            break
    if found == False:
        print("Estudiante no encotrado")

#menu con acceso a todas las funciones

def menu():
    while True:

        print(">>>||Use las teclas del 1 al 6 para seleccionar su opción||<<<<\n1) Ingresar alumno\n2) Borra alumno\n3) Mostrar estudiantes aprobados\n4) Buscar estudiante y su promedio\n5) Listado de todos los estudiantes\n6) Salir de la aplicación")

        choose = input ("Qué desea hacer?: ")

        if choose == "1":
            add_student()
        elif choose == "2":
            remove_student()
        elif choose == "3":
            show_approved()
        elif choose == "4":
            find_student()
        elif choose == "5":
            show_all()
        elif choose == "6":
            print("Hasta pronto!")
            break
        else:
            print("No ha ingresado un valor correcto (1-6), por favor vuelva a intentarlo.")

menu()