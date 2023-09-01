import random

quiz = {"Existem 4 casas em Hogwarts":"V",
"O nome do dragão do Hagrid do 1º livro é Petucho":"F",
"O feitiço usado para levitar coisas é o Wingardium leviosa":"V",
"O lugar onde Harry foi levado para comprar os materiais no primeiro ano de Hogwarts foi a Dedos de mel":"F",
"O Feitiço para conjurar água é aquamenti":"V",
"São 3 relíquias da morte ":"V",
"O patrono da Hermione é um cervo?":"F",
"Devo usar o patrono na presença de um animago":"F",
"A Marca Negra é o símbolo dos Comensais da Morte?": "V",
"O patrono de Harry é uma coruja?": "F",
"Sirius Black é o padrinho de Harry?": "V",
"A casa de Slytherin é conhecida por seu lema 'Coragem'": "F",
"O guardião do Beco Diagonal é o dragão Norberto?": "F",
"O Chapéu Seletor decide a qual casa cada estudante pertence?": "V",
"A varinha de Harry contém a pena de uma fênix?": "V",
"O pomo de ouro é o objeto mais importante no jogo de quadribol?": "F",
"A pedra filosofal é um dos objetos das Relíquias da Morte?": "F",
"O guardião do castelo de Hogwarts é um hipogrifo chamado Bicuço?": "F"
}

perguntas_aleatorias = random.sample(list(quiz.keys()), len(quiz))

pontos = 0

for pergunta in perguntas_aleatorias:
    resposta = input(pergunta)
    if resposta != quiz[pergunta]:
        print("Opção errada")
        pontos = pontos - 1
    else:
        print("Opção correta")
        pontos = pontos + 1
print(pontos)
