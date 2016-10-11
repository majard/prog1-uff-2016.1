valor = eval(input('R$ '))
valor *= 100  #transforma real pra centavos
valor = int(valor)  #transforma valor em um número inteiro
moedasDe1Real = valor//100
valor %= 100  #deixa apenas o resto da divisão por 100 centavos (1 real) na variável valor
moedasDe50 = valor//50
valor %= 50
moedasDe25 = valor//25
valor %= 25
moedasDe10 = valor//10
valor %= 10
moedasDe5 = valor//5
valor %= 5
print(moedasDe1Real, 'moedas de 1 Real, ', moedasDe50, 'moedas de 50 centavos, ', moedasDe25, 'moedas de 25 centavos,',
      moedasDe10, 'moedas de 10 centavos', valor, 'moedas de 1 centavo')
