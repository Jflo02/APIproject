from Domain.interface import Interface

fin = False

cli = Interface()
cli.quiUtilise()
while fin is False:
    choix = cli.faireChoix()
    print(choix)
    resultat = cli.lancerAction(choix)
    print(resultat)
    fin = cli.fin()


