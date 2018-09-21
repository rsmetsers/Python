from tkinter import *
import random
Window = Tk()


AANTAL_SCHEPEN = 1
aantal_pogingen = 0
AANTAL_RIJEN = 3
AANTAL_KOLOMMEN = 4
bord_met_schepen = []
gebruikers_bord_met_schepen = []

uitvoerTekst = StringVar()
doelCoordinaat = []
aantal_pogingen = 0

def maakLeegBord():
    global bord_met_schepen
    global gebruikers_bord_met_schepen
    #maak eerst een rij
    bord_met_schepen = ["-"] * AANTAL_RIJEN
    gebruikers_bord_met_schepen = ["-"] * AANTAL_RIJEN
    for i in range(AANTAL_RIJEN):
        bord_met_schepen[i] = ["-"] * AANTAL_KOLOMMEN
        gebruikers_bord_met_schepen[i] = ["?"] * AANTAL_KOLOMMEN
    print("leeg bord gemaakt")

def toonBord(  ):
    global bord_met_schepen
    #drukt af:( "  A B C D" )
    print( "  ", end="" )
    for kolom in range (AANTAL_KOLOMMEN):
        print( str(chr(kolom+65)), end=" " )
    print()
    for rij in range( AANTAL_RIJEN ):
        print( rij+1, end=" ")
        for kolom in range( AANTAL_KOLOMMEN ):
            print( bord_met_schepen[rij][kolom], end=" " )
            # if( bord_met_schepen[rij][kolom] == "L"):
            #     print( "-", end=" " )
            # else:
            #     print( bord_met_schepen[rij][kolom], end=" " )
            # #print( bord[rij][kolom]+ "rij:"+str(rij) + "kolom:"+ str(kolom) , end=" " )
        print()

# VUL BORD MET MAAR 1 SCHIP
def vulBordRandom():
    global bord_met_schepen
    # print("len(bord_met_schepen[0])-1", len(bord_met_schepen[0])-1)
    # print("len(bord_met_schepen)-1", len(bord_met_schepen)-1)

    randKolom = random.randint(0, len(bord_met_schepen[0])-1 ) #kolommen
    randRij = random.randint(0, len(bord_met_schepen)-1 ) #rijen
    print("randkolom:",randKolom, "randrij:",randRij)
    bord_met_schepen[randRij][randKolom]="S"

    #return bord_met_schepen


def knopjeGedrukt(celRij, celKolom):
    global aantal_pogingen
    aantal_pogingen += 1  #tel poging
    global uitvoerTekst
    print("gebruiker kiest:", celRij, celKolom)#, bord_met_schepen[cellRij][celKolom])
    if bord_met_schepen[celRij][celKolom] == "S":
        uitvoerTekst.set("Raak!")
        print("Schot (" +str(chr(celKolom+65))+ "," + str(celRij+1) +") is raak!")
        bord_met_schepen[celRij][celKolom] = "R"
        gebruikers_bord_met_schepen[celRij][celKolom] = "S"
    else:
        uitvoerTekst.set("Mis!")
        print("Schot (" +str(chr(celKolom+65))+ "," + str(celRij+1) +") is mis!")
        bord_met_schepen[celRij][celKolom] = "X"
        gebruikers_bord_met_schepen[celRij][celKolom] = "X"

    if spelIsAfgelopen():
        print("Schot (" +str(chr(celKolom+65))+ "," + str(celRij+1) +") is mis!")
        uitvoerTekst.set("Gefeliciteerd, je hebt gewonnen!")
        print("Gefeliciteerd, je hebt gewonnen. Het heeft je " + str(aantal_pogingen ) + " beurten gekost.") #spel afgelopen: geef gebruiker een compliment

    tekenSpelBord()



