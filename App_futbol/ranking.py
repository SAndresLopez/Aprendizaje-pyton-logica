class SistemaRanking:
    def __init__(self, lista_jugadores):
        self.jugadores = lista_jugadores

    def obtener_top_10(self):
        # Ordenamos a los jugadores de mayor a menor ranking
        # Usamos 'reverse=True' para que el 5.0 esté arriba del 1.0
        ranking_ordenado = sorted(
            self.jugadores,
            key=lambda j: j.ranking,
            reverse=True
        )

        # Tomamos solo los primeros 10
        return ranking_ordenado[:10]

    def mostrar_tabla_honor(self):
        print("=== 🏆 TOP 10 MEJORES JUGADORES ===")
        top = self.obtener_top_10()

        for puesto, jugador in enumerate(top, start=1):
            # Formateamos para que se vea como una tabla real
            print(f"{puesto}. {jugador.nombre} | {jugador.ranking:.1f}⭐ | Equipo: {jugador.equipo}")


# --- SIMULACIÓN DE LA TABLA ---
# Creamos varios jugadores con diferentes puntajes para probar
j1 = Jugador("Andres", 22, "A")
j1.ranking = 4.8

j2 = Jugador("Carlos", 25, "B")
j2.ranking = 5.0

j3 = Jugador("Luis", 21, "A")
j3.ranking = 3.5  # (Seguro tiene muchos reportes jeje)

# Metemos a todos en una lista global
base_de_datos_usuarios = [j1, j2, j3]

# Ejecutamos el ranking
leaderboard = SistemaRanking(base_de_datos_usuarios)
leaderboard.mostrar_tabla_honor()