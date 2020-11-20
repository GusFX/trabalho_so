import cpu 

def main():
    my_cpu = cpu.CPU()

    my_cpu.altera_programa(["CARGI 4"])
    my_cpu.executa()    


if __name__ == '__main__':
    main()