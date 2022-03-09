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
#adicionar interface
import random
from tkinter import *
from tkinter import messagebox
import time
def oquefazer():
    listaresposta = ['Treinar Python e se alimentar direito', 'Assistir um programa divertido',
             'Já se hidratou hoje? Beba água','Leia um livro', 'Dá uma espiada no Insta',
             'Faça sua tarefa que está acumulada!', 'Vai lavar a louça!',
             'Não sei, sou apenas um computador!', 'Faça o que quiser, você é livre :D',
             'Não entre em pânico!', 'Nada, tire o dia para descansar', 'Comece uma dieta!',
             'Leve o cachorro para passear.', 'Vá dormir', 'Que tal um filme?',
             'Meditação pode ajudar', 'Boa pergunta!']

    resposta = random.choice(listaresposta)
    texto_resposta['text'] = resposta

def horas():
    horario= time.clock()

#Área da interface
quadro = Tk()
quadro.title('Decida por mim')
quadro.geometry('300x500')

botao_fazer = Button(quadro,sleep(1),text='O que devo fazer?'
                     ,bg='#00f100', command=oquefazer)
botao_fazer.grid(column=0, row=0, padx=70, pady=30)

texto_resposta = Label(quadro,text='')
texto_resposta.grid(column=0, row=2)

quadro.mainloop()

