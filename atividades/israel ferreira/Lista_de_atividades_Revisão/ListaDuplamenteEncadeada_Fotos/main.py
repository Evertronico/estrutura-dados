from GaleriaFotos import GaleriaFotos

def menu():
    print("=" * 50)
    print("||    <<<<<<<<<<<<MENU DE NAVEGAÇÃO DE FOTOS>>>>>>>>>>    ||")
    print("||    1) - ADICIONAR FOTO..................:    ||")
    print("||    2) - AVANÇAR PARA PRÓXIMA FOTO.......:    ||")
    print("||    3) - VOLTAR PARA FOTO ANTERIOR.......:    ||")
    print("||    4) - EXIBIR FOTO ATUAL...............:    ||")
    print("||    5) - EXIBIR GALERIA COMPLETA.........:    ||")
    print("||    6) - INFORMAR POSIÇÃO ATUAL..........:    ||")
    print("||    7) - SAIR............................:    ||")
    print("=" * 50)

def main():
    galeria = GaleriaFotos()

    while True:
        menu()
        opcao = input("- ")
        print("-" * 50)

        if opcao == "1":
            nome_foto = input("Nome da Foto para adicionar: ")
            galeria.adicionar_foto(nome_foto)
            print(f"Foto '{nome_foto}' adicionada com sucesso!")
        elif opcao == "2":
            if galeria.avancar_foto():
                print("Avançou para a próxima foto.")
            else:
                print("Não há próxima foto.")
        elif opcao == "3":
            if galeria.voltar_foto():
                print("Voltou para a foto anterior.")
            else:
                print("Não há foto anterior.")
        elif opcao == "4":
            print(galeria.exibir_foto_atual())
        elif opcao == "5":
            galeria.exibir_galeria()
        elif opcao == "6":
            print(galeria.informar_posicao_atual())
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        print("\n")

if __name__ == "__main__":
    main()
