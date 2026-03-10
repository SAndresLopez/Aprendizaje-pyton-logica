class Partido:
    def __init__(self, hora, capacidad):
        self.hora = hora
        self.capacidad = capacidad
        self.titulares = []
        self.suplentes = []
        self.abierto = True

    def agregar_jugador(self, jugador):
        if len(self.titulares) < self.capacidad:
            jugador.es_titular = True
            self.titulares.append(jugador)
            return f"✅ {jugador.nombre} es Titular a las {self.hora}"
        else:
            jugador.es_titular = False
            self.suplentes.append(jugador)
            return f"⏳ {jugador.nombre} a Suplentes (Cupo lleno)"

class AdministradorCanchas:
    def __init__(self, nombre_establecimiento):
        self.nombre = nombre_establecimiento
        self.horarios_disponibles = {} # Diccionario { "19:00": Objeto Partido }

    def habilitar_horario(self, hora, capacidad):
        self.horarios_disponibles[hora] = Partido(hora, capacidad)
        print(f" Horario de las {hora} habilitado en {self.nombre}.")