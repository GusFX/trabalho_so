import cpu_interrupcao as ci

class CPUEstado(object):
    """
    docstring
    """
    pc = 0
    acumulador = 0
    interrupcao = ci.CPUInterrupcao()

def get_modo(self):
    """Retorna modo de interrupcao da CPU"""
    return self.interrupcao.estado_atual

def set_modo_normal(self):
    if self.interrupcao.estado_atual != ci.NORMAL:
        self.interrupcao.estado_atual = ci.NORMAL
        self.interrupcao.pc += 1