class SistemaSeguridad:
    @staticmethod
    def procesar_reporte(emisor, receptor, motivo, gravedad, es_real):
        if es_real:
            # Penaliza al infractor
            receptor.ranking -= (gravedad * 0.4)
            receptor.reportes_recibidos.append(motivo)
            return f"⚠️ Reporte validado contra {receptor.nombre}."
        else:
            # Penaliza al mentiroso (Fake Report)
            emisor.ranking -= 2.0
            return f"🚫 Reporte FALSO. Penalización para el emisor: {emisor.nombre}."

    @staticmethod
    def validar_chat(usuario1, usuario2):
        if usuario1.equipo == usuario2.equipo:
            return "🔓 Chat permitido (Mismo equipo)."
        return "🔒 Chat bloqueado (Equipos diferentes)."