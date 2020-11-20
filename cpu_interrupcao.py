class CPUInterrupcao(object):
    """
    docstring
    """
    NORMAL = 'normal'
    INSTRUCAO_ILEGAL = 'ilegal'
    VIOLACAO_MEM = 'violacao'

    estado_atual = ""

    def __init__(self):
        self.estado_atual = self.NORMAL
        