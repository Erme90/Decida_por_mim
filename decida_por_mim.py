#Iniciando projeto número 02 - decida por mim.
"""Objetivo: Crie um script que responda qualquer pergunta que for feita a ele.
Recomendo ter uma base de possíveis respostas (10-20 ou mais).
Ex: Será que devo sair de casa hoje? Seu script reponde: “Sim, vai lá!
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
import random
from tkinter import *
from tkinter import messagebox
from time import sleep
def oquefazer():
    listaresposta = ['Treinar Python e se alimentar direito', 'Assistir um programa divertido',
             'Já se hidratou hoje? Beba água','Leia um livro', 'Dá uma espiada no Insta',
                     'Faça sua tarefa que está acumulada!', 'Vai lavar a louça!',
                'Não sei, sou apenas um computador!', 'Faça o que quiser, você é livre :D',
            'Não entre em pânico!', 'Nada, tire o dia para descansar', 'Comece uma dieta!',
                     'Leve o cachorro para passear.', 'Vá dormir', 'Que tal um filme?',
                     'Meditação pode ajudar', 'Boa pergunta ^_^']
    resposta = random.choice(listaresposta)

    pensando = 'Deixe-me pensar...'
    texto_resposta['text'] = pensando

    texto_resposta2['text'] = resposta

#Área da interface
quadro = Tk()
quadro.title('Decida por mim')
quadro.geometry('350x350')

botao_fazer = Button(quadro,text='O que devo fazer?', padx=22, command=oquefazer)
botao_fazer.grid(column=0, row=0)

texto_resposta = Label(quadro,text='')
texto_resposta.grid(column=0, row=1)
sleep(1)
texto_resposta2 = Label(quadro,text='')
texto_resposta2.grid(column=0, row=2)

quadro.mainloop()