def tekenSpelBord():
    labelA = Label(Window, text="A").grid(row=0, column=1)
    labelB = Label(Window, text="B").grid(row=0, column=2)
    labelC = Label(Window, text="C").grid(row=0, column=3)
    labelD = Label(Window, text="D").grid(row=0, column=4)

    label1 = Label(Window, text="1").grid(row=1, column=0)
    buttonA1 = Button(Window, text=gebruikers_bord_met_schepen[0][0], command=lambda:knopjeGedrukt(0,0)).grid(row=1, column=1)
    buttonB1 = Button(Window, text=gebruikers_bord_met_schepen[0][1], command=lambda:knopjeGedrukt(0,1)).grid(row=1, column=2)
    buttonC1 = Button(Window, text=gebruikers_bord_met_schepen[0][2], command=lambda:knopjeGedrukt(0,2)).grid(row=1, column=3)
    buttonD1 = Button(Window, text=gebruikers_bord_met_schepen[0][3], command=lambda:knopjeGedrukt(0,3)).grid(row=1, column=4)

    label2 = Label(Window, text="2").grid(row=2, column=0)
    buttonA2 = Button(Window, text=gebruikers_bord_met_schepen[1][0], command=lambda:knopjeGedrukt(1,0)).grid(row=2, column=1)
    buttonB2 = Button(Window, text=gebruikers_bord_met_schepen[1][1], command=lambda:knopjeGedrukt(1,1)).grid(row=2, column=2)
    buttonC2 = Button(Window, text=gebruikers_bord_met_schepen[1][2], command=lambda:knopjeGedrukt(1,2)).grid(row=2, column=3)
    buttonD2 = Button(Window, text=gebruikers_bord_met_schepen[1][3], command=lambda:knopjeGedrukt(1,3)).grid(row=2, column=4)

    label3 = Label(Window, text="3").grid(row=3, column=0)
    buttonA3 = Button(Window, text=gebruikers_bord_met_schepen[2][0], command=lambda:knopjeGedrukt(2,0)).grid(row=3, column=1)
    buttonB3 = Button(Window, text=gebruikers_bord_met_schepen[2][1], command=lambda:knopjeGedrukt(2,1)).grid(row=3, column=2)
    buttonC3 = Button(Window, text=gebruikers_bord_met_schepen[2][2], command=lambda:knopjeGedrukt(2,2)).grid(row=3, column=3)
    buttonD3 = Button(Window, text=gebruikers_bord_met_schepen[2][3], command=lambda:knopjeGedrukt(2,3)).grid(row=3, column=4)
    uitvoer = Label(Window, textvariable=uitvoerTekst).grid(row=4, columnspan=5)

    # icoontjeR = PhotoImage(file="ship.png")
    # icoon_knop = Button(Window, image=icoontjeR).grid(row=5)

    # een plaatje op een knop
    icoontjeR = PhotoImage(file="R_icon.png")
    # zet plaatje ONDER tekst
    icoon_knop = Button(compound=BOTTOM, image=icoontjeR, text="knop").grid(row=5, columnspan=5)

    #TRYING TO FILL DYNAMICALLY DOENS"T WORK BECAUSE COORDIN D3 ARE ALWAYS GIVEN TO BUTTON
    # label = Label(Window, text="A").grid(row=0, column=1)
    # label = Label(Window, text="B").grid(row=0, column=2)
    # label = Label(Window, text="C").grid(row=0, column=3)
    # label = Label(Window, text="D").grid(row=0, column=4)
    #
    # label = Label(Window, text="1").grid(row=1, column=0)
    # label = Label(Window, text="2").grid(row=2, column=0)
    # label = Label(Window, text="3").grid(row=3, column=0)
    #
    #
    # for row in range (3):
    #     for kolom in range (4):
    #         button = Button(Window, text=bord_met_schepen[row][kolom], command=lambda:knopjeGedrukt(row,kolom)).grid(row=row+1, column=kolom+1)
    #
    # uitvoer = Label(Window, textvariable=uitvoerTekst).grid(row=4, columnspan=4)
    #


# var = tkinter.StringVar()
# entryField = tkinter.Entry(master, textvariable=var)
# e.pack()
#
# var.set("a new value") # entryField text now updated with this value

#uitvoer = Label(Window, textvariable=uitvoerTekst).grid(row=2)




def spelIsAfgelopen(  ):
     global bord_met_schepen
     game_afgelopen = True
     for rij in range( AANTAL_RIJEN ):
        for kolom in range( AANTAL_KOLOMMEN ):
            if bord_met_schepen[rij][kolom]=="S":
                game_afgelopen = False
     #print("Game afgelopen:", game_afgelopen )
     return game_afgelopen

#HOOFDPROGRAMMA
#bord_met_schepen = maakLeegBord(bord_met_schepen)#maak een leeg bord
# maakLeegBord()#maak een leeg bord
# vulBordRandom()#vul bord met schepen
# #bord_met_schepen = vulBordRandomMeerdereSchepen(bord_met_schepen)#vul bord met willekeurige schepen
#toonBord( ) #toon op het scherm
maakLeegBord()
vulBordRandom()
toonBord()
tekenSpelBord()

if spelIsAfgelopen():
    Window.quit()

Window.mainloop()


