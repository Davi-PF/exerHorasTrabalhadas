from datetime import datetime, timedelta


class HorasTrabalhadas:
    @staticmethod
    def calcular_horas_trabalhadas(hora_inicio, hora_termino, duracao_intervalo):
        try:
            # Adicione suporte para formatos H:mm ou HHmm
            if len(hora_inicio) == 4:
                formato = "%H%M"
            elif len(hora_inicio) == 5:
                formato = "%H:%M"
            else:
                raise ValueError("Formato de hora inválido.")

            hora_inicio = datetime.strptime(hora_inicio, formato)
            hora_termino = datetime.strptime(hora_termino, formato)
            duracao_intervalo = datetime.strptime(duracao_intervalo, formato)

            if duracao_intervalo >= timedelta(hours=24):
                raise ValueError("A duração do intervalo deve ser menor que 24 horas.")

            # Verificar se os horários estão invertidos e ajustar, se necessário
            if hora_termino < hora_inicio:
                hora_termino, hora_inicio = hora_inicio, hora_termino

            diferenca = hora_termino - hora_inicio - duracao_intervalo
            horas_trabalhadas = diferenca.total_seconds() / 3600

            return round(horas_trabalhadas, 2)
        except ValueError as e:
            raise ValueError(str(e))
        except Exception as e:
            raise Exception("Erro ao calcular as horas trabalhadas.")

    @staticmethod
    def validar_formato_hora(hora):
        try:
            # Adicione suporte para formatos H:mm ou HHmm
            if len(hora) == 4:
                formato = "%H%M"
            elif len(hora) == 5:
                formato = "%H:%M"
            else:
                raise ValueError("Formato de hora inválido.")

            datetime.strptime(hora, formato)
            return True
        except ValueError:
            return False
