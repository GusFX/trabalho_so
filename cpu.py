import cpu_estado as ce


class CPU(object):
    """
    docstring
    """

    #=========================== Execucao de instrucoes ========================#
    
    def CARGI(self, n):
        self.estado.acumulador = n

    def CARGM(self, n):
        mem = self.mem_dados[n]
        self.estado.acumulador = mem

    def CARGX(self, n):
        mem = self.mem_dados[n]
        mem = self.mem_dados[mem]
        self.estado.acumulador = mem
    
    def ARMM(self, n):
        ac = self.estado.acumulador
        self.mem_dados[n] = ac

    def ARMX(self, n):
        ac = self.estado.acumulador
        mem = self.mem_dados[n]
        self.mem_dados[mem] = ac
    
    def SOMA(self, n):
        mem = self.mem_dados[n]
        self.estado.acumulador += mem

    def NEG(self, n):
        self.estado.acumulador = -self.estado.acumulador


    def DESVZ(self, n):
        ac = self.estado.acumulador
        if ac == 0:
            estado.pc = n 


    instrucoes = {"CARGI": CARGI, "CARGM":CARGM, "CARGX":CARGX, "ARMM":ARMM, "ARMX":ARMX, "SOMA":SOMA, "NEG":NEG, "DESVZ":DESVZ}


#====================================================================#


    estado = ce.CPUEstado()
    
    mem_prog = []
    mem_dados = []

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



    