import random
AANTAL_SCHEPEN = 3
aantal_pogingen = 0
AANTAL_RIJEN = 5
AANTAL_KOLOMMEN = 8

#bord_leeg = [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]

# bord_met_schepen = [["-","-","-","-"],#A1 [0,0], B1[0,1], C1[0,2], D1[0,3]
#                     ["-","-","-","-"], #A2 [1,0], B2[1,1], C2[1,2], D2[1,3]
#                     ["-","-","-","-"]] #A3 [2,0], B3[2,1], C3[2,2], D3[2,3]

#bord_met_schepen


#def maakLeegBord(bord_met_schepen):
def maakLeegBord():
    #maak eerst een rij
    bord_met_schepen = ["-"] * AANTAL_RIJEN
    for i in range(AANTAL_RIJEN):
        bord_met_schepen[i] = ["-"] * AANTAL_KOLOMMEN

    print("leeg bord gemaakt")
    return bord_met_schepen

# VUL BORD MET MAAR 1 SCHIP
def vulBordRandom(bord_met_schepen):
    # print("len(bord_met_schepen[0])-1", len(bord_met_schepen[0])-1)
    # print("len(bord_met_schepen)-1", len(bord_met_schepen)-1)

    randKolom = random.randint(0, len(bord_met_schepen[0])-1 ) #kolommen
    randRij = random.randint(0, len(bord_met_schepen)-1 ) #rijen
    print("randkolom:",randKolom, "randrij:",randRij)
    bord_met_schepen[randRij][randKolom]="S"


    # for i in range( len(bord_met_schepen[0])-1):
    #     for j in range( len(bord_met_schepen)-1):
    #         if randRij == j and randKolom == i:
    #             bord_met_schepen[randKolom][randRij] = "S"


    return bord_met_schepen

# Bewaak de vakjes om een ship met een L (leeg) vakje
def vulBordGereserveerdVakjesNaastSchepen (bord_met_schepen, randRij, randKolom):
        #vul vakjes om schepen met een L
    if randRij-1 >=0 and randKolom-1 >= 0 and not bord_met_schepen[randRij-1][randKolom-1] == "S":
        bord_met_schepen[randRij-1][randKolom-1] = "L"
    if randKolom-1 >= 0 and not bord_met_schepen[randRij][randKolom-1] == "S":
        bord_met_schepen[randRij][randKolom-1] = "L"
    if randRij+1 < AANTAL_RIJEN and randKolom-1 >= 0 and not bord_met_schepen[randRij+1][randKolom-1] == "S":
        bord_met_schepen[randRij+1][randKolom-1] = "L"
    if randRij-1 >= 0 and not bord_met_schepen[randRij-1][randKolom] == "S":
        bord_met_schepen[randRij-1][randKolom] = "L"
    if randRij+1 < AANTAL_RIJEN and not bord_met_schepen[randRij+1][randKolom] == "S":
        bord_met_schepen[randRij+1][randKolom] = "L"
    if randKolom+1 < AANTAL_KOLOMMEN and randRij-1 >= 0 and not bord_met_schepen[randRij-1][randKolom+1] == "S":
        bord_met_schepen[randRij-1][randKolom+1] = "L"
    if randKolom+1 < AANTAL_KOLOMMEN and not bord_met_schepen[randRij][randKolom+1] == "S":
        bord_met_schepen[randRij][randKolom+1] = "L"
    if randRij+1 < AANTAL_RIJEN and randKolom+1 < AANTAL_KOLOMMEN and not bord_met_schepen[randRij+1][randKolom+1] == "S":
        bord_met_schepen[randRij+1][randKolom+1] = "L"
    return bord_met_schepen

