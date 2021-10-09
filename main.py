from Domain.interface import Interface

def __main__():
    fin = False
    cli = Interface()
    cli.quiUtilise()
    while fin is False:
        choix = cli.faireChoix()
        cli.lancerAction(choix)
        fin = cli.fin()


__main__()

