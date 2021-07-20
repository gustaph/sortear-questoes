# bibliotecas obrigatorias
import numpy as np
import random

# bibliotecas opcionais
from beautifultable import BeautifulTable           # pip install beautifultable
from termcolor import colored                       # pip install termcolor

class Sorteio:
    def __init__(self, componentes):
        self.componentes = componentes
        self.nro_componentes = len(self.componentes)
        self.divisao = {componente: [] for componente in self.componentes}

    def exibir_dados_formatados(self):
        """
        > Exibe a divisão do conteúdo para os integrantes em uma tabela
        Se não quiser instalar as bibliotecas opcionais, comente essa função
        """
        tabela = BeautifulTable()
        for nome, questoes in self.divisao.items():
            sQuestoes = ', '.join([str(q) for q in questoes])
            tabela.rows.append([nome, colored(len(questoes), "green"), colored(sQuestoes, "yellow")])
        tabela.columns.header = ["Nome", "Qtd", "Questões"]
        print(tabela)

    def exibir_dados(self):
        for key, value in self.divisao.items():
            exibicao = f"{key:10s}:\tQtd:{len(value)} -> {value}"
            print(exibicao)
            print('-' * (len(exibicao) + 5))

    def sortear_questoes(self, conteudos):
        """
        @param conteudos -> list: recebe a lista de conteúdos e temas
        """
        divisao, resto = divmod(len(conteudos), self.nro_componentes)

        questoes_escolhidas = []
        for _ in range(self.nro_componentes):
            conjunto = random.sample(conteudos, divisao)
            questoes_escolhidas.append(conjunto)
            for questao in conjunto:
                del conteudos[conteudos.index(questao)]

        iQuestoes = iter(questoes_escolhidas)
        for cmpt in self.componentes:
            self.divisao[cmpt].extend(next(iQuestoes))

        if resto > 0:
            random.shuffle(self.componentes)
            ii = 0
            iComponentes = iter(self.componentes)
            while ii < len(conteudos):
                self.divisao[next(iComponentes)].extend([conteudos[ii]])
                del conteudos[conteudos.index(conteudos[ii])]

        self.exibir_dados_formatados()
        #self.exibir_dados()   # use essa função se não baixou as bibliotecas opcionais
        return

# TESTES
s = Sorteio(['Integrante 1', 'Integrante 2', 'Integrante 3', 'Integrante 4'])
nro_questoes = 23
questoes = np.arange(1, nro_questoes+1).tolist()  # é preciso estar no formato de lista
s.sortear_questoes(questoes)

s1 = Sorteio(['Integrante 1', 'Integrante 2', 'Integrante 3', 'Integrante 4', 'Integrante 5'])
temas = ["História", "Matemática", "Filosofia", "Português"]
s1.sortear_questoes(temas)