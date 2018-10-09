gewichtenLijst = [56.3, 54.3, 58.9]

nieuwGewicht = float (input ("Hoeveel weeg je?") )

if nieuwGewicht > gewichtenLijst[ len(gewichtenLijst)-1 ]:
    print("Je bent aangekomen")
    aangekomen = nieuwGewicht - gewichtenLijst[ len(gewichtenLijst)-1 ]
    print(aangekomen)

else:
    print("Je bent afgevallen")

gewichtenLijst += [nieuwGewicht]
# OF
#gewichtenLijst.append(nieuwGewicht)

#om te testen:
#print(gewichtenLijst)
