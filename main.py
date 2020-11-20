import cpu 

def main():

    programa = ["CARGI 10",
                "ARMM 2",
                "CARGI 32",
                "SOMA 2",
                "ARMM 0",
                "PARA"]

    dados = [0] * 4

    my_cpu = cpu.CPU()

    my_cpu.altera_programa(programa)
    my_cpu.altera_dados(dados)

    while my_cpu.get_interrupcao() == "normal":
        my_cpu.executa()    

    inst = my_cpu.instucao()
    dados = my_cpu.mem_dados
    d = dados[0]

    print(f"CPU parou na instrução {inst} (deve ser PARA)")
    print(f"O valor de m[0] é {dados[0]} (deve ser 42)")

if __name__ == '__main__':
    main()