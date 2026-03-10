class Reporte:
    def __init__(self, emisor, receptor, categoria, gravedad, comentario=""):
        self.emisor = emisor
        self.receptor = receptor
        self.categoria = categoria
        self.gravedad = gravedad  # 1-5
        self.comentario = comentario
        self.estado = "Pendiente"

class SistemaSeguridad:
    @staticmethod
    def ejecutar_veredicto(reporte, es_real):
        """Procesa reportes negativos y fake reports."""
        if es_real:
            puntos_a_restar = reporte.gravedad * 0.4
            reporte.receptor.ranking -= puntos_a_restar
            # No bajar de 0.0
            if reporte.receptor.ranking < 0: reporte.receptor.ranking = 0.0
            return f"PENALIZACIÓN: {reporte.receptor.nombre} perdió {puntos_a_restar:.1f} pts por {reporte.categoria}."
        else:
            reporte.emisor.ranking -= 1.5
            if reporte.emisor.ranking < 0: reporte.emisor.ranking = 0.0
            return f"FAKE REPORT: {reporte.emisor.nombre} penalizado con -1.5 pts por mentir."

    @staticmethod
    def premiar_jugador(receptor, motivo):
        """Sube el ranking por buen comportamiento o MVP."""
        # Definimos una subida estándar (puedes ajustarla)
        puntos_a_subir = 0.2
        ranking_previo = receptor.ranking
        receptor.ranking += puntos_a_subir

        # EL TECHO: Nadie puede ser más que un 5.0 perfecto
        if receptor.ranking > 5.0:
            receptor.ranking = 5.0

        return (f"PREMIO: {receptor.nombre} recibió +{puntos_a_subir} pts por {motivo}.\n"
                f"Ranking: {ranking_previo:.1f} -> {receptor.ranking:.1f}")

    @staticmethod
    def generar_ranking_top(lista_jugadores):
        return sorted(lista_jugadores, key=lambda j: j.ranking, reverse=True)