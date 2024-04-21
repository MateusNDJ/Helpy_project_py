# Sistema de Login da Porto Seguro

# Define os planos de seguro disponíveis
planos_seguro = {
    1: "Básico",
    2: "Padrão",
    3: "Premium"
}

# Solicita informações do usuário
nome = input("Digite seu nome: ")
modelo_carro = input("Digite o modelo do seu carro: ")

# Exibe os planos de seguro disponíveis
print("\nPlanos de Seguro Disponíveis:")
for num_plano, nome_plano in planos_seguro.items():
    print(f"{num_plano}. {nome_plano}")

# Solicita a escolha do plano de seguro
while True:
    try:
        escolha_plano = int(input("\nDigite o número do plano de seguro desejado (1/2/3): "))
        if escolha_plano in planos_seguro:
            break
        else:
            print("Escolha inválida. Por favor, selecione um número de plano válido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número de plano válido.")

# Exibe as informações fornecidas pelo usuário
print("\nObrigado por fornecer as seguintes informações:")
print(f"Nome: {nome}")
print(f"Modelo do Carro: {modelo_carro}")
print(f"Plano de Seguro Selecionado: {planos_seguro[escolha_plano]}")

