from Usuarios import Jugador
from cancha import Partido
from Seguridad import SistemaSeguridad, Reporte

# 1. Preparación del partido
partido_estelar = Partido("19:00", 10)

# 2. Creamos los jugadores (Todos empiezan en 5.0)
j1 = Jugador("Andres", 22, "A")
j2 = Jugador("Carlos", 25, "A")
j3 = Jugador("Rivaldo", 24, "B")

for j in [j1, j2, j3]:
    partido_estelar.inscribir_jugador(j)

print("--- INICIO DEL PARTIDO ---")

# 3. Escenario A: Reporte Negativo (Alguien no pagó)
print("\n[Suceso]: El jugador Rivaldo reporta que Carlos no pagó.")
rep_pago = Reporte(j3, j2, "No_Pago", 5, "Se fue sin dejar su parte.")
print(SistemaSeguridad.ejecutar_veredicto(rep_pago, es_real=True))

# 4. Escenario B: Premiación (MVP del partido)
# Digamos que Andres jugó increíble y todos lo votan.
print("\n[Suceso]: El equipo vota a Andres como el mejor jugador.")
# Primero le bajamos un poco para probar que sube (simulando que tenía 4.0)
j1.ranking = 4.0
print(SistemaSeguridad.premiar_jugador(j1, "MVP del encuentro"))

# 5. Escenario C: Intento de subir más allá del 5.0
# Si alguien ya es perfecto, no sube más.
print("\n[Suceso]: Intentando premiar a un jugador con 5.0")
print(SistemaSeguridad.premiar_jugador(j3, "Juego Limpio"))

# 6. RESULTADO FINAL DEL EVENTO
print("\n=== TABLA DE POSICIONES DEL EVENTO ===")
top_10 = SistemaSeguridad.generar_ranking_top(partido_estelar.obtener_todos())
for i, jugador in enumerate(top_10, 1):
    print(f"{i}. {jugador}")