# #VUL BORD MET 2 SCHEPEN
def vulBordRandomMeerdereSchepen(bord_met_schepen):
    tellerSchepenGeplaatst = 0


    while tellerSchepenGeplaatst <= AANTAL_SCHEPEN:

        randKolom = random.randint(0, len(bord_met_schepen[0])-1 ) #kolommen
        randRij = random.randint(0, len(bord_met_schepen)-1 ) #rijen
        #print("attempting", randRij,randKolom)
        # if bord_met_schepen[randRij][randKolom] == "S":
        #     print("daar staat al een schip")
        # elif bord_met_schepen[randRij][randKolom] == "L":
        #     print("Daar in de buurt staat al een schip")
        # else:
        if (not bord_met_schepen[randRij][randKolom] == "S") and (not bord_met_schepen[randRij][randKolom] == "L"):
            bord_met_schepen[randRij][randKolom] = "S"
            bord_met_schepen = vulBordGereserveerdVakjesNaastSchepen( bord_met_schepen, randRij, randKolom )
            #toonBordMetL( bord_met_schepen )
            tellerSchepenGeplaatst += 1

    print("Er staan", tellerSchepenGeplaatst, "schepen van grote 1.")
    return bord_met_schepen


#FUNCTIE DEFINITIES
def vraagSpelerOmInvoer():
    invoerGoed = False
    while not invoerGoed:
        doelLetter = input("Welke kolom (letter) gok je?")
        doelLetter = doelLetter.upper()
        if(not len(doelLetter)==1):
            print("Voer maar een letter of een cijfer in!")

        elif ( ord(doelLetter)-65 < 0 ) or ( ord(doelLetter)-65 >= AANTAL_KOLOMMEN):
        #if doelLetter not in ["A", "B","C", "D"]:
            print("Incorrecte invoer voor kolom")

        else:
            doelCijfer = int(input("Welk rij kies je? "))
            #print("len:", len(bord_met_schepen))
            if doelCijfer <=0 or doelCijfer > len(bord_met_schepen):
                print("Incorrecte invoer voor rij")
            else: #zowel kolom als rij zijn OK
                print("Jouw gok is:", doelLetter, doelCijfer)
                invoerGoed = True

    #doelLetter="A"
    #doelCijfer=1
# print(ord('A'))#A i s65
# print(str(chr(65)))

    # if doelLetter == "A":
    #     doelKolom = 0
    # if doelLetter == "B":
    #     doelKolom = 1
    # if doelLetter == "C":
    #     doelKolom = 2
    # if doelLetter == "D":
    #     doelKolom = 3

    doelKolom = ord(doelLetter)-65

    doelCoordinaat = [ doelKolom, doelCijfer-1 ]
    print("doelCoordinaat:", doelCoordinaat)
    return doelCoordinaat

def toonBordMetL( bord ):
    #drukt af:( "  A B C D" )
    print( "-", end="" )
    for kolom in range (AANTAL_KOLOMMEN):
        print( str(chr(kolom+65)), end=" " )
    print()
    for rij in range( AANTAL_RIJEN ):
        print( rij+1, end=" ")
        for kolom in range( AANTAL_KOLOMMEN ):
            print( bord[rij][kolom], end=" " )
            #print( bord[rij][kolom]+ "rij:"+str(rij) + "kolom:"+ str(kolom) , end=" " )
        print()

def toonBord( bord ):
    #drukt af:( "  A B C D" )
    print( "  ", end="" )
    for kolom in range (AANTAL_KOLOMMEN):
        print( str(chr(kolom+65)), end=" " )
    print()
    for rij in range( AANTAL_RIJEN ):
        print( rij+1, end=" ")
        for kolom in range( AANTAL_KOLOMMEN ):
            if( bord[rij][kolom] == "L"):
                print( "-", end=" " )
            else:
                print( bord[rij][kolom], end=" " )
            #print( bord[rij][kolom]+ "rij:"+str(rij) + "kolom:"+ str(kolom) , end=" " )
        print()

def toonCoordinatenBord( bord ):
    #drukt af:( "  A B C D" )
    print( "  " , end="")
    for kolom in range (AANTAL_KOLOMMEN):
        print( str(chr(kolom+65)), end=" " )
    print()

    for rij in range( AANTAL_RIJEN ):
        print( rij+1, end=" ")
        for kolom in range( AANTAL_KOLOMMEN ):
            print( rij, kolom, end=" " )
            #print( bord[rij][kolom]+ "rij:"+str(rij) + "kolom:"+ str(kolom) , end=" " )
        print()

