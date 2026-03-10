from usuarios import Jugador
from cancha import AdministradorCanchas
from seguridad import SistemaSeguridad

# 1. El dueño avisa disponibilidad
mi_complejo = AdministradorCanchas("Canchas El Pibe")
mi_complejo.habilitar_horario("20:00", 10) # 10 jugadores para las 8 PM

# 2. Se registran jugadores
prospecto = Jugador("Andres", 22, "A")
partido_8pm = mi_complejo.horarios_disponibles["20:00"]
print(partido_8pm.agregar_jugador(prospecto))

# 3. Prueba de seguridad (Reporte falso)
troll = Jugador("User123", 19, "B")
resultado = SistemaSeguridad.procesar_reporte(troll, prospecto, "Insultos", 5, False)
print(resultado)
print(f"Ranking del troll ahora: {troll.ranking}")