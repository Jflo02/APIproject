from Domain.interface import Interface

fin = False

cli = Interface()
cli.quiUtilise()
while fin is False:
    choix = cli.faireChoix()
    print(choix)
    fin = cli.fin()


