import cpu_interrupcao as ci

class CPUEstado(object):
    """
    docstring
    """
    pc = 0
    acumulador = 0
    interrupcao = ci.CPUInterrupcao()
