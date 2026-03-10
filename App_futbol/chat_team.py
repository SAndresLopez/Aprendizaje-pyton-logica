class Mensaje:
    def __init__(self, autor, contenido):
        self.autor = autor.nombre
        self.equipo = autor.equipo
        self.texto = contenido
        self.hora = "20:05"  # Aquí luego usarías la hora real


class SalaChat:
    def __init__(self, partido_id):
        self.partido_id = partido_id
        self.historial_equipo_A = []
        self.historial_equipo_B = []

    def enviar_mensaje(self, jugador, texto):
        # Creamos el objeto mensaje
        nuevo_msj = Mensaje(jugador, texto)

        # FILTRO CRÍTICO: ¿A qué buzón va?
        if jugador.equipo == "A":
            self.historial_equipo_A.append(nuevo_msj)
            return "✅ Mensaje enviado al equipo A"
        elif jugador.equipo == "B":
            self.historial_equipo_B.append(nuevo_msj)
            return "✅ Mensaje enviado al equipo B"

    def ver_chat_equipo(self, jugador):
        # Solo permite ver los mensajes si el jugador pertenece al equipo
        if jugador.equipo == "A":
            return [f"{m.autor}: {m.texto}" for m in self.historial_equipo_A]
        elif jugador.equipo == "B":
            return [f"{m.autor}: {m.texto}" for m in self.historial_equipo_B]
        else:
            return "🚫 No tienes acceso a ningún chat."


# --- EJEMPLO DE USO ---
chat_partido_8pm = SalaChat(partido_id=101)

# Jugador del equipo A escribe
chat_partido_8pm.enviar_mensaje(j1, "¡Muchachos, todos de blanco!")

# Jugador del equipo B intenta leer el chat de A
mensajes_para_j3 = chat_partido_8pm.ver_chat_equipo(j3)  # j3 es equipo B
# Resultado: j3 solo verá sus propios mensajes de equipo B, no los de j1.