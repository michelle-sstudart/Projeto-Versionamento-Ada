# Função para coletar informações sobre o pet e o tutor
def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet e seu tutor.")

    # Coleta do nome do pet
    nome_pet = input("Nome do pet: ")

    # Coleta do nome do tutor
    nome_tutor = input("Nome do tutor: ")

    # Coleta do endereço do tutor e pet
    endereco = input("Endereço: ")

    # Coleta do número do contato do Tutor
    while True:
        try:
            numero_tutor = input("Número do contato do Tutor (somente números): ")
        # Validação básica: verifica se o núero contém apenas digitos
            if numero_tutor.isdigit():
                break
            else:
                print("Por favor, insira apenas números para o contato: ")
        except ValueError:
            print("Ocorreu um erro. Tente novamente:")
             
    # Coleta da idade do pet, garantindo que seja um número inteiro
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    # Coleta do peso do pet, garantindo que seja um número flutuante
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

    # Exibindo as informações coletadas
    print("\nInformações do pet e do tutor")
    print(f"Nome do tutor: {nome_tutor}")
    print(f"Endereço: {endereco} ")
    print(f"Número do Contato do tutor: {numero_tutor}")
    print(f"Nome do pet: {nome_pet}")
    print(f"Idade do pet: {idade} anos")
    print(f"Peso do pet: {peso} kg")
    
# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
