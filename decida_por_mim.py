#Iniciando projeto número 02 - decida por mim.
"""Objetivo: Crie um script que responda qualquer pergunta que for feita a ele.
Recomendo ter uma base de possíveis respostas (10-20 ou mais).
Ex: Será que devo sair de casa hoje? Seu script reponde: “Sim, vai lá!”

Detalhes e boas Práticas:
Habilidades praticas a aplicar:
    Listas
    Random
    Laços de Repetição
    Input de dados
    Saida de dados
    Geração de valores"""
#IDEIAS
#Faça a lista de todas as possíveis respostas primeiro.
#Tente adicionar uma que pergunte a data.
#Tente adicionar uma, que fale problemas matematicos....

respostas = ('Treinar Python e se alimentar direito', 'Claro, escolha um programa!')
while True:
    pergunta = str(input('Faça uma pergunta: ')).strip()
    if pergunta == 'O que devo':
        print('O que?')
    elif pergunta in 'O que devo fazer hoje?':
        print(respostas[0])
        opcao = str(input('Algo mais? ')).strip()
        if opcao in 'Nn':
            print('Beleza, nos falamos depois!')
            break
    elif pergunta in 'Vamos assistir algo' or 'Vamos assistir' or 'Vamos assistir tvTV':
        print(respostas[1])
