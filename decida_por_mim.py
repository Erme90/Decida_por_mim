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
import datetime
import random
from tkinter import *
from tkinter import messagebox
import time
def oquefazer():
    listaresposta = ['Treinar Python e se alimentar direito', 'Assistir um programa divertido',
             'Já se hidratou hoje? Beba água.','Leia um livro.', 'Dá uma espiada no Insta.',
             'Faça sua tarefa que está acumulada!', 'Vai lavar a louça!',
             'Não sei, sou apenas um computador!', 'Faça o que quiser, você é livre :D',
             'Não entre em pânico!', 'Nada, tire o dia para descansar', 'Comece uma dieta!',
             'Leve o cachorro para passear.', 'Vá dormir', 'Que tal um filme?',
             'Meditação pode ajudar', 'Boa pergunta!', 'Comece algo novo!']

    resposta = random.choice(listaresposta)
    fazer_resposta['text'] = resposta

def horas():
    horas = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    horario = [f'{horas}:{min}:{sec}']
    horas_resposta['text'] = horario

def comida():
    listacomida = ['pizza.', 'Hamburguer.', 'Já almoçou? Come um doce!',
                   'Algo saudável, como um MC Donalds', 'Nada! Você já comeu demais',
                   'Beba água', 'Churrasco!', 'Arroz e feijão','Macarrão vai bem!',
                   'Um suco de laranja talvez?', 'Come um doce e se arrependa',
                   'Pão com ovo', 'Ração de gato? Não sei o que humanos comem',
                   'Desculpe, sem ideias','Comida japonesa!', 'Comida mexicana!',
                   'Um omelete com queijo', 'Mas já tá com fome???', 'Nada, regime já!',
                   'Uma salada', 'Vocês comem oquê?', 'Um terabyte de dados??',
                   'Adeus e obrigado pelos peixes!', 'Frango assado', 'Bolo de chocolate']
    randomiza = random.choice(listacomida)
    comida_randomiza['text']=randomiza
#Área da interface
quadro = Tk()
quadro.title('Decida por mim')
quadro.geometry('300x300')

#função (O que fazer)
botao_fazer = Button(quadro,text='O que devo fazer?'
                     ,bg='#00f100', command=oquefazer)
botao_fazer.grid(column=0, row=0, padx=70, pady=10)
fazer_resposta = Label(quadro,text='')
fazer_resposta.grid(column=0, row=1)

#função (Horas)
botao_horas = Button(quadro,text='Me diga as horas',
                     bg='#f000f0', command=horas)
botao_horas.grid(column=0, row=2, padx=70, pady=10)
horas_resposta = Label(quadro,text='')
horas_resposta.grid(column=0, row=3)

#função (comida)
botao_comida = Button(quadro,text='O que devo comer?',bg='#ffff00', command=comida)
botao_comida.grid(column=0, row=4)
comida_randomiza = Label(quadro,text='')
comida_randomiza.grid(column=0, row=5)

quadro.mainloop()