def spelIsAfgelopen( bord ):
     game_afgelopen = True
     for rij in range( AANTAL_RIJEN ):
        for kolom in range( AANTAL_KOLOMMEN ):
            if bord[rij][kolom]=="S":
                game_afgelopen = False
     #print("Game afgelopen:", game_afgelopen )
     return game_afgelopen

def verwerkSchot( bord, doelcoordinaat ):
     kolom = doelcoordinaat[0]
     rij = doelcoordinaat[1]

     if bord[rij][kolom]=="S":#er staat een schip
        bord[rij][kolom]="X" # vervang door een neergeschotten schip
        print("Schot (" +str(chr(kolom+65))+ "," + str(rij+1) +") is raak!")
#        return True
     else:
        print("Schot (" +str(chr(kolom+65))+ "," + str(rij+1) +") is mis!")
#        return False


#HOOFDPROGRAMMA
#bord_met_schepen = maakLeegBord(bord_met_schepen)#maak een leeg bord
bord_met_schepen = maakLeegBord()#maak een leeg bord
#bord_met_schepen = vulBordRandom(bord_met_schepen)#vul bord met schepen
bord_met_schepen = vulBordRandomMeerdereSchepen(bord_met_schepen)#vul bord met willekeurige schepen
toonBord( bord_met_schepen ) #toon op het scherm

while not spelIsAfgelopen( bord_met_schepen ): #zolang spel niet is afgelopen
    print("Het spel is nog niet afgelopen.")
    doelCoordinaat = vraagSpelerOmInvoer()  #vraag speler om invoer
    aantal_pogingen += 1  #tel poging
    verwerkSchot( bord_met_schepen, doelCoordinaat ) #controleer of hit/mis, pas bord aan en geef feedback aan gebruiker
    toonBord( bord_met_schepen )



print("Gefeliciteerd, je hebt gewonnen. Het heeft je " + str(aantal_pogingen ) + " beurten gekost.") #spel afgelopen: geef gebruiker een compliment



# ANSWER TIC TAC TOE
# from pcinput import getInteger
#
# "-" = "-"
# SPELERX = "X"
# SPELERO = "O"
# MAXZET = 9
#
# def toon_bord( b ):
#     print( "  1 2 3" )
#     for rij in range( 3 ):
#         print( rij+1, end=" ")
#         for kol in range( 3 ):
#             print( b[rij][kol], end=" " )
#         print()
#
# def opponent( p ):
#     if p == SPELERX:
#         return SPELERO
#     return SPELERX
#
# def neemRowKolom( speler, wat ):
#     while True:
#         num = getInteger( "Speler "+speler+", welke "+wat+
#             " kies je? " )
#         if num < 1 or num > 3:
#             print( "Geef 1, 2, of 3" )
#             continue
#         return num
#
# def winnaar( b ):
#     for rij in range( 3 ):
#         if b[rij][0] != "-" and b[rij][0] == b[rij][1] \
#             and b[rij][0] == b[rij][2]:
#             return True
#     for kol in range( 3 ):
#         if b[0][kol] != "-" and b[0][kol] == b[1][kol] \
#             and b[0][kol] == b[2][kol]:
#             return True
#     if b[1][1] != "-":
#         if b[1][1] == b[0][0] and b[1][1] == b[2][2]:
#             return True
#         if b[1][1] == b[0][2] and b[1][1] == b[2][0]:
#             return True
#     return False
#
# bord = [["-","-","-"],["-","-","-"],["-","-","-"]]
# speler = SPELERX
#
# toon_bord( bord )
# zet = 0
# while True:
#     rij = neemRowKolom( speler, "rij" )
#     kol = neemRowKolom( speler, "kolom" )
#     if bord[rij-1][kol-1] != "-":
#         print( "Rij", rij, "en kolom", kol, "is niet "-"" )
#         continue
#     bord[rij-1][kol-1] = speler
#     toon_bord( bord )
#     if winnaar( bord ):
#         print( "Speler", speler, "wint!" )
#         break
#     zet += 1
#     if zet == MAXZET:
#         print( "Het is gelijkspel." )
#         break
#     speler = opponent( speler )
