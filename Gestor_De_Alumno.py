class Fecha:

    def __init__(self, fecha: str):
        partes_de_la_fecha: list[str] = fecha.split("/")
        self.dia = int(partes_de_la_fecha[0])
        self.mes = int(partes_de_la_fecha[1])
        self.anio = int(partes_de_la_fecha[2])

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"


class Alumno:

    def __init__(self, nombre, legajo, fecha_nacimiento):
        self.nombre = nombre
        self.legajo = legajo
        self.fecha_de_nacimiento: Fecha = fecha_nacimiento
        self.nota_parcial1 = 0
        self.nota_parcial2 = 0

    def guardar_calificacion_nota_parcial1(self, nota):
        if 1 <= nota <= 10:
            self.nota_parcial1 = nota
        else:
            raise ValueError("La nota debe estar entre 1 y 10")

    def guardar_calificacion_nota_parcial2(self, nota):
        if 1 <= nota <= 10:
            self.nota_parcial2 = nota
        else:
            raise ValueError("La nota debe estar entre 1 y 10")

    def promedio_parciales(self):
        return (self.nota_parcial1 + self.nota_parcial2) / 2

    def estado(self):
        if self.promedio_parciales() < 4:
            return "Desaprobado"
        elif self.promedio_parciales() <= 6:
            return "Regular"
        elif self.nota_parcial1 >= 6 and self.nota_parcial2 >= 6:
            return "Promocionado"
        else:
            return "Regular"

    def generar_texto_de_notas(self):
        texto = "Notas: "
        if self.nota_parcial1 > 0:
            texto += f"1° Parcial -> {self.nota_parcial1} "
        if self.nota_parcial2 > 0:
            texto += f"| 2° Parcial -> {self.nota_parcial2} "
        if self.nota_parcial1 == 0 and self.nota_parcial2 == 0:
            texto = ""
        return texto

    def __str__(self):
        return f"Alumno ({self.legajo}): {self.nombre} - Fecha Nac. {self.fecha_de_nacimiento} {self.generar_texto_de_notas()}"


class Materia:

    def __init__(self, codigo, nombre, horas_semanales):
        self.codigo = codigo
        self.nombre = nombre
        self.horas_semanales = horas_semanales

    def __str__(self):
        return f"Materia ({self.codigo}): {self.nombre} - {self.horas_semanales} hs semanales"

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_horas_semanales(self, horas):
        if horas > 0:
            self.horas_semanales = horas
        else:
            print("Las horas deben ser mayores a 0")


class Inscripcion:

    def __init__(self, alumno, materia):
        self.alumno = alumno
        self.materia = materia

    def __str__(self):
        return f"Inscripción: Alumno ({self.alumno.legajo}) {self.alumno.nombre} -> Materia ({self.materia.codigo}) {self.materia.nombre}"


class GestorDeAlumnos:

    def __init__(self):
        self.alumnos: list[Alumno] = []

    def crear_alumno(self, nombre, legajo, fecha_nac):
        self.alumnos.append(Alumno(nombre, legajo, fecha_nac))

    def cargar_alumnos(self, cantidad=1):
        for i in range(cantidad):
            print(f"---- Cargando el {i+1}° alumno ----")
            nombre = input("Nombre: ")

            while True:
                legajo = int(input("Legajo: "))
                if self.es_un_legajo_valido(legajo):
                    fecha = Fecha(input("Fecha (DD/MM/AAAA): "))
                    self.crear_alumno(nombre, legajo, fecha)
                    break
                else:
                    print("Legajo duplicado")

    def mostrar_alumnos(self):
        print("---- Alumnos ----")
        for a in self.alumnos:
            print(a)

    def modificar_alumno(self):
        legajo = int(input("Legajo: "))
        alumno = self.buscar_alumno(legajo)

        if alumno:
            nombre = input("Nuevo nombre: ")
            if nombre != "":
                alumno.nombre = nombre
        else:
            print("No existe")

    def eliminar_alumno(self):
        legajo = int(input("Legajo: "))
        alumno = self.buscar_alumno(legajo)

        if alumno:
            self.alumnos.remove(alumno)
            print("Eliminado")
        else:
            print("No existe")

    def es_un_legajo_valido(self, legajo):
        return self.buscar_alumno(legajo) is None

    def buscar_alumno(self, legajo):
        for a in self.alumnos:
            if a.legajo == legajo:
                return a
        return None


