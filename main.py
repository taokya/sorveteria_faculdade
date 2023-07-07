# Definem-se os valores da sorveteria em forma de tupla, de acordo com o sabor escolhido
precos = {
    'tr': {1: 6, 2: 11, 3: 15},
    'pr': {1: 7, 2: 13, 3: 18},
    'es': {1: 8, 2: 15, 3: 21}
}

total = 0 # Armazena o valor total dos pedidos

# Mensagem de boas-vindas
print("Bem-vindo(a) a sorveteria de Jhenifer Ferreira Vaz")

for sabor, valores in precos.items(): # mostra o cardápio da sorveteria, usando o for para percorrer a lista de preços
    print(f"Sabor: {sabor}")
    for bolas, preco in valores.items():
        print(f"Opção: {bolas} bola(s) - Preço: R$ {preco:.2f}")
    print()

while True: # Enquanto o usuário escolher que quer continuar o pedido, o código volta ao início
    # Entrada do sabor na sorveteria
    sabor = input("Digite o sabor do sorvete (tr - tradicional, pr - premium, es - especisl): ")
    sabor
  
    # Verifica se o sabor é válido
    if sabor not in ['tr', 'pr', 'es']: # se o valor não estiver entre os informados, retorna mensagem de inválido
        print("Sabor de sorvete inválido!")
        continue
    
    # Entrada da quantidade de bolas de sorvete
    bolas_de_sorvete = input("Digite o número de bolas de sorvete (1, 2 ou 3): ")
    
    # Verificar se a quantidade de bolas é válida
    if bolas_de_sorvete not in ['1', '2', '3']: # se o valor não estiver entre os informados, retorna mensagem de inválido
        print("Quantidade de bolas de sorvete inválida!")
        continue
    
    # Calcula o preço total fazendo a varredura na tupla de precos
    valor_total = precos[sabor][int(bolas_de_sorvete)] # faz a conversão da variável bolas de str para int
    
    # Saída de console com o resumo do pedido
    print(f"Você pediu {bolas_de_sorvete} bola(s) de sorvete {sabor}.")
    print(f"Valor total: R$ {valor_total:.2f}")

    total += valor_total # Armazena o total anterior e o novo 
    
    # Perguntar se o cliente deseja pedir mais alguma coisa
    pedido = input("Deseja pedir mais alguma coisa? (s - Sim, n - Não): ")
    
    if pedido != 's': # Se a opção de continuar com o pedido for diferente de S o código acaba
      print("Agadecemos o pedido!")
      break

print(f"Valor total: R$ {total:.2f}")
