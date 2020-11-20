from cpu_interrupcao import CPUInterrupcao

class CPUEstado(object):
    """
    docstring
    """
    pc = 0
    acumulador = 0
    interrupcao = CPUInterrupcao()

    def get_modo(self):
        """Retorna modo de interrupcao da CPU"""
        return self.interrupcao.estado_atual

    def set_modo_normal(self):
        if self.interrupcao.estado_atual != CPUInterrupcao.NORMAL:
            self.interrupcao.estado_atual = CPUInterrupcao.NORMAL
            self.interrupcao.pc += 1

    def set_modo_ilegal(self):
        self.interrupcao.estado_atual = CPUInterrupcao.INSTRUCAO_ILEGAL

    def set_modo_violacao(self):
        self.interrupcao.estado_atual = CPUInterrupcao.VIOLACAO_MEM