import cpu_estado as ce

class CPU(object):
    """
    docstring
    """
    estado = ce.CPUEstado()
    
    mem_prog = []
    mem_dados = []
    instrucoes = ("CARGI", "CARGM", "CARGX", "ARMM", "ARMX", "SOMA", "NEG", "DESVZ")

    def __init__(self):
        pass

    def altera_programa(self, prog):
        """Altera o conteudo da memoria de programa"""
        self.mem_prog = prog

    def altera_dados(self, dados):
        """Altera o conteudo da memoria de dados"""
        self.mem_dados = dados

    def interrupcao(self):
        pass

    def retorna_interrupcao(self):
        pass

    def instucao(self):
        pass

    def salva_estado(self):
        pass

    def altera_estado(self, new_estado):
        pass

    def estado_inicializa(self):
        pass
    
    def executa(self):
        pass