class GestorDeMaterias:

    def __init__(self):
        self.materias: list[Materia] = []

    def crear_materia(self, codigo, nombre, horas):
        self.materias.append(Materia(codigo, nombre, horas))

    def cargar_materias(self, cantidad=1):
        for i in range(cantidad):
            print(f"---- Cargando la {i+1}° materia ----")
            codigo = input("Código: ")

            while True:
                if self.buscar_materia(codigo) is None:
                    nombre = input("Nombre: ")
                    horas = int(input("Horas semanales: "))
                    if horas > 0:
                        self.crear_materia(codigo, nombre, horas)
                        break
                    else:
                        print("Horas inválidas")
                else:
                    print("Código duplicado")
                    codigo = input("Código: ")

    def mostrar_materias(self):
        if not self.materias:
            print("Aun no hay materias cargadas")
            return

        print("---- Materias ----")
        for m in self.materias:
            print(m)

    def modificar_materia(self):
        codigo = input("Código: ")
        materia = self.buscar_materia(codigo)

        if materia:
            nombre = input("Nuevo nombre: ")
            horas = input("Nuevas horas: ")

            if nombre != "":
                materia.set_nombre(nombre)
            if horas != "":
                materia.set_horas_semanales(int(horas))
        else:
            print("No existe")

    def eliminar_materia(self):
        codigo = input("Código: ")
        materia = self.buscar_materia(codigo)

        if materia:
            confirmacion = input(
                f"Confirma eliminar {materia}? (s/n): "
            ).lower().strip()

            if confirmacion in ("s", "si"):
                self.materias.remove(materia)
                print("Eliminada")
            else:
                print("Cancelado")
        else:
            print("No existe")

    def buscar_materia(self, codigo):
        for m in self.materias:
            if m.codigo == codigo:
                return m
        return None


class GestorDeInscripciones:

    def __init__(self, gestor_alumnos, gestor_materias):
        self.inscripciones: list[Inscripcion] = []
        self.gestor_alumnos = gestor_alumnos
        self.gestor_materias = gestor_materias

    def inscribir(self):
        legajo = int(input("Legajo alumno: "))
        codigo = input("Codigo materia: ")

        alumno = self.gestor_alumnos.buscar_alumno(legajo)
        materia = self.gestor_materias.buscar_materia(codigo)

        if alumno is None:
            print("Alumno no existe")
            return

        if materia is None:
            print("Materia no existe")
            return

        if self.buscar_inscripcion(alumno, materia):
            print("Ya está inscripto")
            return

        self.inscripciones.append(Inscripcion(alumno, materia))
        print("Inscripción realizada")

    def dar_baja(self):
        legajo = int(input("Legajo alumno: "))
        codigo = input("Codigo materia: ")

        alumno = self.gestor_alumnos.buscar_alumno(legajo)
        materia = self.gestor_materias.buscar_materia(codigo)

        if alumno is None or materia is None:
            print("Alumno o materia no existe")
            return

        inscripcion = self.buscar_inscripcion(alumno, materia)

        if inscripcion:
            self.inscripciones.remove(inscripcion)
            print("Inscripción eliminada")
        else:
            print("No existe inscripción")

    def listar(self):
        if not self.inscripciones:
            print("No hay inscripciones")
            return

        print("---- INSCRIPCIONES ----")
        for i in self.inscripciones:
            print(i)

    def buscar_inscripcion(self, alumno, materia):
        for i in self.inscripciones:
            if i.alumno == alumno and i.materia == materia:
                return i
        return None


mi_gestor_de_alumnos = GestorDeAlumnos()
mi_gestor_de_materias = GestorDeMaterias()
mi_gestor_de_inscripciones = GestorDeInscripciones(
    mi_gestor_de_alumnos,
    mi_gestor_de_materias
)


def mostrar_menu():
    print("------ MENU -------")
    print("1- Crear Alumno")
    print("2- Listar Alumnos")
    print("3- Modificar Alumno")
    print("4- Eliminar Alumno")
    print("5- Crear Materia")
    print("6- Listar Materias")
    print("7- Modificar Materia")
    print("8- Eliminar Materia")
    print("9- Inscribir alumno")
    print("10- Dar baja inscripción")
    print("11- Listar inscripciones")
    print("12- Salir")


def pedir_opcion():
    while True:
        op = int(input("Opción: "))
        if 1 <= op <= 12:
            return op
        print("Opción inválida")


while True:
    mostrar_menu()
    op = pedir_opcion()

    if op == 1:
        mi_gestor_de_alumnos.cargar_alumnos()
    elif op == 2:
        mi_gestor_de_alumnos.mostrar_alumnos()
    elif op == 3:
        mi_gestor_de_alumnos.modificar_alumno()
    elif op == 4:
        mi_gestor_de_alumnos.eliminar_alumno()

    elif op == 5:
        mi_gestor_de_materias.cargar_materias()
    elif op == 6:
        mi_gestor_de_materias.mostrar_materias()
    elif op == 7:
        mi_gestor_de_materias.modificar_materia()
    elif op == 8:
        mi_gestor_de_materias.eliminar_materia()

    elif op == 9:
        mi_gestor_de_inscripciones.inscribir()
    elif op == 10:
        mi_gestor_de_inscripciones.dar_baja()
    elif op == 11:
        mi_gestor_de_inscripciones.listar()

    else:
        print("Fin del programa")
        break















