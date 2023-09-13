from horas_trabalhadas import HorasTrabalhadas


def main():
    while True:
        print("\nOpções:")
        print("1 - Calcular horas trabalhadas")
        print("2 - Validar formato de hora")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            hora_inicio = input("Digite a hora de início (H:mm ou HHmm): ")
            hora_termino = input("Digite a hora de término (H:mm ou HHmm): ")
            duracao_intervalo = input("Digite a duração do intervalo (H:mm ou HHmm): ")

            try:
                horas_trabalhadas = HorasTrabalhadas.calcular_horas_trabalhadas(
                    hora_inicio, hora_termino, duracao_intervalo
                )
                print(f"Horas trabalhadas: {horas_trabalhadas} horas")
            except ValueError as e:
                print(f"Erro: {str(e)}")
            except Exception as e:
                print("Erro inesperado ao calcular horas trabalhadas.")

        elif escolha == "2":
            hora = input("Digite a hora para validar o formato (H:mm ou HHmm): ")
            if HorasTrabalhadas.validar_formato_hora(hora):
                print("Formato de hora válido.")
            else:
                print("Formato de hora inválido.")

        elif escolha == "3":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
