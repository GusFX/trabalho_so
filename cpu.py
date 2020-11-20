import cpu_estado as ce


class CPU(object):
    """
    docstring
    """

    def CARGI(self, n):
        self.estado.acumulador = n
        print(n)


    estado = ce.CPUEstado()
    
    mem_prog = []
    mem_dados = []
    instrucoes = {"CARGI": CARGI, "CARGM":CARGM, "CARGX":CARGX, "ARMM":ARMM, "ARMX":ARMX, "SOMA":SOMA, "NEG":NEG, "DESVZ":DESVZ}

    def __init__(self):
        pass

    def altera_programa(self, prog):
        """Altera o conteudo da memoria de programa"""
        self.mem_prog = prog


    def altera_dados(self, dados):
        """Altera o conteudo da memoria de dados"""
        self.mem_dados = dados


    def get_interrupcao(self):
        """Le modo de interrupcao da CPU"""
        return self.estado.get_modo()


    def retorna_interrupcao(self):
        """Coloca CPU em modo normal ao voltar de uma interrupcao"""
        self.estado.set_modo_normal()


    def instucao(self):
        """Obtem instrucao do PC"""
        pc = self.estado.pc
        return mem_prog[pc]


    def salva_estado(self):
        """Obtem estado interno da CPU"""
        return self.estado


    def altera_estado(self, new_estado):
        """Altera estado interno da CPU"""
        self.estado = new_estado


    def estado_inicializa(self):
        """Inicializa o estado interno da CPU"""
        pass


    def executa(self):
        """Executa uma instrucao"""

        pc = self.estado.pc
        instrucao_atual = self.mem_prog[pc]
        inst,arg = instrucao_atual.split()
        

        self.instrucoes[0][inst](self, arg)


    #=========================== Execucao de instrucoes ========================#

    